# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foco.ui'
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/lion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_af_mode = QtWidgets.QLabel(Dialog)
        self.label_af_mode.setGeometry(QtCore.QRect(30, 30, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_af_mode.setFont(font)
        self.label_af_mode.setObjectName("label_af_mode")
        self.comboBox_af_mode = QtWidgets.QComboBox(Dialog)
        self.comboBox_af_mode.setGeometry(QtCore.QRect(110, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_af_mode.setFont(font)
        self.comboBox_af_mode.setObjectName("comboBox_af_mode")
        self.comboBox_af_mode.addItem("")
        self.comboBox_af_mode.addItem("")
        self.comboBox_af_mode.addItem("")
        self.label_af_pause = QtWidgets.QLabel(Dialog)
        self.label_af_pause.setGeometry(QtCore.QRect(260, 30, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_af_pause.setFont(font)
        self.label_af_pause.setObjectName("label_af_pause")
        self.comboBox_af_pause = QtWidgets.QComboBox(Dialog)
        self.comboBox_af_pause.setGeometry(QtCore.QRect(350, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_af_pause.setFont(font)
        self.comboBox_af_pause.setObjectName("comboBox_af_pause")
        self.comboBox_af_pause.addItem("")
        self.comboBox_af_pause.addItem("")
        self.comboBox_af_pause.addItem("")
        self.comboBox_af_range = QtWidgets.QComboBox(Dialog)
        self.comboBox_af_range.setGeometry(QtCore.QRect(590, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_af_range.setFont(font)
        self.comboBox_af_range.setObjectName("comboBox_af_range")
        self.comboBox_af_range.addItem("")
        self.comboBox_af_range.addItem("")
        self.comboBox_af_range.addItem("")
        self.label_af_range = QtWidgets.QLabel(Dialog)
        self.label_af_range.setGeometry(QtCore.QRect(500, 30, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_af_range.setFont(font)
        self.label_af_range.setObjectName("label_af_range")
        self.comboBox_af_speed = QtWidgets.QComboBox(Dialog)
        self.comboBox_af_speed.setGeometry(QtCore.QRect(840, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_af_speed.setFont(font)
        self.comboBox_af_speed.setObjectName("comboBox_af_speed")
        self.comboBox_af_speed.addItem("")
        self.comboBox_af_speed.addItem("")
        self.label_af_speed = QtWidgets.QLabel(Dialog)
        self.label_af_speed.setGeometry(QtCore.QRect(750, 30, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_af_speed.setFont(font)
        self.label_af_speed.setObjectName("label_af_speed")
        self.label_af_trigger = QtWidgets.QLabel(Dialog)
        self.label_af_trigger.setGeometry(QtCore.QRect(120, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_af_trigger.setFont(font)
        self.label_af_trigger.setObjectName("label_af_trigger")
        self.pushButton_trigger_start = QtWidgets.QPushButton(Dialog)
        self.pushButton_trigger_start.setGeometry(QtCore.QRect(50, 180, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_trigger_start.setFont(font)
        self.pushButton_trigger_start.setObjectName("pushButton_trigger_start")
        self.pushButton_trigger_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_trigger_cancel.setGeometry(QtCore.QRect(180, 180, 93, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_trigger_cancel.setFont(font)
        self.pushButton_trigger_cancel.setObjectName("pushButton_trigger_cancel")
        self.pushButton_main_w = QtWidgets.QPushButton(Dialog)
        self.pushButton_main_w.setGeometry(QtCore.QRect(1140, 600, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_main_w.setFont(font)
        self.pushButton_main_w.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_main_w.setObjectName("pushButton_main_w")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Foco"))
        self.label_af_mode.setText(_translate("Dialog", "AfMode"))
        self.comboBox_af_mode.setItemText(0, _translate("Dialog", "Manual"))
        self.comboBox_af_mode.setItemText(1, _translate("Dialog", "Auto"))
        self.comboBox_af_mode.setItemText(2, _translate("Dialog", "Continuous"))
        self.label_af_pause.setText(_translate("Dialog", "AfPause"))
        self.comboBox_af_pause.setItemText(0, _translate("Dialog", "Deferred"))
        self.comboBox_af_pause.setItemText(1, _translate("Dialog", "Immediate"))
        self.comboBox_af_pause.setItemText(2, _translate("Dialog", "Resume"))
        self.comboBox_af_range.setItemText(0, _translate("Dialog", "Normal"))
        self.comboBox_af_range.setItemText(1, _translate("Dialog", "Macro"))
        self.comboBox_af_range.setItemText(2, _translate("Dialog", "Full"))
        self.label_af_range.setText(_translate("Dialog", "AfRange"))
        self.comboBox_af_speed.setItemText(0, _translate("Dialog", "Normal"))
        self.comboBox_af_speed.setItemText(1, _translate("Dialog", "Fast"))
        self.label_af_speed.setText(_translate("Dialog", "AfSpeed"))
        self.label_af_trigger.setText(_translate("Dialog", "AfTrigger"))
        self.pushButton_trigger_start.setText(_translate("Dialog", "Start"))
        self.pushButton_trigger_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_main_w.setText(_translate("Dialog", "Voltar"))
import py_GUIs.icones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
