import matplotlib.pyplot as plt
import mediapipe as mp
import numpy as np
import math
import cv2

# Parâmetros
patches = [151, 101, 330]  # Regiões de interesse
face_mesh = mp.solutions.face_mesh.FaceMesh(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5, 
    max_num_faces=1
)
fs = 30  # Frequência de amostragem (Hz)
num_estimators = 1
rppg_channels = []

def processa_um_frame(frame):
    """Processa um único frame para extrair as médias RGB dos patches de interesse."""
    results = face_mesh.process(frame)
    mean_red, mean_green, mean_blue = 0, 0, 0
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
                mean_red += np.mean(crop_patch[:, :, 0])  # Canal Vermelho
                mean_green += np.mean(crop_patch[:, :, 1])  # Canal Verde
                mean_blue += np.mean(crop_patch[:, :, 2])  # Canal Azul
    
    # Retorna a média dos valores RGB para o frame
    return [mean_red / len(patches), mean_green / len(patches), mean_blue / len(patches)]

def plot_rppg_signal(rppg_data, fs):
    """Plota o sinal RPPG extraído ao longo do tempo."""
    num_frames = rppg_data.shape[2]
    time = np.linspace(0, num_frames / fs, num_frames)
    
    plt.figure(figsize=(10, 6))
    plt.plot(time, rppg_data[0, 0, :], label='Red Channel', color='red')
    plt.plot(time, rppg_data[0, 1, :], label='Green Channel', color='green')
    plt.plot(time, rppg_data[0, 2, :], label='Blue Channel', color='blue')
    
    plt.xlabel("Time (s)")
    plt.ylabel("Intensity")
    plt.title("RPPG Signal Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

# Caminho do vídeo
caminho_video = 'video_face_1.h264'  # Substitua pelo caminho do seu vídeo H.264

# Abre o vídeo
captura = cv2.VideoCapture(caminho_video)

# Verifica se o vídeo foi aberto corretamente
if not captura.isOpened():
    print("Erro ao abrir o vídeo.")
else:
    while True:
        ret, frame = captura.read()
        if not ret:
            print("Fim do vídeo ou erro ao ler frame.")
            break
        
        # Processa o frame e armazena o resultado
        rgb_values = processa_um_frame(frame)
        rppg_channels.append(rgb_values)
        
        # Exibe o frame
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Libera o objeto de captura e fecha a janela
captura.release()
cv2.destroyAllWindows()

# Converte a lista para um ndarray com shape [1, 3, num_frames]
rppg_channels = np.array(rppg_channels, dtype=np.float32).transpose(1, 0)
rppg_channels = np.expand_dims(rppg_channels, axis=0)

# Mostra o gráfico das capturas no tempo
plot_rppg_signal(rppg_channels, fs)
