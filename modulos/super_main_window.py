from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
import sys
from collections import deque
from py_GUIs.main_window import Ui_Dialog
from picamera2.outputs import FileOutput
from picamera2.encoders import H264Encoder
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
        self.ui.startButton.clicked.connect(self.start_caputre)
        self.ui.qpicamera2.done_signal.connect(self.stop_capture)


        # Inicializando as janelas filhas e passando `self` como referência para `main_window`
        self.advanced_settings_window = SuperAdvancedSettings(self)
        self.config_window = SuperConfig(self)
        self.foco_window = SuperFoco(self)
        self.results_window = SuperResults(self)

        # Variáveis para captura
        self.frames = []
        self.encoder = H264Encoder(10000000)
        self.buffer = io.BytesIO()
        self.output = FileOutput("test.h264")
        self.cont = 0
        self.cont_enable = False

        # Configurações da câmera
        self.ui.picam2.post_callback = self.post_callback

    def post_callback(self, request):
        if self.cont_enable:
            if self.cont == 150:
                self.cont_enable = False
                request.get_metadata()
                print('CODIFICADOR PARADO')
            self.cont = self.cont + 1
            print(self.cont)

    def start_camera(self):
        # Método para iniciar a câmera
        if self.ui.picam2 is not None:
            self.config_camera()
            self.ui.picam2.start()

    def stop_camera(self):
        # Método para parar a câmera
        if self.ui.picam2 is not None:
            self.ui.picam2.stop()

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

    def config_camera(self):
        video_config = self.ui.picam2.create_video_configuration(
            controls={"FrameDurationLimits": (33333, 33333)},  # Limita para 30 fps
            main={"size": (800, 600)}
        )
        self.ui.picam2.configure(video_config)
        print(self.ui.picam2.camera_configuration())

    def start_caputre(self):
        self.cont_enable = True
        self.ui.picam2.start_encoder(self.encoder, self.output)
    
    def stop_capture(self, job):
        self.ui.picam2.stop_encoder()


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    main_window = SuperMainWindow()
    main_window.show()

    sys.exit(app.exec_())
