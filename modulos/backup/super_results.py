from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from py_GUIs.results import Ui_Dialog

# Classe principal que expande a janela principal da aplicação
class SuperResults(QDialog):
    def __init__(self, *args, **kwargs):
        super(SuperResults, self).__init__(*args, **kwargs)
        
        # Inicializa a interface gerada pelo Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_main_w.clicked.connect(self.voltar)
        self.ui.pushButton_amostragem.clicked.connect(self.mostra_amostragem)
        self.ui.pushButton_grafico.clicked.connect(self.mostra_grafico)

    def mostra_grafico(self):
        print("MOSTRA GRAFICO")

    def mostra_amostragem(self):
        print("MOSTRA AMOSTRAGEM")
            
    def voltar(self):
        print("VOLTA")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    foco_window = SuperResults()
    foco_window.showMaximized()

    sys.exit(app.exec_())
