from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from py_GUIs.advanced_settings import Ui_Dialog

# Classe principal que expande a janela principal da aplicação
class SuperAdvancedSettings(QDialog):
    def __init__(self, main_window, *args, **kwargs):
        super(SuperAdvancedSettings, self).__init__(*args, **kwargs)

        # Guarda a referência da janela principal
        self.main_window = main_window
        
        # Inicializa a interface gerada pelo Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conecta as entradas com as funções
        self.ui.pushButton_main_w.clicked.connect(self.voltar)

        # Controles da janela
        self.Saturation = 1 
        self.Contrast = 1
        self.Sharpness = 1
        self.Brightness = 0
        self.AwbEnable = 1 #None
        self.AwbMode = 0
        self.AeEnable = 1 #None
        self.AeConstraintMode = 0
        self.AeExposureMode = 0
        self.AeFlickerMode = 0
        self.AeFlickerPeriod = 8333
        self.AeMeteringMode = 0
        self.HdrMode = 0
        self.HdrChannel = None # Não há essa funcionalidade na câmera
        self.NoiseReductionMode = 0

    # exemplo de configuração (controles é um dicionário)    
    '''
    config = picam2.create_video_configuration(main={"format": 'RGB888', "size": Size[i]},
                                                   buffer_count=15,
                                                   queue=True,
                                                   display=None,
                                                   encode=None,
                                                   controls={"FrameDurationLimits": (33333, 33333),
                                                             "AwbEnable": AwbEnable[i],
                                                             "AeFlickerMode": AeFlickerMode[i],
                                                             "NoiseReductionMode": NoiseReductionMode[i],
                                                             "AeEnable": AeEnable[i]})	
    
    '''
    
    def voltar(self):
        self.update_controls()
        self.hide()  # Oculta a janela, mantendo os dados
        self.main_window.show()  # Exibe a janela principal novamente

    def dict_controls(self): # modificar para ser um dicionario geral para os controles
        return {
            "Saturation": self.Saturation,
            "Contrast": self.Contrast,
            "Sharpness": self.Sharpness,
            "Brightness": self.Brightness,
            "AwbEnable": self.AwbEnable,
            "AwbMode": self.AwbMode,
            "AeEnable": self.AeEnable,
            "AeConstraintMode": self.AeConstraintMode,
            "AeExposureMode": self.AeExposureMode,
            "AeFlickerPeriod": self.AeFlickerPeriod,
            "AeMeteringMode": self.AeMeteringMode,
            "HdrMode": self.HdrMode,
            "NoiseReductionMode": self.NoiseReductionMode
        }

    def update_controls(self):
        # Atualiza os valores
        self.Saturation = self.ui.horizontalSlider_sat.value() / 10
        self.Contrast = self.ui.horizontalSlider_contr.value() / 10
        self.Sharpness = self.ui.horizontalSlider_aguca.value() / 10
        self.Brightness = self.ui.horizontalSlider_brilho.value() / 10
        self.AwbEnable = self.ui.checkBox_AWB.isChecked()
        self.AwbMode = self.ui.comboBox_AWB_mode.currentIndex()
        self.AeEnable = self.ui.checkBox_AE.isChecked()
        self.AeConstraintMode = self.ui.comboBox_Ae_constraint.currentIndex()
        self.AeExposureMode = self.ui.comboBox_AE_exposure.currentIndex()
        self.AeFlickerMode = self.ui.comboBox_AE_Fliker_mode.currentIndex()
        self.AeFlickerPeriod = self.ui.spinBox_AE_fliker_period.value()
        self.AeMeteringMode = self.ui.comboBox_AE_metering.currentIndex()
        self.HdrMode = self.ui.comboBox_HDR_MODE.currentIndex()
        self.NoiseReductionMode = self.ui.comboBox_Noise_redu_mode.currentIndex()

        # Atualiza os controles
        self.main_window.ui.picam2.set_controls(self.dict_controls())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    foco_window = SuperAdvancedSettings()
    foco_window.showMaximized()

    sys.exit(app.exec_())
