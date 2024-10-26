import sys
from PyQt5.QtWidgets import QApplication
from modulos.super_results import SuperResults

# Cria a aplicação
app = QApplication(sys.argv)

# Instancia a janela principal da aplicação
window = SuperResults()

# Exibe a janela
window.showMaximized()

# Executa o loop da aplicação
sys.exit(app.exec_())