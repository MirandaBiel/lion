import sys
from PyQt5.QtWidgets import QApplication
from modulos.super_config import SuperConfig

# Cria a aplicação
app = QApplication(sys.argv)

# Instancia a janela principal da aplicação
window = SuperConfig()

# Exibe a janela
window.showMaximized()

# Executa o loop da aplicação
sys.exit(app.exec_())