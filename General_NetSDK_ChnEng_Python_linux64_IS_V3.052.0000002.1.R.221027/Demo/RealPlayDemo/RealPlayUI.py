# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RealPlayUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PlayWnd = QtWidgets.QLabel(self.centralwidget)
        self.PlayWnd.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.PlayWnd.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.PlayWnd.setObjectName("PlayWnd")
        self.IP_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IP_lineEdit.setGeometry(QtCore.QRect(90, 380, 81, 20))
        self.IP_lineEdit.setObjectName("IP_lineEdit")
        self.IP_label = QtWidgets.QLabel(self.centralwidget)
        self.IP_label.setGeometry(QtCore.QRect(10, 380, 61, 16))
        self.IP_label.setObjectName("IP_label")
        self.Port_label = QtWidgets.QLabel(self.centralwidget)
        self.Port_label.setGeometry(QtCore.QRect(190, 380, 61, 16))
        self.Port_label.setObjectName("Port_label")
        self.Port_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Port_lineEdit.setGeometry(QtCore.QRect(260, 380, 61, 20))
        self.Port_lineEdit.setObjectName("Port_lineEdit")
        self.Name_label = QtWidgets.QLabel(self.centralwidget)
        self.Name_label.setGeometry(QtCore.QRect(10, 420, 71, 16))
        self.Name_label.setObjectName("Name_label")
        self.Name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_lineEdit.setGeometry(QtCore.QRect(90, 420, 81, 20))
        self.Name_lineEdit.setObjectName("Name_lineEdit")
        self.Pwd_label = QtWidgets.QLabel(self.centralwidget)
        self.Pwd_label.setGeometry(QtCore.QRect(190, 420, 54, 12))
        self.Pwd_label.setObjectName("Pwd_label")
        self.Pwd_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Pwd_lineEdit.setGeometry(QtCore.QRect(260, 420, 111, 20))
        self.Pwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pwd_lineEdit.setObjectName("Pwd_lineEdit")
        self.Channel_label = QtWidgets.QLabel(self.centralwidget)
        self.Channel_label.setGeometry(QtCore.QRect(330, 380, 81, 16))
        self.Channel_label.setObjectName("Channel_label")
        self.Channel_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Channel_comboBox.setGeometry(QtCore.QRect(420, 380, 69, 22))
        self.Channel_comboBox.setObjectName("Channel_comboBox")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(400, 410, 91, 31))
        self.login_btn.setObjectName("login_btn")
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(400, 450, 91, 31))
        self.play_btn.setObjectName("play_btn")
        self.StreamTyp_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.StreamTyp_comboBox.setEnabled(False)
        self.StreamTyp_comboBox.setGeometry(QtCore.QRect(90, 460, 131, 22))
        self.StreamTyp_comboBox.setObjectName("StreamTyp_comboBox")
        self.StreamTyp_comboBox.addItem("")
        self.StreamTyp_comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 460, 71, 16))
        self.label_5.setObjectName("label_5")
        self.Channel_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Channel_label_2.setGeometry(QtCore.QRect(240, 460, 81, 16))
        self.Channel_label_2.setObjectName("Channel_label_2")
        self.PlayMode_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.PlayMode_comboBox.setEnabled(False)
        self.PlayMode_comboBox.setGeometry(QtCore.QRect(310, 460, 69, 22))
        self.PlayMode_comboBox.setObjectName("PlayMode_comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "实时监视(RealPlay)"))
        self.PlayWnd.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\">实时监视（RealPlay）</p></body></html>"))
        self.IP_label.setText(_translate("MainWindow", "IP地址(IP)"))
        self.Port_label.setText(_translate("MainWindow", "端口(Port)"))
        self.Name_label.setText(_translate("MainWindow", "用户名(Name)"))
        self.Pwd_label.setText(_translate("MainWindow", "密码(PWD)"))
        self.Channel_label.setText(_translate("MainWindow", "通道(Channel)"))
        self.login_btn.setText(_translate("MainWindow", "登录(Login)"))
        self.play_btn.setText(_translate("MainWindow", "监视(Play)"))
        self.StreamTyp_comboBox.setItemText(0, _translate("MainWindow", "主码流(MainStream)"))
        self.StreamTyp_comboBox.setItemText(1, _translate("MainWindow", "辅码流(ExtraStream)"))
        self.label_5.setText(_translate("MainWindow", "码流(Stream)"))
        self.Channel_label_2.setText(_translate("MainWindow", "模式(Mode)"))

