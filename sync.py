# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Oct 10 14:34:30 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(345, 316)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Desktop/Sync/public/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 131, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(40, 140, 52, 27))
        self.spinBox.setRange(-5, 24)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(120, 140, 52, 27))
        self.spinBox_2.setRange(-59, 59)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(200, 140, 52, 27))
        self.spinBox_3.setRange(-59, 59)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(280, 140, 52, 27))
        self.spinBox_4.setRange(-1000, 1000)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 50, 321, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 321, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 145, 58, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 145, 58, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(93, 145, 58, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 145, 58, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 240, 87, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, -10, 171, 51))
        self.label_5.setStyleSheet(_fromUtf8("font-size:30px;"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 345, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "reSyncme", None))
        self.pushButton.setText(_translate("MainWindow", "Sync", None))
        self.pushButton_2.setText(_translate("MainWindow", "select file", None))
        self.pushButton_3.setText(_translate("MainWindow", "save it as", None))
        self.label.setText(_translate("MainWindow", "HH:", None))
        self.label_2.setText(_translate("MainWindow", "SS:", None))
        self.label_3.setText(_translate("MainWindow", "MM:", None))
        self.label_4.setText(_translate("MainWindow", "MS:", None))
        self.pushButton_4.setText(_translate("MainWindow", "about", None))
        self.label_5.setText(_translate("MainWindow", "Sync Subtitle", None))

