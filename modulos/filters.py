from scipy.signal import butter, filtfilt
import numpy as np

# Apenas normaliza o sinal usando Z-score
def filter_z(signal):
    # Z-Score Normalizacao 
    x = np.mean(signal)
    dp = np.std(signal)
    norm_signal = (signal - x) / dp

    return norm_signal

# Apenas filtro de butterworth
def filter_butterworth(signal, fs, order=2):
    # Aplica o filtro de passa banda
    f_low = 0.6
    f_high = 3.6

    # Calcular as frequências normalizadas
    wn_low = 2 * f_low / fs
    wn_high = 2 * f_high / fs

    # Calcular os coeficientes do filtro Butterworth
    b, a = butter(order, [wn_low, wn_high], btype='band')

    # Aplicar o filtro passa-faixa
    y = filtfilt(b, a, signal)

    return y

# Normaliza Z-Score e aplica o filtro de ButterWorth
def filter_z_butterworth(signal, fs):
    
    y = filter_butterworth(filter_z(signal), fs)

    return y

# Alinha a onda no eixo x e aplica o filtro de Butterworth
def filter_align_buterworth(signal, fs):
    x = np.mean(signal)
    signal = (signal - x)

    y = filter_butterworth(signal, fs)

    return y
