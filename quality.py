import matplotlib.pyplot as plt
import mediapipe as mp
import numpy as np
import math
import cv2
import rPPG_Methods as rppg
import signal_quality as sqi

# Parâmetros
patches = [151, 101, 330]  # Regiões de interesse (números de landmarks)
face_mesh = mp.solutions.face_mesh.FaceMesh(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5, 
    max_num_faces=1
)
fs = 30  # Frequência de amostragem (Hz)

# Função para plotar os sinais BVP extraídos
def plot_bvp_signals_separately(bvp_signals, labels, fs):
    """
    Plota os sinais BVP em janelas separadas para cada método.
    
    Parâmetros:
    - bvp_signals: lista de arrays numpy, cada um com formato [n_patches, num_frames]
    - labels: lista de strings com os nomes dos métodos
    - fs: frequência de amostragem (Hz)
    """
    for bvp, label in zip(bvp_signals, labels):
        n_patches, num_frames = bvp.shape
        time = np.linspace(0, num_frames / fs, num_frames)

        for patch_idx in range(n_patches):
            plt.figure(figsize=(10, 6))
            plt.plot(time, bvp[patch_idx, :], label=f'Patch {patch_idx+1}')
            plt.title(f'Sinal BVP - Método: {label} (Patch {patch_idx+1})')
            plt.xlabel('Tempo (s)')
            plt.ylabel('Amplitude')
            plt.legend()
            plt.grid(True)
            plt.show()

def processa_um_frame(frame):
    """Processa um único frame para extrair as médias RGB dos patches de interesse."""
    results = face_mesh.process(frame)
    patch_colors = []
    
    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        
        # Converte coordenadas normalizadas para pixels
        landmarks_points = [
            (int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]))
            for landmark in face_landmarks.landmark
        ]
        
        # Calcula o tamanho do patch
        l = int((math.sqrt((landmarks_points[337][0] - landmarks_points[108][0])**2 +
                           (landmarks_points[337][1] - landmarks_points[108][1])**2)) / 5)
        
        # Extrai os patches para análise
        for patch in patches:
            y_min = max(0, landmarks_points[patch][1] - l)
            y_max = min(frame.shape[0], landmarks_points[patch][1] + l)
            x_min = max(0, landmarks_points[patch][0] - l)
            x_max = min(frame.shape[1], landmarks_points[patch][0] + l)
            
            if y_max > y_min and x_max > x_min:
                crop_patch = frame[y_min:y_max, x_min:x_max]
                mean_red = np.mean(crop_patch[:, :, 0])  # Canal Vermelho
                mean_green = np.mean(crop_patch[:, :, 1])  # Canal Verde
                mean_blue = np.mean(crop_patch[:, :, 2])  # Canal Azul
                patch_colors.append([mean_red, mean_green, mean_blue])
    
    # Se não foram encontrados rostos, retorna zeros
    if not patch_colors:
        patch_colors = [[0, 0, 0] for _ in patches]
    
    return np.array(patch_colors)  # Retorna um array [num_patches, 3]

def processa_um_frame_ssr(frame, patch_id=151, target_size=(32, 32)):
    """
    Processa um único frame para extrair a região de interesse (patch 151) em formato adequado para a função SSR.
    Sempre retorna um ndarray com shape [target_size[0], target_size[1], 3].
    """
    # Processa o frame para obter landmarks
    results = face_mesh.process(frame)
    
    # Inicializa o patch com zeros caso não seja detectado rosto
    patch_crop = np.zeros((target_size[0], target_size[1], 3), dtype=np.float32)
    
    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        
        # Converte coordenadas normalizadas para pixels
        landmarks_points = [
            (int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0]))
            for landmark in face_landmarks.landmark
        ]
        
        # Calcula o tamanho do patch (usando distância entre landmarks como referência)
        l = int((math.sqrt((landmarks_points[337][0] - landmarks_points[108][0]) ** 2 +
                           (landmarks_points[337][1] - landmarks_points[108][1]) ** 2)) / 5)
        
        # Extrai o patch 151 para análise
        y_min = max(0, landmarks_points[patch_id][1] - l)
        y_max = min(frame.shape[0], landmarks_points[patch_id][1] + l)
        x_min = max(0, landmarks_points[patch_id][0] - l)
        x_max = min(frame.shape[1], landmarks_points[patch_id][0] + l)
        
        if y_max > y_min and x_max > x_min:
            patch_crop_raw = frame[y_min:y_max, x_min:x_max]
            
            # Redimensiona para o tamanho fixo `target_size` (independente do tamanho original)
            patch_crop = cv2.resize(patch_crop_raw, target_size, interpolation=cv2.INTER_AREA)
    
    return patch_crop.astype(np.float32)  # Retorna um array [32, 32, 3]

