import sys
from PyQt5.QtWidgets import QApplication
from modulos.super_foco import SuperFoco

# Cria a aplicação
app = QApplication(sys.argv)

# Instancia a janela principal da aplicação
window = SuperFoco()

# Exibe a janela
window.showMaximized()

# Executa o loop da aplicação
sys.exit(app.exec_())