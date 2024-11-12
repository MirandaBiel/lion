# Importações da GUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
from py_GUIs.main_window import Ui_Dialog
from PyQt5.QtCore import QTimer

# Importações da picamera
from picamera2.outputs import FileOutput
from picamera2.encoders import H264Encoder

# Importações utilitárias
import matplotlib
matplotlib.use('Agg')  # Define o backend para não-interativo
import matplotlib.pyplot as plt
import mediapipe as mp
import math
import cv2
import rPPG_Methods as rppg
import sys
from collections import deque
import numpy as np
import io
import time
import os

# Importações as classes correspondentes de cada janela da pasta 'modulos'
from modulos.super_foco import SuperFoco
from modulos.super_config import SuperConfig
from modulos.super_advanced_settings import SuperAdvancedSettings
from modulos.super_results import SuperResults

# Inicialisa o face_mesh do mediapipe
face_mesh = mp.solutions.face_mesh.FaceMesh(
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5, 
    max_num_faces=1
)

# Funções de plotagem e análise do sinal
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

def processa_um_frame(frame, patches):
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

def plot_rppg_signal(rppg_data, fs, output_dir='plots'):
    """
    Plota e salva o sinal RPPG extraído ao longo do tempo para cada patch e cada canal (R, G, B).
    
    Parâmetros:
    - rppg_data: numpy array com formato [n_patches, 3, n_frames]
    - fs: frequência de amostragem (Hz)
    - output_dir: diretório onde os gráficos serão salvos (default: 'plots')
    """
    n_patches, _, num_frames = rppg_data.shape
    time = np.linspace(0, num_frames / fs, num_frames)
    
    # Cria o diretório se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
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
        
        # Salva o gráfico em vez de exibir
        output_path = os.path.join(output_dir, f'rppg_signal_patch_{patch_idx+1}.png')
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()  # Fecha a figura para liberar memória
        print(f"Gráfico salvo em: {output_path}")