def plot_rppg_signal(rppg_data, fs):
    """
    Plota o sinal RPPG extraído ao longo do tempo para cada patch e cada canal (R, G, B).
    
    Parâmetros:
    - rppg_data: numpy array com formato [n_patches, 3, n_frames]
    - fs: frequência de amostragem (Hz)
    """
    n_patches, _, num_frames = rppg_data.shape
    time = np.linspace(0, num_frames / fs, num_frames)
    
    for patch_idx in range(n_patches):
        plt.figure(figsize=(10, 6))
        plt.plot(time, rppg_data[patch_idx, 0, :], label=f'Red Channel (Patch {patch_idx+1})', color='red')
        plt.plot(time, rppg_data[patch_idx, 1, :], label=f'Green Channel (Patch {patch_idx+1})', color='green')
        plt.plot(time, rppg_data[patch_idx, 2, :], label=f'Blue Channel (Patch {patch_idx+1})', color='blue')
        
        plt.title(f"RPPG Signal Over Time - Patch {patch_idx+1}")
        plt.xlabel("Time (s)")
        plt.ylabel("Intensity")
        plt.legend()
        plt.grid(True)
        plt.show()

def plot_bvp_signal_1d(bvp_signal, label, fs):
    """
    Plota um sinal BVP unidimensional ao longo do tempo.

    Parâmetros:
    - bvp_signal: array 1D com o sinal BVP [num_frames]
    - label: string com o nome do método
    - fs: frequência de amostragem (Hz)
    """
    num_frames = len(bvp_signal)
    time = np.linspace(0, num_frames / fs, num_frames)

    plt.figure(figsize=(10, 6))
    plt.plot(time, bvp_signal, label=f'Método: {label}')
    plt.title(f'Sinal BVP - Método: {label}')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

# Caminho do vídeo
caminho_video = 'video_face_1.h264'

# Lista para armazenar os valores RGB
rppg_channels = []
rppg_channels_ssr = []

# Abre o vídeo
captura = cv2.VideoCapture(caminho_video)

if not captura.isOpened():
    print("Erro ao abrir o vídeo.")
else:
    while True:
        ret, frame = captura.read()
        if not ret:
            print("Fim do vídeo ou erro ao ler frame.")
            break
        
        # Processa o frame e armazena o resultado
        rgb_values = processa_um_frame(frame)  # Agora retorna [num_patches, 3]
        rppg_channels.append(rgb_values)

        # Processa o frame e extrai o patch 151 com tamanho fixo
        patch_crop = processa_um_frame_ssr(frame, target_size=(32, 32))
        rppg_channels_ssr.append(patch_crop)
        
        # Exibe o frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Libera o objeto de captura e fecha a janela
captura.release()
cv2.destroyAllWindows()

# Converte a lista para um ndarray com shape [num_patches, 3, num_frames]
rppg_channels = np.array(rppg_channels, dtype=np.float32)
rppg_channels = rppg_channels.transpose(1, 2, 0)

# Converte a lista para um ndarray com o formato necessário [num_frames, rows, columns, rgb_channels]
rppg_channels_ssr = np.array(rppg_channels_ssr, dtype=np.float32)

# Mostra o gráfico das capturas no tempo
plot_rppg_signal(rppg_channels, fs)

# Aplicar métodos rPPG e converter para listas
bvp_chrom = np.mean(rppg.CHROM(rppg_channels), axis=0).tolist()
bvp_green = np.mean(rppg.GREEN(rppg_channels), axis=0).tolist()
bvp_lgi = np.mean(rppg.LGI(rppg_channels), axis=0).tolist()
bvp_pos = np.mean(rppg.POS(rppg_channels, fps=fs), axis=0).tolist()
bvp_gbgr = np.mean(rppg.GBGR(rppg_channels), axis=0).tolist()
bvp_ica = np.mean(rppg.ICA(rppg_channels, component='second_comp'), axis=0).tolist()
bvp_omit = np.mean(rppg.OMIT(rppg_channels), axis=0).tolist()
bvp_pbv = np.mean(rppg.PBV(rppg_channels), axis=0).tolist()
bvp_pca = np.mean(rppg.PCA(rppg_channels, component='second_comp'), axis=0).tolist()
bvp_ssr = np.mean(rppg.SSR(rppg_channels_ssr, fps=fs), axis=0).tolist()

plot_bvp_signal_1d(bvp_chrom, "CHROM", fs)
plot_bvp_signal_1d(bvp_green, "GREEN", fs)
plot_bvp_signal_1d(bvp_lgi, "LGI", fs)
plot_bvp_signal_1d(bvp_pos, "POS", fs)
plot_bvp_signal_1d(bvp_gbgr, "GBGR", fs)
plot_bvp_signal_1d(bvp_ica, "ICA", fs)
plot_bvp_signal_1d(bvp_omit, "OMIT", fs)
plot_bvp_signal_1d(bvp_pbv, "PBV", fs)
plot_bvp_signal_1d(bvp_pca, "PCA", fs)
plot_bvp_signal_1d(bvp_ssr, "SSR", fs)

signal = bvp_green

sqi_Perfusion = sqi.Perfusion(signal)
sqi_Skewness = sqi.Skewness(signal)
sqi_Kurtosis = sqi.Kurtosis(signal)
#sqi_Entropy = sqi.Entropy(signal)
sqi_Zero_Crossing_rate = sqi.Zero_Crossing_rate(signal)
#sqi_SNR = sqi.SNR(signal)

print(sqi_Perfusion)
print(sqi_Skewness)
print(sqi_Kurtosis)
#print(sqi_Entropy)
print(sqi_Zero_Crossing_rate)
#print(sqi_SNR)