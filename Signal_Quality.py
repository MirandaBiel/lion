from numpy import min, max, mean, std, abs, log

def PPG_analysis(signal: list, window_size: int, SQI: str) -> dict:
    """
    Analyzes PPG signal quality.

    Parameters:
        signal (list): The PPG signal data as a list of values.
        window_size (int): Size of the window for analysis.
        SQI (str): Type of signal quality indicator to use.
                   Options:
                   - 'Perfusion'
                   - 'Skewness'
                   - 'Kurtosis'
                   - 'Entropy'
                   - 'ZCR'
                   - 'SNR'

    Returns:
        dict: The signal segment with the SQI value closest to zero.
        {'Window': window, 'SQI': SQI}
    """

    best_sqi = float('inf')             # Inicializa com um valor muito alto
    best_window = None
    
    if SQI == 'Perfusion':
        for i in range(0, len(signal) - window_size + 1):
            window = signal[i : i + window_size]
            PSQI = Perfusion(window)    # Calcula o SQI proposto para a janela atual
            
            # Verifica se o SQI atual é o proximo de 0
            if abs(PSQI) < best_sqi:
                best_sqi = PSQI
                best_window = window

        return {"Window": best_window, "SQI": best_sqi}
    
    elif SQI == 'Skewness':
        for i in range(0, len(signal) - window_size + 1):
            window = signal[i : i + window_size]
            SSQI = Skewness(window)    # Calcula o SQI proposto para a janela atual
            
            # Verifica se o SQI atual é o proximo de 0
            if abs(SSQI) < best_sqi:
                best_sqi = SSQI
                best_window = window

        return {"Window": best_window, "SQI": best_sqi}

    elif SQI == 'Kurtosis':
        for i in range(0, len(signal) - window_size + 1):
            window = signal[i : i + window_size]
            KSQI = Kurtosis(window)    # Calcula o SQI proposto para a janela atual
            
            # Verifica se o SQI atual é o proximo de 0
            if abs(KSQI) < best_sqi:
                best_sqi = KSQI
                best_window = window

        return {"Window": best_window, "SQI": best_sqi}
    
    elif SQI == 'Entropy':
        for i in range(0, len(signal) - window_size + 1):
            window = signal[i : i + window_size]
            ESQI = Entropy(window)    # Calcula o SQI proposto para a janela atual
            
            # Verifica se o SQI atual é o proximo de 0
            if abs(ESQI) < best_sqi:
                best_sqi = ESQI
                best_window = window

        return {"Window": best_window, "SQI": best_sqi}
    
    elif SQI == 'ZCR':
        for i in range(0, len(signal) - window_size + 1):
            window = signal[i : i + window_size]
            ZSQI = Zero_Crossing_rate(window)    # Calcula o SQI proposto para a janela atual
            
            # Verifica se o SQI atual é o proximo de 0
            if abs(ZSQI) < best_sqi:
                best_sqi = ZSQI
                best_window = window

        return {"Window": best_window, "SQI": best_sqi}
    
    elif SQI == 'SNR':
        for i in range(0, len(signal) - window_size + 1):
            window = signal[i : i + window_size]
            NSQI = SNR(window)    # Calcula o SQI proposto para a janela atual
            
            # Verifica se o SQI atual é o proximo de 0
            if abs(NSQI) < best_sqi:
                best_sqi = NSQI
                best_window = window

        return {"Window": best_window, "SQI": best_sqi}

    else:
        return print(f"Error: SQI: {SQI} not found")

""" 
    As funções abaixo devem receber um sinal PPG no formato list ou np.array
    e retornam os respectivos resultados da analise do sinal PPG.
"""

def Perfusion(signal: list) -> float:
    """The perfusion index is a standard measure for evaluating 
    PPG signal quality. It is calculated as the ratio of pulsatile 
    blood f low to static blood in peripheral tissue, often 
    obtained from a pulse oximeter
    """

    y_min = min(signal)
    y_max = max(signal)
    x = mean(signal)
    PSQI = ((y_max - y_min)/x)*100
    
    return round(PSQI, 4)

def Skewness(signal: list) -> float:
    """Skewness is a measure of the asymmetry of a prob ability
    distribution and is related to distorted PPG signals"""

    N = len(signal)
    x = mean(signal)
    dp = std(signal)
    sum = 0
    for i in range(1, N):
        sum += (signal[i] - x) / dp
    SSQI = (1/N) * sum

    return round(SSQI, 4)

def Kurtosis(signal: list) -> float:
    """Kurtosis measures how the tails of a distribution differ 
    from those of a normal distribution. It determines if extreme 
    values are present in the distribution and has been found to 
    be a good indicator of PPG signal quality."""

    N = len(signal)
    x = mean(signal)
    dp = std(signal)
    sum = 0
    for i in range(0, N):
        sum += (signal[i] - x) / dp
    KSQI = (1/N) * sum

    return round(KSQI, 4)

def Entropy(signal: list) -> float:
    """Entropy quantifies the uncertainty in a signal probability density 
    function (PDF) and is anothereffective indicator of PPG signal quality"""

    N = len(signal)
    sum = 0
    for i in range(i, N):
        sum += signal[i]^2 * log(signal[i]^2)
    ESQI = -sum

    return round(ESQI, 4)

def Zero_Crossing_rate(signal: list) -> float:
    """The zero crossing rate indicates the rate of sign changes in the signal, 
    representing how often the signal changes from positive to negative"""

    N = len(signal)
    zero_crossings = 0
    for i in range(1, N):
        if (signal[i-1] > 0 and signal[i] < 0) or (signal[i-1] < 0 and signal[i] > 0):
            zero_crossings += 1
    ZSQI = (1/N) * zero_crossings

    return round(ZSQI, 4)

def SNR(signal: list) -> float:
    """This SQI compares the power of the desirable signal to the power of undesired background noise"""

    abs_signal = abs(signal)
    dp_signal = std(abs_signal)
    dp_noise = std(signal)
    if dp_noise == 0:
        return float('inf') if dp_signal > 0 else 0
    NSQI = (dp_signal^2) / (dp_noise^2)

    return round(NSQI, 4)
