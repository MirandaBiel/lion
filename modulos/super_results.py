from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets, QtCore
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from py_GUIs.results import Ui_Dialog

# Classe principal que expande a janela principal da aplicação
class SuperResults(QDialog):
    def __init__(self, main_window, *args, **kwargs):
        super(SuperResults, self).__init__(*args, **kwargs)

        # Guarda a referência da janela principal
        self.main_window = main_window
        
        # Inicializa a interface gerada pelo Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_main_w.clicked.connect(self.voltar)
        self.ui.pushButton_amostragem.clicked.connect(self.atualizar)
        self.ui.pushButton_grafico.clicked.connect(self.mostra_grafico)

        self.path_grafico_bvp = None
        self.path_grafico_bvp_filtrado = None
        self.path_grafico_espectro = None
        self.indice_grafico = 0
        self.path_grafico = None

    def mostra_grafico(self):
        pixmap = QtGui.QPixmap(self.path_grafico)
        # Redimensiona o pixmap para caber no label
        pixmap = pixmap.scaled(self.ui.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.ui.label.setPixmap(pixmap)

    def atualizar(self):
        self.path_grafico_bvp = self.main_window.path_grafico_bvp
        self.path_grafico_bvp_filtrado = self.main_window.path_grafico_bvp_filtrado
        self.path_grafico_espectro = self.main_window.path_grafico_espectro
        self.indice_grafico = self.ui.comboBox_grafico.currentIndex()

        if self.indice_grafico == 0:
            self.path_grafico = self.path_grafico_bvp
        elif self.indice_grafico == 1:
            self.path_grafico = self.path_grafico_bvp_filtrado
        elif self.indice_grafico == 2:
            self.path_grafico = self.path_grafico_espectro

        self.mostra_grafico()

        self.ui.lineEdit_bom.setText(str(self.main_window.bpm))
        self.ui.lineEdit_irpm.setText(str(self.main_window.irpm))
        self.ui.lineEdit_iq1.setText(str(self.main_window.iq2))
        self.ui.lineEdit_iq2.setText(str(self.main_window.iq3))
        self.ui.lineEdit_t_analise.setText(str(self.main_window.iq1))
        self.ui.lineEdit_t_afericao.setText(str(self.main_window.tempo_de_captura / 1000))
        self.ui.comboBox_metodo.setCurrentText(self.main_window.method)
            
    def voltar(self):
        self.hide()  # Oculta a janela, mantendo os dados
        self.main_window.show()  # Exibe a janela principal novamente
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    foco_window = SuperResults()
    foco_window.showMaximized()

    sys.exit(app.exec_())
