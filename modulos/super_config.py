from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtGui, QtWidgets
# from picamera2 import Picamera2
# from picamera2.previews.qt import QGlPicamera2
import sys
from py_GUIs.config import Ui_Dialog

# Classe principal que expande a janela principal da aplicação
class SuperConfig(QDialog):
    def __init__(self, main_window, *args, **kwargs):
        super(SuperConfig, self).__init__(*args, **kwargs)

        # Guarda a referência da janela principal
        self.main_window = main_window
        
        # Inicializa a interface gerada pelo Qt Designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_main_w.clicked.connect(self.voltar)

        # Define os checkboxes selecionados inicialmente
        self.ui.checkBox_151.setChecked(True)
        self.ui.checkBox_101.setChecked(True)
        self.ui.checkBox_330.setChecked(True)

        self.ui.checkBox_10.setChecked(True)
        self.ui.checkBox_104.setChecked(True)
        self.ui.checkBox_107.setChecked(True)
        self.ui.checkBox_108.setChecked(True)
        self.ui.checkBox_109.setChecked(True)
        self.ui.checkBox_135.setChecked(True)
        self.ui.checkBox_18.setChecked(True)
        self.ui.checkBox_188.setChecked(True)
        self.ui.checkBox_199.setChecked(True)
        self.ui.checkBox_266.setChecked(True)
        self.ui.checkBox_280.setChecked(True)
        self.ui.checkBox_299.setChecked(True)
        self.ui.checkBox_333.setChecked(True)
        self.ui.checkBox_336.setChecked(True)
        self.ui.checkBox_337.setChecked(True)
        self.ui.checkBox_338.setChecked(True)
        self.ui.checkBox_347.setChecked(True)
        self.ui.checkBox_36.setChecked(True)
        self.ui.checkBox_364.setChecked(True)
        self.ui.checkBox_4.setChecked(True)
        self.ui.checkBox_50.setChecked(True)
        self.ui.checkBox_6.setChecked(True)
        self.ui.checkBox_69.setChecked(True)
        self.ui.checkBox_9.setChecked(True)
        self.ui.comboBox_metodo.setCurrentIndex(9)

        self.ui.comboBox_metodo
        self.ui.radioButton_espectro
        self.ui.radioButton_picos
        self.ui.spinBox_fs
        
    def voltar(self):
        if self.ui.radioButton_espectro.isChecked():
            self.main_window.analysis = 'mediana'
        else:
            self.main_window.analysis = 'media'
        self.main_window.fps = self.ui.spinBox_fs.value()
        self.main_window.frame_duration = int(1000000 / self.main_window.fps)
        self.main_window.method = self.ui.comboBox_metodo.currentText()
        self.main_window.ui.picam2.set_controls(controls={"FrameDurationLimits": (self.main_window.frame_duration, self.main_window.frame_duration)})
        self.main_window.landmarks_gain = self.ui.horizontalSlider_patches_size.value() / 10
        self.main_window.landmarks = []
        if self.ui.checkBox_10.isChecked():
            self.main_window.landmarks.append(10)
        if self.ui.checkBox_101.isChecked():
            self.main_window.landmarks.append(101)
        if self.ui.checkBox_104.isChecked():
            self.main_window.landmarks.append(104)
        if self.ui.checkBox_107.isChecked():
            self.main_window.landmarks.append(107)
        if self.ui.checkBox_108.isChecked():
            self.main_window.landmarks.append(108)
        if self.ui.checkBox_109.isChecked():
            self.main_window.landmarks.append(109)
        if self.ui.checkBox_135.isChecked():
            self.main_window.landmarks.append(135)
        if self.ui.checkBox_151.isChecked():
            self.main_window.landmarks.append(151)
        if self.ui.checkBox_18.isChecked():
            self.main_window.landmarks.append(18)
        if self.ui.checkBox_188.isChecked():
            self.main_window.landmarks.append(188)
        if self.ui.checkBox_199.isChecked():
            self.main_window.landmarks.append(199)
        if self.ui.checkBox_266.isChecked():
            self.main_window.landmarks.append(266)
        if self.ui.checkBox_280.isChecked():
            self.main_window.landmarks.append(280)
        if self.ui.checkBox_299.isChecked():
            self.main_window.landmarks.append(299)
        if self.ui.checkBox_330.isChecked():
            self.main_window.landmarks.append(330)
        if self.ui.checkBox_333.isChecked():
            self.main_window.landmarks.append(333)
        if self.ui.checkBox_36.isChecked():
            self.main_window.landmarks.append(36)
        if self.ui.checkBox_364.isChecked():
            self.main_window.landmarks.append(364)
        if self.ui.checkBox_336.isChecked():
            self.main_window.landmarks.append(336)
        if self.ui.checkBox_337.isChecked():
            self.main_window.landmarks.append(337)
        if self.ui.checkBox_9.isChecked():
            self.main_window.landmarks.append(9)
        if self.ui.checkBox_6.isChecked():
            self.main_window.landmarks.append(6)
        if self.ui.checkBox_338.isChecked():
            self.main_window.landmarks.append(338)
        if self.ui.checkBox_347.isChecked():
            self.main_window.landmarks.append(347)
        if self.ui.checkBox_69.isChecked():
            self.main_window.landmarks.append(69)
        if self.ui.checkBox_4.isChecked():
            self.main_window.landmarks.append(4)
        if self.ui.checkBox_50.isChecked():
            self.main_window.landmarks.append(50)

        self.hide()  # Oculta a janela, mantendo os dados
        self.main_window.show()  # Exibe a janela principal novamente


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria uma instância da janela principal
    foco_window = SuperConfig()
    foco_window.showMaximized()

    sys.exit(app.exec_())
