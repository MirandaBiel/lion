import sys
from PyQt5.QtWidgets import QApplication
from modulos.super_main_window_label import SuperMainWindow

# Cria a aplicação
app = QApplication(sys.argv)

# Instancia a janela principal da aplicação
window = SuperMainWindow()

# Exibe a janela
window.showMaximized()

# Executa o loop da aplicação
sys.exit(app.exec_())