# Classe principal que expande a janela principal da aplicação
class SuperMainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(SuperMainWindow, self).__init__(*args, **kwargs)
        
        # Inicializa a interface gerada pelo Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_config.clicked.connect(self.open_config_window)
        self.ui.pushButton_config_avanca.clicked.connect(self.open_advanced_settings_window)
        self.ui.pushButton_foco.clicked.connect(self.open_foco_window)
        self.ui.pushButton_resultados.clicked.connect(self.open_results_window)
        self.ui.startButton.clicked.connect(self.start_capture)

        # Inicializando as janelas filhas e passando `self` como referência para `main_window`
        self.advanced_settings_window = SuperAdvancedSettings(self)
        self.config_window = SuperConfig(self)
        self.foco_window = SuperFoco(self)
        self.results_window = SuperResults(self)

        # Variáveis para captura
        self.n_video = 5
        self.encoder = H264Encoder()
        self.video_path = f'video_face_{self.n_video}.h264'
        self.output = FileOutput(self.video_path)
        self.frames = []

        # Variáveis das janelas
        self.tempo_de_captura = 30000 # em milisegundos
        self.fps = 30
        self.frame_duration = int(1000000 / self.fps)
        self.size = (800, 600)
        self.landmarks = [151, 101, 330]
        self.landmarks_gain = 1
        self.method = 'GBGR'
        self.analysis = 'espectral'

        # Timer para parar a gravação
        self.record_timer = QTimer()
        self.record_timer.timeout.connect(self.update_progress)
        self.elapsed_time = 0

        # Configurações da câmera
        self.ui.picam2.post_callback = self.post_callback
        self.cont = 0
        self.frames_capturados = 0
        self.frames_gravados = 0
        self.cont_enable = False
        self.config = self.ui.picam2.create_video_configuration(
            controls={"FrameDurationLimits": (self.frame_duration, self.frame_duration)},
            main={"size": self.size}
        )

        # Variáveis para análise
        self.rppg_channels = []
        self.rppg_channels_ssr = []
        self.np_rppg_channels = None
        self.np_rppg_channels_ssr = None

    def extract_raw_signal(self):
        # Zera as listas dos sinais
        self.rppg_channels = []
        self.rppg_channels_ssr = []

        self.ui.label_comunicacao_2.setText('Realizando processamento...')
        progress_value = 0
        self.ui.progressBar_2.setValue(progress_value)
        n_frames = self.frames_capturados
        processed_frames = 0

        captura = cv2.VideoCapture(self.video_path)
        if not captura.isOpened():
            print("Erro ao abrir o vídeo.")
        else:
            while True:
                ret, frame = captura.read()
                if not ret:
                    print("Fim do vídeo ou erro ao ler frame.")
                    break
                
                # Processa o frame e armazena o resultado
                rgb_values = processa_um_frame(frame, self.landmarks)  # Agora retorna [num_patches, 3]
                self.rppg_channels.append(rgb_values)

                # Processa o frame e extrai o patch 151 com tamanho fixo
                patch_crop = processa_um_frame_ssr(frame, target_size=(32, 32))
                self.rppg_channels_ssr.append(patch_crop)
                
                processed_frames = processed_frames + 1
                progress_value = int((processed_frames / n_frames) * 100)
                self.ui.progressBar_2.setValue(progress_value)

            self.ui.progressBar_2.setValue(100)
            self.ui.label_comunicacao_2.setText('Análise concluida...')
            print(f'Frames processados: {processed_frames}')

        # Converte a lista para um ndarray com shape [num_patches, 3, num_frames]
        self.rppg_channels = np.array(self.rppg_channels, dtype=np.float32)
        self.rppg_channels = self.rppg_channels.transpose(1, 2, 0)

        # Converte a lista para um ndarray com o formato necessário [num_frames, rows, columns, rgb_channels]
        self.rppg_channels_ssr = np.array(self.rppg_channels_ssr, dtype=np.float32)

        # Mostra o gráfico da captura no tempo
        plot_rppg_signal(self.rppg_channels, self.fps)

    def post_callback(self, request):
        if self.cont_enable:
            self.cont = self.cont + 1

    # Métodos para abrir cada janela
    def open_foco_window(self):
        self.hide()
        self.foco_window.showMaximized()

    def open_config_window(self):
        self.hide()
        self.config_window.showMaximized()

    def open_advanced_settings_window(self):
        self.hide()
        self.advanced_settings_window.showMaximized()

    def open_results_window(self):
        self.hide()
        self.results_window.showMaximized()
    
    # Métodos de funcionalidades
    def start_camera(self):
        # Método para iniciar a câmera
        if self.ui.picam2 is not None:
            self.config_camera()
            self.ui.picam2.start()

    def stop_camera(self):
        # Método para parar a câmera
        if self.ui.picam2 is not None:
            self.ui.picam2.stop()

    def config_camera(self):
        self.ui.picam2.configure(self.config)
        print(self.ui.picam2.camera_configuration())

    def start_capture(self):
        self.tempo_de_captura = (self.ui.spinBox_tempo_2.value() * 1000)
        self.timer_interval = int(self.tempo_de_captura / 10)
        self.record_timer.setInterval(self.timer_interval)
        self.ui.picam2.start_encoder(self.encoder, self.output)
        self.record_timer.start()
        self.cont_enable = True
        self.ui.label_comunicacao_2.setText('Realizando captura...')

    def stop_capture(self):
        self.ui.picam2.stop_encoder()
        self.cont_enable = False
        self.frames_capturados = self.cont
        self.cont = 0
        print(f'Frames capturados: {self.frames_capturados}')

        # Realiza a extração do sinal
        self.extract_raw_signal()

    def update_progress(self):
        # Atualiza o tempo decorrido e a barra de progresso
        self.elapsed_time += self.timer_interval
        if self.elapsed_time >= self.tempo_de_captura:
            self.stop_capture()
            self.elapsed_time = 0
            progress_value = 100
            self.record_timer.stop()
        else:
            progress_value = int((self.elapsed_time / self.tempo_de_captura) * 100)

        self.ui.progressBar_2.setValue(progress_value)
    
    def mostra_variaveis(self):
        print(self.ui.picam2.camera_configuration())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    main_window = SuperMainWindow()
    main_window.show()

    sys.exit(app.exec_())