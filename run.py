import sys
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from modulos.main_window import preview_main_window 

app = QApplication(sys.argv)
window = preview_main_window()
window.show()
sys.exit(app.exec_())