from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
#from picamera2 import Picamera2
#from picamera2.previews.qt import QGlPicamera2
import os, sys
 
from py_GUIs.main_window import Ui_MainWindow

class super_main_window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(super_main_window, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
