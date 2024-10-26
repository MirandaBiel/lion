from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from py_GUIs.main_window import Ui_MainWindow

# Classe principal que expande a janela principal da aplicação
class SuperMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SuperMainWindow, self).__init__(*args, **kwargs)
        
        # Inicializa a interface gerada pelo Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

    def setup_camera(self):
        # Exemplo de como inicializar a câmera (descomente se usar Picamera2)
        # self.ui.picam2 = Picamera2()
        # self.ui.qpicamera2 = QGlPicamera2(self.ui.picam2, width=800, height=600, keep_ar=False)
        # self.ui.gridPreview.addWidget(self.ui.qpicamera2, 0, 0, 1, 1)
        pass

    def start_camera(self):
        # Método para iniciar a câmera
        if self.ui.picam2 is not None:
            self.ui.picam2.start()

    def stop_camera(self):
        # Método para parar a câmera
        if self.ui.picam2 is not None:
            self.ui.picam2.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    main_window = SuperMainWindow()
    main_window.show()

    sys.exit(app.exec_())
