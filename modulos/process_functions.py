from scipy.signal import butter, filtfilt, find_peaks
from scipy.interpolate import CubicSpline
from scipy.linalg import inv
import numpy as np

# Apenas normaliza o sinal usando Z-score
def filter_z(signal):
    # Z-Score Normalizacao 
    x = np.mean(signal)
    dp = np.std(signal)
    norm_signal = (signal - x) / dp

    return norm_signal

# Apenas filtro de butterworth
def filter_butterworth(signal, fs, order=6):
    # Aplica o filtro de passa banda
    nyquist = 0.5 * fs
    f_low = 0.6
    f_high = 3.6

    # Calcular as frequências normalizadas
    wn_low = 2 * f_low / nyquist
    wn_high = 2 * f_high / nyquist

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

# Passa alta detrending
def detrending_highpass_filter(signal, fs, lambda_value=300):
    # Calcula a frequência de corte normalizada com base no parâmetro lambda
    normalized_cutoff = 0.011 * lambda_value
    
    # Calcula a frequência de corte em Hz
    cutoff_freq = normalized_cutoff * fs
    
    # Calcula a matriz D de diferenças de segunda ordem
    n = len(signal)
    D = np.zeros((n - 3, n - 1))
    for i in range(n - 3):
        D[i, i:i+3] = [1, -2, 1]
    
    # Calcula a matriz I
    I = np.eye(n - 1)
    
    # Calcula a matriz A = (I + lambda^2 * D^T * D)
    A = I + (lambda_value**2) * np.dot(D.T, D)

    # Novos vetores de sinal e tempo
    n_signal = signal[:-1]
    
    # Calcula o sinal de baixa frequência
    low_freq_signal = np.dot(n_signal, inv(A))

    # Calcula o sinal filtrado subtraindo o sinal de baixa frequência do sinal original
    filtered_signal = n_signal - low_freq_signal

    # Duplica o ultimo elemento dos sinais
    low_freq_signal = np.append(low_freq_signal, low_freq_signal[-1])
    filtered_signal = np.append(filtered_signal, filtered_signal[-1])
    
    return filtered_signal

# Transformada de Fourier
def calculate_fft(signal, fs, padding_factor=10):
    # Calcular a FFT com padding
    fft_result = np.fft.fft(signal, n=len(signal) * padding_factor)
    spectrum = np.abs(fft_result)  # Módulo do espectro
    freqs = np.fft.fftfreq(len(fft_result), 1/fs) * 60  # Converter para BPM

    return spectrum, freqs

# Estima bpm
def find_peak_in_range(spectrum, freqs, min_freq=30, max_freq=216):
    # Encontrar os índices que correspondem à faixa de frequências desejada
    start_index = np.argmax(freqs >= min_freq)
    end_index = np.argmax(freqs >= max_freq)

    # Verificar se a faixa é válida
    if start_index >= end_index:
        return None, None

    # Encontrar o índice do maior pico dentro da faixa
    peak_index = np.argmax(spectrum[start_index:end_index]) + start_index

    # Obter a frequência e amplitude correspondentes ao maior pico
    peak_frequency = freqs[peak_index]
    peak_amplitude = spectrum[peak_index]

    return peak_frequency

# Estima irpm
def irpm():
    return 16

# Interpolação polinomial Spline Cúbica
def cubic_spline_interpolation(signal, sampling_freq, interp_freq=200):
    # Tempo original
    t_original = np.arange(len(signal)) / sampling_freq
    print(t_original)
    
    # Tempo interpolado
    t_interp = np.arange(0, t_original[-1], 1 / interp_freq)
    print(t_interp)
    
    # Interpolação cúbica spline
    cubic_spline = CubicSpline(t_original, signal)
    interpolated_signal = cubic_spline(t_interp)
    
    return interpolated_signal, t_interp

# Índice de confiança
def analyze_signal_spectrum(spectrum, freqs, file, min_bpm=30, max_bpm=200, num_peaks=20):
    # Encontrar os índices correspondentes à faixa de frequências entre min_bpm e max_bpm
    start_index = np.argmax(freqs >= min_bpm)
    end_index = np.argmax(freqs >= max_bpm)

    # Encontrar picos no espectro dentro da faixa desejada
    peaks, _ = find_peaks(spectrum[start_index:end_index])
    peaks += start_index  # Ajustar os índices dos picos para a faixa total

    # Ordenar os picos pela potência
    sorted_peaks = peaks[np.argsort(spectrum[peaks])[::-1]]

    # Selecionar os picos mais proeminentes
    if len(sorted_peaks) >= num_peaks:
        top_peaks = sorted_peaks[:num_peaks]
    else:
        top_peaks = sorted_peaks

    # Obter as frequências e amplitudes correspondentes aos picos
    peak_frequencies = freqs[top_peaks]
    peak_amplitudes = spectrum[top_peaks]

    # Escrever as frequências e amplitudes no arquivo
    for i, (frequency, amplitude) in enumerate(zip(peak_frequencies, peak_amplitudes), 1):
        #file.write(f'Heart Rate Frequency {i} in BPM: {frequency:.2f}, Amplitude: {amplitude:.2f}\n')
        pass

    return peak_frequencies, peak_amplitudes