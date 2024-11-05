from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from collections import deque
from py_GUIs.main_window import Ui_Dialog
from picamera2.outputs import FileOutput
from picamera2.encoders import H264Encoder
from PyQt5.QtCore import QTimer
import numpy as np
import io
import time


# Importa as classes correspondentes de cada janela da pasta 'modulos'
from modulos.super_foco import SuperFoco
from modulos.super_config import SuperConfig
from modulos.super_advanced_settings import SuperAdvancedSettings
from modulos.super_results import SuperResults

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
        self.ui.startButton.clicked.connect(self.mostra_variaveis)

        # Inicializando as janelas filhas e passando `self` como referência para `main_window`
        self.advanced_settings_window = SuperAdvancedSettings(self)
        self.config_window = SuperConfig(self)
        self.foco_window = SuperFoco(self)
        self.results_window = SuperResults(self)

        # Variáveis para captura
        self.encoder = H264Encoder()
        self.output = FileOutput("video.h264")
        self.frames = []

        # Variáveis das janelas
        self.tempo_de_captura = 5000 # em milisegundos
        self.fps = 30
        self.frame_duration = int(1000000 / self.fps)
        self.size = (800, 600)
        self.landmarks = [151, 101, 330]
        self.landmarks_gain = 1
        self.method = 'GBGR'
        self.analysis = 'espectral'

        # Timer para parar a gravação após 5 segundos
        self.record_timer = QTimer()
        self.record_timer.setInterval(self.tempo_de_captura)
        self.record_timer.setSingleShot(True)  # Para disparar apenas uma vez
        self.record_timer.timeout.connect(self.stop_capture)

        # Configurações da câmera
        self.ui.picam2.post_callback = self.post_callback
        self.cont = 0
        self.cont_enable = False

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
        video_config = self.ui.picam2.create_video_configuration(
            controls={"FrameDurationLimits": (self.frame_duration, self.frame_duration)},
            main={"size": self.size}
        )
        self.ui.picam2.configure(video_config)
        print(self.ui.picam2.camera_configuration())

    def start_capture(self):
        self.ui.picam2.start_encoder(self.encoder, self.output)
        self.record_timer.start()
        self.cont_enable = True

    def stop_capture(self):
        self.ui.picam2.stop_encoder()
        self.cont_enable = False
        print(f'Frames capturados: {self.cont}')
    
    def mostra_variaveis(self):
        print("Landmarks")
        print(self.landmarks)
        #print("Frame Duration")
        #print(self.frame_duration)
        #print("size")
        #print(self.size)
        print('landmarks gain')
        print(self.landmarks_gain)
        print('metodo')
        print(self.method)
        print('analysis')
        print(self.analysis)
        print('fps')
        print(self.fps)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    main_window = SuperMainWindow()
    main_window.show()

    sys.exit(app.exec_())