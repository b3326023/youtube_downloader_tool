# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_url.setGeometry(QtCore.QRect(80, 50, 331, 22))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.lineEdit_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dir.setGeometry(QtCore.QRect(80, 120, 331, 22))
        self.lineEdit_dir.setText("D:\Python\Youtube_Downloader\download")
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.btn_dl = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dl.setGeometry(QtCore.QRect(190, 180, 211, 31))
        self.btn_dl.setObjectName("btn_dl")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 71, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_fmt = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_fmt.setGeometry(QtCore.QRect(80, 180, 80, 31))
        self.comboBox_fmt.setObjectName("comboBox_fmt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube-Downloader"))
        self.label.setText(_translate("MainWindow", "影片網址:"))
        self.label_2.setText(_translate("MainWindow", "下載位置:"))
        self.btn_dl.setText(_translate("MainWindow", "下載"))
        self.label_3.setText(_translate("MainWindow", "檔案格式:"))
