# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advanced_settings.ui'
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
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/lion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton_main_w = QtWidgets.QPushButton(Dialog)
        self.pushButton_main_w.setGeometry(QtCore.QRect(1140, 600, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_main_w.setFont(font)
        self.pushButton_main_w.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_main_w.setObjectName("pushButton_main_w")
        self.label_config_b = QtWidgets.QLabel(Dialog)
        self.label_config_b.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.label_config_b.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_config_b.setObjectName("label_config_b")
        self.comboBox_base_config = QtWidgets.QComboBox(Dialog)
        self.comboBox_base_config.setGeometry(QtCore.QRect(160, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_base_config.setFont(font)
        self.comboBox_base_config.setObjectName("comboBox_base_config")
        self.comboBox_base_config.addItem("")
        self.comboBox_base_config.addItem("")
        self.comboBox_base_config.addItem("")
        self.label_n_buffers = QtWidgets.QLabel(Dialog)
        self.label_n_buffers.setGeometry(QtCore.QRect(20, 140, 141, 31))
        self.label_n_buffers.setObjectName("label_n_buffers")
        self.spinBox_n_buffers = QtWidgets.QSpinBox(Dialog)
        self.spinBox_n_buffers.setGeometry(QtCore.QRect(190, 110, 91, 101))
        self.spinBox_n_buffers.setProperty("value", 12)
        self.spinBox_n_buffers.setObjectName("spinBox_n_buffers")
        self.label_espaco_cores = QtWidgets.QLabel(Dialog)
        self.label_espaco_cores.setGeometry(QtCore.QRect(20, 260, 131, 21))
        self.label_espaco_cores.setObjectName("label_espaco_cores")
        self.comboBox_Esp_cores = QtWidgets.QComboBox(Dialog)
        self.comboBox_Esp_cores.setGeometry(QtCore.QRect(170, 250, 91, 41))
        self.comboBox_Esp_cores.setObjectName("comboBox_Esp_cores")
        self.comboBox_Esp_cores.addItem("")
        self.comboBox_Esp_cores.addItem("")
        self.comboBox_Esp_cores.addItem("")
        self.label_foramto = QtWidgets.QLabel(Dialog)
        self.label_foramto.setGeometry(QtCore.QRect(20, 340, 81, 21))
        self.label_foramto.setObjectName("label_foramto")
        self.comboBox_formato = QtWidgets.QComboBox(Dialog)
        self.comboBox_formato.setGeometry(QtCore.QRect(110, 330, 91, 41))
        self.comboBox_formato.setObjectName("comboBox_formato")
        self.comboBox_formato.addItem("")
        self.comboBox_formato.addItem("")
        self.comboBox_formato.addItem("")
        self.comboBox_formato.addItem("")
        self.comboBox_formato.addItem("")
        self.label_sat = QtWidgets.QLabel(Dialog)
        self.label_sat.setGeometry(QtCore.QRect(340, 30, 81, 21))
        self.label_sat.setObjectName("label_sat")
        self.horizontalSlider_sat = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_sat.setGeometry(QtCore.QRect(440, 30, 281, 22))
        self.horizontalSlider_sat.setMaximum(20)
        self.horizontalSlider_sat.setSingleStep(1)
        self.horizontalSlider_sat.setProperty("value", 10)
        self.horizontalSlider_sat.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_sat.setObjectName("horizontalSlider_sat")
        self.label_cont = QtWidgets.QLabel(Dialog)
        self.label_cont.setGeometry(QtCore.QRect(340, 90, 81, 21))
        self.label_cont.setObjectName("label_cont")
        self.horizontalSlider_contr = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_contr.setGeometry(QtCore.QRect(440, 90, 281, 22))
        self.horizontalSlider_contr.setMaximum(20)
        self.horizontalSlider_contr.setProperty("value", 10)
        self.horizontalSlider_contr.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_contr.setObjectName("horizontalSlider_contr")
        self.label_aguc = QtWidgets.QLabel(Dialog)
        self.label_aguc.setGeometry(QtCore.QRect(340, 150, 101, 21))
        self.label_aguc.setObjectName("label_aguc")
        self.horizontalSlider_aguca = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_aguca.setGeometry(QtCore.QRect(440, 150, 281, 22))
        self.horizontalSlider_aguca.setMaximum(20)
        self.horizontalSlider_aguca.setProperty("value", 10)
        self.horizontalSlider_aguca.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_aguca.setObjectName("horizontalSlider_aguca")
        self.label_brilho = QtWidgets.QLabel(Dialog)
        self.label_brilho.setGeometry(QtCore.QRect(340, 210, 61, 21))
        self.label_brilho.setObjectName("label_brilho")
        self.horizontalSlider_brilho = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_brilho.setGeometry(QtCore.QRect(440, 210, 281, 22))
        self.horizontalSlider_brilho.setMinimum(-10)
        self.horizontalSlider_brilho.setMaximum(10)
        self.horizontalSlider_brilho.setSingleStep(1)
        self.horizontalSlider_brilho.setProperty("value", 0)
        self.horizontalSlider_brilho.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_brilho.setObjectName("horizontalSlider_brilho")
        self.checkBox_AE = QtWidgets.QCheckBox(Dialog)
        self.checkBox_AE.setGeometry(QtCore.QRect(460, 270, 101, 20))
        self.checkBox_AE.setChecked(True)
        self.checkBox_AE.setObjectName("checkBox_AE")
        self.label_AE_contraint_mode = QtWidgets.QLabel(Dialog)
        self.label_AE_contraint_mode.setGeometry(QtCore.QRect(960, 20, 141, 41))
        self.label_AE_contraint_mode.setObjectName("label_AE_contraint_mode")
        self.comboBox_Ae_constraint = QtWidgets.QComboBox(Dialog)
        self.comboBox_Ae_constraint.setGeometry(QtCore.QRect(1110, 20, 91, 41))
        self.comboBox_Ae_constraint.setObjectName("comboBox_Ae_constraint")
        self.comboBox_Ae_constraint.addItem("")
        self.comboBox_Ae_constraint.addItem("")
        self.comboBox_Ae_constraint.addItem("")
        self.comboBox_Ae_constraint.addItem("")
        self.label_AE_exposure = QtWidgets.QLabel(Dialog)
        self.label_AE_exposure.setGeometry(QtCore.QRect(960, 90, 131, 31))
        self.label_AE_exposure.setObjectName("label_AE_exposure")
        self.comboBox_AE_exposure = QtWidgets.QComboBox(Dialog)
        self.comboBox_AE_exposure.setGeometry(QtCore.QRect(1110, 90, 91, 41))
        self.comboBox_AE_exposure.setObjectName("comboBox_AE_exposure")
        self.comboBox_AE_exposure.addItem("")
        self.comboBox_AE_exposure.addItem("")
        self.comboBox_AE_exposure.addItem("")
        self.comboBox_AE_exposure.addItem("")
        self.label_AE_fliker_mode = QtWidgets.QLabel(Dialog)
        self.label_AE_fliker_mode.setGeometry(QtCore.QRect(960, 170, 121, 21))
        self.label_AE_fliker_mode.setObjectName("label_AE_fliker_mode")
        self.comboBox_AE_Fliker_mode = QtWidgets.QComboBox(Dialog)
        self.comboBox_AE_Fliker_mode.setGeometry(QtCore.QRect(1080, 160, 151, 41))
        self.comboBox_AE_Fliker_mode.setObjectName("comboBox_AE_Fliker_mode")
        self.comboBox_AE_Fliker_mode.addItem("")
        self.comboBox_AE_Fliker_mode.addItem("")
        self.label_AE_fliker_period = QtWidgets.QLabel(Dialog)
        self.label_AE_fliker_period.setGeometry(QtCore.QRect(960, 250, 121, 21))
        self.label_AE_fliker_period.setObjectName("label_AE_fliker_period")
        self.spinBox_AE_fliker_period = QtWidgets.QSpinBox(Dialog)
        self.spinBox_AE_fliker_period.setGeometry(QtCore.QRect(1090, 220, 131, 81))
        self.spinBox_AE_fliker_period.setMaximum(999999999)
        self.spinBox_AE_fliker_period.setProperty("value", 8333)
        self.spinBox_AE_fliker_period.setObjectName("spinBox_AE_fliker_period")
        self.label_AE_metering = QtWidgets.QLabel(Dialog)
        self.label_AE_metering.setGeometry(QtCore.QRect(960, 350, 131, 20))
        self.label_AE_metering.setObjectName("label_AE_metering")
        self.comboBox_AE_metering = QtWidgets.QComboBox(Dialog)
        self.comboBox_AE_metering.setGeometry(QtCore.QRect(1110, 340, 151, 41))
        self.comboBox_AE_metering.setObjectName("comboBox_AE_metering")
        self.comboBox_AE_metering.addItem("")
        self.comboBox_AE_metering.addItem("")
        self.comboBox_AE_metering.addItem("")
        self.comboBox_AE_metering.addItem("")
        self.checkBox_AWB = QtWidgets.QCheckBox(Dialog)
        self.checkBox_AWB.setGeometry(QtCore.QRect(310, 270, 111, 20))
        self.checkBox_AWB.setChecked(True)
        self.checkBox_AWB.setObjectName("checkBox_AWB")
        self.label_AWB_mode = QtWidgets.QLabel(Dialog)
        self.label_AWB_mode.setGeometry(QtCore.QRect(250, 340, 81, 16))
        self.label_AWB_mode.setObjectName("label_AWB_mode")
        self.comboBox_AWB_mode = QtWidgets.QComboBox(Dialog)
        self.comboBox_AWB_mode.setGeometry(QtCore.QRect(340, 330, 101, 41))
        self.comboBox_AWB_mode.setObjectName("comboBox_AWB_mode")
        self.comboBox_AWB_mode.addItem("")
        self.comboBox_AWB_mode.addItem("")
        self.comboBox_AWB_mode.addItem("")
        self.comboBox_AWB_mode.addItem("")
        self.comboBox_AWB_mode.addItem("")
        self.comboBox_AWB_mode.addItem("")
        self.comboBox_AWB_mode.addItem("")
        self.label_ganho_de_cor = QtWidgets.QLabel(Dialog)
        self.label_ganho_de_cor.setGeometry(QtCore.QRect(780, 30, 101, 16))
        self.label_ganho_de_cor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ganho_de_cor.setObjectName("label_ganho_de_cor")
        self.doubleSpinBox_vermelh_ganho = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_vermelh_ganho.setGeometry(QtCore.QRect(780, 80, 101, 71))
        self.doubleSpinBox_vermelh_ganho.setProperty("value", 1.0)
        self.doubleSpinBox_vermelh_ganho.setObjectName("doubleSpinBox_vermelh_ganho")
        self.doubleSpinBox_azul_gain = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_azul_gain.setGeometry(QtCore.QRect(780, 190, 101, 71))
        self.doubleSpinBox_azul_gain.setProperty("value", 1.0)
        self.doubleSpinBox_azul_gain.setObjectName("doubleSpinBox_azul_gain")
        self.label_ver = QtWidgets.QLabel(Dialog)
        self.label_ver.setGeometry(QtCore.QRect(780, 60, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_ver.setFont(font)
        self.label_ver.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ver.setObjectName("label_ver")
        self.label_azul = QtWidgets.QLabel(Dialog)
        self.label_azul.setGeometry(QtCore.QRect(810, 170, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_azul.setFont(font)
        self.label_azul.setObjectName("label_azul")
        self.label_exposure_value = QtWidgets.QLabel(Dialog)
        self.label_exposure_value.setGeometry(QtCore.QRect(770, 280, 121, 20))
        self.label_exposure_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_exposure_value.setObjectName("label_exposure_value")
        self.doubleSpinBox_exposure_value = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_exposure_value.setGeometry(QtCore.QRect(780, 310, 101, 71))
        self.doubleSpinBox_exposure_value.setMinimum(1.0)
        self.doubleSpinBox_exposure_value.setObjectName("doubleSpinBox_exposure_value")
        self.label_hdr_channel = QtWidgets.QLabel(Dialog)
        self.label_hdr_channel.setGeometry(QtCore.QRect(480, 340, 91, 16))
        self.label_hdr_channel.setObjectName("label_hdr_channel")
        self.comboBox_HDR_Channel = QtWidgets.QComboBox(Dialog)
        self.comboBox_HDR_Channel.setGeometry(QtCore.QRect(580, 330, 151, 41))
        self.comboBox_HDR_Channel.setObjectName("comboBox_HDR_Channel")
        self.comboBox_HDR_Channel.addItem("")
        self.comboBox_HDR_Channel.addItem("")
        self.comboBox_HDR_Channel.addItem("")
        self.comboBox_HDR_Channel.addItem("")
        self.label_hdr_mode = QtWidgets.QLabel(Dialog)
        self.label_hdr_mode.setGeometry(QtCore.QRect(20, 430, 71, 16))
        self.label_hdr_mode.setObjectName("label_hdr_mode")
        self.comboBox_HDR_MODE = QtWidgets.QComboBox(Dialog)
        self.comboBox_HDR_MODE.setGeometry(QtCore.QRect(110, 420, 191, 41))
        self.comboBox_HDR_MODE.setObjectName("comboBox_HDR_MODE")
        self.comboBox_HDR_MODE.addItem("")
        self.comboBox_HDR_MODE.addItem("")
        self.comboBox_HDR_MODE.addItem("")
        self.comboBox_HDR_MODE.addItem("")
        self.comboBox_HDR_MODE.addItem("")
        self.label_noise_red = QtWidgets.QLabel(Dialog)
        self.label_noise_red.setGeometry(QtCore.QRect(350, 430, 161, 16))
        self.label_noise_red.setObjectName("label_noise_red")
        self.comboBox_Noise_redu_mode = QtWidgets.QComboBox(Dialog)
        self.comboBox_Noise_redu_mode.setGeometry(QtCore.QRect(530, 420, 191, 41))
        self.comboBox_Noise_redu_mode.setObjectName("comboBox_Noise_redu_mode")
        self.comboBox_Noise_redu_mode.addItem("")
        self.comboBox_Noise_redu_mode.addItem("")
        self.comboBox_Noise_redu_mode.addItem("")

        self.retranslateUi(Dialog)
        self.comboBox_formato.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configurações Avançadas"))
        self.pushButton_main_w.setText(_translate("Dialog", "Voltar"))
        self.label_config_b.setText(_translate("Dialog", "Configuração base"))
        self.comboBox_base_config.setItemText(0, _translate("Dialog", "Vídeo"))
        self.comboBox_base_config.setItemText(1, _translate("Dialog", "Vizualização"))
        self.comboBox_base_config.setItemText(2, _translate("Dialog", "Foto"))
        self.label_n_buffers.setText(_translate("Dialog", "Número de Buffers"))
        self.label_espaco_cores.setText(_translate("Dialog", "Espaço de cores"))
        self.comboBox_Esp_cores.setItemText(0, _translate("Dialog", "RGB"))
        self.comboBox_Esp_cores.setItemText(1, _translate("Dialog", "YUV"))
        self.comboBox_Esp_cores.setItemText(2, _translate("Dialog", "HCV"))
        self.label_foramto.setText(_translate("Dialog", "Formato"))
        self.comboBox_formato.setItemText(0, _translate("Dialog", "992x750"))
        self.comboBox_formato.setItemText(1, _translate("Dialog", "800x600"))
        self.comboBox_formato.setItemText(2, _translate("Dialog", "640x480"))
        self.comboBox_formato.setItemText(3, _translate("Dialog", "512x384"))
        self.comboBox_formato.setItemText(4, _translate("Dialog", "320x240"))
        self.label_sat.setText(_translate("Dialog", "Saturação"))
        self.label_cont.setText(_translate("Dialog", "Contaste"))
        self.label_aguc.setText(_translate("Dialog", "Aguçamento"))
        self.label_brilho.setText(_translate("Dialog", "Brilho"))
        self.checkBox_AE.setText(_translate("Dialog", "AeEnable"))
        self.label_AE_contraint_mode.setText(_translate("Dialog", "AeConstraintMode"))
        self.comboBox_Ae_constraint.setItemText(0, _translate("Dialog", "Normal"))
        self.comboBox_Ae_constraint.setItemText(1, _translate("Dialog", "Highlight"))
        self.comboBox_Ae_constraint.setItemText(2, _translate("Dialog", "Shadows"))
        self.comboBox_Ae_constraint.setItemText(3, _translate("Dialog", "Custom"))
        self.label_AE_exposure.setText(_translate("Dialog", "AeExposureMode"))
        self.comboBox_AE_exposure.setItemText(0, _translate("Dialog", "Normal"))
        self.comboBox_AE_exposure.setItemText(1, _translate("Dialog", "Short"))
        self.comboBox_AE_exposure.setItemText(2, _translate("Dialog", "Long"))
        self.comboBox_AE_exposure.setItemText(3, _translate("Dialog", "Custom"))
        self.label_AE_fliker_mode.setText(_translate("Dialog", "AeFlickerMode"))
        self.comboBox_AE_Fliker_mode.setItemText(0, _translate("Dialog", "FlickerOff"))
        self.comboBox_AE_Fliker_mode.setItemText(1, _translate("Dialog", "FlickerManual"))
        self.label_AE_fliker_period.setText(_translate("Dialog", "AeFlickerPeriod"))
        self.label_AE_metering.setText(_translate("Dialog", "AeMeteringMode"))
        self.comboBox_AE_metering.setItemText(0, _translate("Dialog", "CentreWeighted"))
        self.comboBox_AE_metering.setItemText(1, _translate("Dialog", "Spot"))
        self.comboBox_AE_metering.setItemText(2, _translate("Dialog", "Matrix"))
        self.comboBox_AE_metering.setItemText(3, _translate("Dialog", "Custom"))
        self.checkBox_AWB.setText(_translate("Dialog", "AwbEnable"))
        self.label_AWB_mode.setText(_translate("Dialog", "AwbMode"))
        self.comboBox_AWB_mode.setItemText(0, _translate("Dialog", "Auto"))
        self.comboBox_AWB_mode.setItemText(1, _translate("Dialog", "Tungsten"))
        self.comboBox_AWB_mode.setItemText(2, _translate("Dialog", "Fluorescent"))
        self.comboBox_AWB_mode.setItemText(3, _translate("Dialog", "Indoor"))
        self.comboBox_AWB_mode.setItemText(4, _translate("Dialog", "Daylight"))
        self.comboBox_AWB_mode.setItemText(5, _translate("Dialog", "Cloudy"))
        self.comboBox_AWB_mode.setItemText(6, _translate("Dialog", "Custom"))
        self.label_ganho_de_cor.setText(_translate("Dialog", "Ganho de cor"))
        self.label_ver.setText(_translate("Dialog", "Vermelho"))
        self.label_azul.setText(_translate("Dialog", "Azul"))
        self.label_exposure_value.setText(_translate("Dialog", "ExposureValue"))
        self.label_hdr_channel.setText(_translate("Dialog", "HdrChannel"))
        self.comboBox_HDR_Channel.setItemText(0, _translate("Dialog", "HdrChannelNone"))
        self.comboBox_HDR_Channel.setItemText(1, _translate("Dialog", "HdrChannelShort"))
        self.comboBox_HDR_Channel.setItemText(2, _translate("Dialog", "HdrChannelMedium"))
        self.comboBox_HDR_Channel.setItemText(3, _translate("Dialog", "HdrChannelLong "))
        self.label_hdr_mode.setText(_translate("Dialog", "HdrMode"))
        self.comboBox_HDR_MODE.setItemText(0, _translate("Dialog", "Off "))
        self.comboBox_HDR_MODE.setItemText(1, _translate("Dialog", "SingleExposure"))
        self.comboBox_HDR_MODE.setItemText(2, _translate("Dialog", "MultiExposure"))
        self.comboBox_HDR_MODE.setItemText(3, _translate("Dialog", "Night"))
        self.comboBox_HDR_MODE.setItemText(4, _translate("Dialog", "MultiExposureUnmerged"))
        self.label_noise_red.setText(_translate("Dialog", "NoiseReductionMode"))
        self.comboBox_Noise_redu_mode.setItemText(0, _translate("Dialog", "Off "))
        self.comboBox_Noise_redu_mode.setItemText(1, _translate("Dialog", "Fast"))
        self.comboBox_Noise_redu_mode.setItemText(2, _translate("Dialog", "HighQuality"))
import py_GUIs.icones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
