# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 652)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/lion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # ... (Seu código para configurar widgets)

        # Criando o menu
        MainWindow.setMenuBar(self.menubar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 30))
        self.menubar.setObjectName("menubar")
        
        # Criando o menu "Salvar" e suas ações
        self.menuSalvar = QtWidgets.QMenu(self.menubar)
        self.menuSalvar.setObjectName("menuSalvar")
        
        # Criando uma ação de salvar
        self.actionSalvar = QtWidgets.QAction("Salvar", MainWindow)
        self.actionSalvar.triggered.connect(self.salvar_arquivo)  # Conectando a função
        
        # Adicionando a ação ao menu
        self.menuSalvar.addAction(self.actionSalvar)
        self.menubar.addAction(self.menuSalvar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "lion"))
        self.menuSalvar.setTitle(_translate("MainWindow", "Salvar"))
        # Adicione mais itens de tradução aqui se necessário

    # Função a ser chamada quando a ação "Salvar" é acionada
    def salvar_arquivo(self):
        QtWidgets.QMessageBox.information(None, "Salvar", "Arquivo salvo com sucesso!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
