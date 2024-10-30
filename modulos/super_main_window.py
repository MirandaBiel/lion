from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from collections import deque
from py_GUIs.main_window import Ui_Dialog


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
        self.ui.startButton.clicked.connect(self.caputre)

        # Inicializando as janelas filhas e passando `self` como referência para `main_window`
        self.advanced_settings_window = SuperAdvancedSettings(self)
        self.config_window = SuperConfig(self)
        self.foco_window = SuperFoco(self)
        self.results_window = SuperResults(self)
        
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

    def caputre(self):
        # Parametros da captura
        fs = 30  # Taxa de quadros em Hz
        ts = 5   # Duracao da captura em segundos
        n_frames = fs * ts + 10  # NÃºmero total de quadros a capturar

        # Cria a fila com tamanho mÃ¡ximo
        queue = deque(maxlen=n_frames)
        tempos_de_captura = []

        # Captura e armazena os quadros na fila
        for i in range(n_frames):
            [main], metadata = self.ui.picam2.capture_arrays()
            tempos_de_captura.append(metadata["SensorTimestamp"])
            queue.append(main)  # Adiciona o quadro Ã  fila

            # Calcula e atualiza a porcentagem na progressBar_2
            progress_percent = int((i + 1) / n_frames * 100)
            self.ui.progressBar_2.setValue(progress_percent)

        # Calcula os intervalos entre os tempos de captura
        intervalos = [(((tempos_de_captura[i+1] - tempos_de_captura[i]) * 0.000001) - 33.333)
                    for i in range(len(tempos_de_captura) - 1)]
        print("Intervalos entre capturas:", intervalos)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    main_window = SuperMainWindow()
    main_window.show()

    sys.exit(app.exec_())
