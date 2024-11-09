from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from libcamera import controls
from py_GUIs.foco import Ui_Dialog

# Classe principal que expande a janela principal da aplicação
class SuperFoco(QDialog):
    def __init__(self, main_window, *args, **kwargs):
        super(SuperFoco, self).__init__(*args, **kwargs)

        # Guarda a referência da janela principal
        self.main_window = main_window
        
        # Inicializa a interface gerada pelo Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_main_w.clicked.connect(self.voltar)
        
    def voltar(self):
        mode = self.ui.comboBox_af_mode.currentText()
        if mode == 'Manual':
            AfMode = controls.AfModeEnum.Manual
        if mode == 'Auto':
            AfMode = controls.AfModeEnum.Auto
        if mode == 'Continuous':
            AfMode = controls.AfModeEnum.Continuous    
        self.main_window.ui.picam2.set_controls({"AfMode": AfMode})
        self.hide()  # Oculta a janela, mantendo os dados
        self.main_window.show()  # Exibe a janela principal novamente
        
    def trigger(self):
        mode = self.ui.comboBox_af_mode.currentText()
        if mode == 'Auto':
            self.main_window.ui.picam2.autofocus_cycle(wait=False)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    foco_window = SuperFoco()
    foco_window.showMaximized()

    sys.exit(app.exec_())
