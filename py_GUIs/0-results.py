# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 652)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/lion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridResultados = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridResultados.setContentsMargins(0, 0, 0, 0)
        self.gridResultados.setObjectName("gridResultados")
        self.label_icone_bpm = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_icone_bpm.setStyleSheet("image: url(:/icones/coracao.png);")
        self.label_icone_bpm.setText("")
        self.label_icone_bpm.setObjectName("label_icone_bpm")
        self.gridResultados.addWidget(self.label_icone_bpm, 0, 0, 1, 1)
        self.label_text_irpm = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_text_irpm.setObjectName("label_text_irpm")
        self.gridResultados.addWidget(self.label_text_irpm, 1, 1, 1, 1)
        self.label_text_bpm = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_text_bpm.setObjectName("label_text_bpm")
        self.gridResultados.addWidget(self.label_text_bpm, 0, 1, 1, 1)
        self.label_icone_irpm = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_icone_irpm.setStyleSheet("image: url(:/icones/respiracao.png);")
        self.label_icone_irpm.setText("")
        self.label_icone_irpm.setObjectName("label_icone_irpm")
        self.gridResultados.addWidget(self.label_icone_irpm, 1, 0, 1, 1)
        self.lineEdit_bom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_bom.sizePolicy().hasHeightForWidth())
        self.lineEdit_bom.setSizePolicy(sizePolicy)
        self.lineEdit_bom.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_bom.setReadOnly(True)
        self.lineEdit_bom.setObjectName("lineEdit_bom")
        self.gridResultados.addWidget(self.lineEdit_bom, 0, 2, 1, 1)
        self.lineEdit_irpm = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_irpm.sizePolicy().hasHeightForWidth())
        self.lineEdit_irpm.setSizePolicy(sizePolicy)
        self.lineEdit_irpm.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_irpm.setReadOnly(True)
        self.lineEdit_irpm.setObjectName("lineEdit_irpm")
        self.gridResultados.addWidget(self.lineEdit_irpm, 1, 2, 1, 1)
        self.gridResultados.setColumnStretch(0, 1)
        self.gridResultados.setColumnStretch(1, 6)
        self.gridResultados.setColumnStretch(2, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(650, 10, 591, 481))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridGrafico = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridGrafico.setContentsMargins(0, 0, 0, 0)
        self.gridGrafico.setObjectName("gridGrafico")
        self.spinBox_t_sup = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_t_sup.sizePolicy().hasHeightForWidth())
        self.spinBox_t_sup.setSizePolicy(sizePolicy)
        self.spinBox_t_sup.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_t_sup.setMaximum(99999)
        self.spinBox_t_sup.setProperty("value", 30)
        self.spinBox_t_sup.setObjectName("spinBox_t_sup")
        self.gridGrafico.addWidget(self.spinBox_t_sup, 3, 1, 1, 1)
        self.label_t_sup = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_t_sup.setObjectName("label_t_sup")
        self.gridGrafico.addWidget(self.label_t_sup, 3, 0, 1, 1)
        self.label_t_inf = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_t_inf.setObjectName("label_t_inf")
        self.gridGrafico.addWidget(self.label_t_inf, 2, 0, 1, 1)
        self.spinBox_t_inf = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_t_inf.sizePolicy().hasHeightForWidth())
        self.spinBox_t_inf.setSizePolicy(sizePolicy)
        self.spinBox_t_inf.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_t_inf.setMaximum(9999)
        self.spinBox_t_inf.setObjectName("spinBox_t_inf")
        self.gridGrafico.addWidget(self.spinBox_t_inf, 2, 1, 1, 1)
        self.comboBox_grafico = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_grafico.sizePolicy().hasHeightForWidth())
        self.comboBox_grafico.setSizePolicy(sizePolicy)
        self.comboBox_grafico.setObjectName("comboBox_grafico")
        self.comboBox_grafico.addItem("")
        self.comboBox_grafico.addItem("")
        self.comboBox_grafico.addItem("")
        self.gridGrafico.addWidget(self.comboBox_grafico, 0, 1, 1, 1)
        self.label_grafico = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_grafico.setObjectName("label_grafico")
        self.gridGrafico.addWidget(self.label_grafico, 0, 0, 1, 1)
        self.label_metodo = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_metodo.setObjectName("label_metodo")
        self.gridGrafico.addWidget(self.label_metodo, 1, 0, 1, 1)
        self.comboBox_metodo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_metodo.sizePolicy().hasHeightForWidth())
        self.comboBox_metodo.setSizePolicy(sizePolicy)
        self.comboBox_metodo.setObjectName("comboBox_metodo")
        self.comboBox_metodo.addItem("")
        self.comboBox_metodo.addItem("")
        self.gridGrafico.addWidget(self.comboBox_metodo, 1, 1, 1, 1)
        self.gridGrafico.setRowStretch(0, 2)
        self.gridGrafico.setRowStretch(1, 2)
        self.gridGrafico.setRowStretch(2, 5)
        self.gridGrafico.setRowStretch(3, 5)
        self.pushButton_grafico = QtWidgets.QPushButton(Dialog)
        self.pushButton_grafico.setGeometry(QtCore.QRect(910, 600, 191, 41))
        self.pushButton_grafico.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_grafico.setObjectName("pushButton_grafico")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(19, 229, 331, 271))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridSecondResults = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridSecondResults.setContentsMargins(0, 0, 0, 0)
        self.gridSecondResults.setObjectName("gridSecondResults")
        self.label_IQ1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_IQ1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_IQ1.setObjectName("label_IQ1")
        self.gridSecondResults.addWidget(self.label_IQ1, 3, 0, 1, 1)
        self.label_t_afericao = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_t_afericao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_t_afericao.setObjectName("label_t_afericao")
        self.gridSecondResults.addWidget(self.label_t_afericao, 0, 0, 1, 1)
        self.label_t_total = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_t_total.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_t_total.setObjectName("label_t_total")
        self.gridSecondResults.addWidget(self.label_t_total, 2, 0, 1, 1)
        self.lineEdit_t_total = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_t_total.sizePolicy().hasHeightForWidth())
        self.lineEdit_t_total.setSizePolicy(sizePolicy)
        self.lineEdit_t_total.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_t_total.setReadOnly(True)
        self.lineEdit_t_total.setObjectName("lineEdit_t_total")
        self.gridSecondResults.addWidget(self.lineEdit_t_total, 2, 1, 1, 1)
        self.lineEdit_t_afericao = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_t_afericao.sizePolicy().hasHeightForWidth())
        self.lineEdit_t_afericao.setSizePolicy(sizePolicy)
        self.lineEdit_t_afericao.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_t_afericao.setReadOnly(True)
        self.lineEdit_t_afericao.setObjectName("lineEdit_t_afericao")
        self.gridSecondResults.addWidget(self.lineEdit_t_afericao, 0, 1, 1, 1)
        self.lineEdit_t_analise = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_t_analise.sizePolicy().hasHeightForWidth())
        self.lineEdit_t_analise.setSizePolicy(sizePolicy)
        self.lineEdit_t_analise.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_t_analise.setReadOnly(True)
        self.lineEdit_t_analise.setObjectName("lineEdit_t_analise")
        self.gridSecondResults.addWidget(self.lineEdit_t_analise, 1, 1, 1, 1)
        self.label_t_analise = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_t_analise.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_t_analise.setObjectName("label_t_analise")
        self.gridSecondResults.addWidget(self.label_t_analise, 1, 0, 1, 1)
        self.label_IQ2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_IQ2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_IQ2.setObjectName("label_IQ2")
        self.gridSecondResults.addWidget(self.label_IQ2, 4, 0, 1, 1)
        self.lineEdit_iq1 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_iq1.sizePolicy().hasHeightForWidth())
        self.lineEdit_iq1.setSizePolicy(sizePolicy)
        self.lineEdit_iq1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_iq1.setReadOnly(True)
        self.lineEdit_iq1.setObjectName("lineEdit_iq1")
        self.gridSecondResults.addWidget(self.lineEdit_iq1, 3, 1, 1, 1)
        self.lineEdit_iq2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_iq2.sizePolicy().hasHeightForWidth())
        self.lineEdit_iq2.setSizePolicy(sizePolicy)
        self.lineEdit_iq2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_iq2.setReadOnly(True)
        self.lineEdit_iq2.setObjectName("lineEdit_iq2")
        self.gridSecondResults.addWidget(self.lineEdit_iq2, 4, 1, 1, 1)
        self.gridSecondResults.setColumnStretch(0, 5)
        self.gridSecondResults.setColumnStretch(1, 1)
        self.pushButton_amostragem = QtWidgets.QPushButton(Dialog)
        self.pushButton_amostragem.setGeometry(QtCore.QRect(660, 600, 221, 41))
        self.pushButton_amostragem.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_amostragem.setObjectName("pushButton_amostragem")
        self.pushButton_main_w = QtWidgets.QPushButton(Dialog)
        self.pushButton_main_w.setGeometry(QtCore.QRect(1130, 600, 131, 41))
        self.pushButton_main_w.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_main_w.setObjectName("pushButton_main_w")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "lion - Results"))
        self.label_text_irpm.setText(_translate("Dialog", "Incursões respiratórias por minuto (iRPM):"))
        self.label_text_bpm.setText(_translate("Dialog", "Batimentos por minuto (BPM):"))
        self.label_t_sup.setText(_translate("Dialog", "Tempo superior:"))
        self.label_t_inf.setText(_translate("Dialog", "Tempo inferior:"))
        self.comboBox_grafico.setItemText(0, _translate("Dialog", "BVP"))
        self.comboBox_grafico.setItemText(1, _translate("Dialog", "BVP filtrado"))
        self.comboBox_grafico.setItemText(2, _translate("Dialog", "Análise espectral"))
        self.label_grafico.setText(_translate("Dialog", "Selecione o gráfico:"))
        self.label_metodo.setText(_translate("Dialog", "Método de análise:"))
        self.comboBox_metodo.setItemText(0, _translate("Dialog", "GREEN"))
        self.comboBox_metodo.setItemText(1, _translate("Dialog", "GRGB"))
        self.pushButton_grafico.setText(_translate("Dialog", "Vizualizar gráfico"))
        self.label_IQ1.setText(_translate("Dialog", "IQ1:"))
        self.label_t_afericao.setText(_translate("Dialog", "Tempo de aferição (s):"))
        self.label_t_total.setText(_translate("Dialog", "Tempo total (s):"))
        self.label_t_analise.setText(_translate("Dialog", "Tempo de análise (s):"))
        self.label_IQ2.setText(_translate("Dialog", "IQ2:"))
        self.lineEdit_iq1.setText(_translate("Dialog", "*"))
        self.lineEdit_iq2.setText(_translate("Dialog", "*"))
        self.pushButton_amostragem.setText(_translate("Dialog", "Análise da amostragem"))
        self.pushButton_main_w.setText(_translate("Dialog", "Voltar"))
import icones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
