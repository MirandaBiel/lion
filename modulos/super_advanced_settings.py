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
        self.ui.horizontalSlider_aguca.valueChanged.connect(self.sliders_update)
        self.ui.horizontalSlider_brilho.valueChanged.connect(self.sliders_update)
        self.ui.horizontalSlider_contr.valueChanged.connect(self.sliders_update)
        self.ui.horizontalSlider_sat.valueChanged.connect(self.sliders_update)
        
    def voltar(self):
        self.hide()  # Oculta a janela, mantendo os dados
        self.main_window.show()  # Exibe a janela principal novamente

    def img_dict(self):
        return {
            "Saturation": int(self.ui.horizontalSlider_sat.value() / 10),
            "Contrast": int(self.ui.horizontalSlider_contr.value() / 10),
            "Sharpness": int(self.ui.horizontalSlider_aguca.value() / 10),
            "Brightness": int(self.ui.horizontalSlider_brilho.value() / 10),
        }

    def sliders_update(self):
        self.main_window.ui.picam2.set_controls(self.img_dict)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    foco_window = AdvancedSettings()
    foco_window.showMaximized()

    sys.exit(app.exec_())
