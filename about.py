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

class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName(_fromUtf8("about"))
        about.resize(467, 173)
        self.centralwidget = QtGui.QWidget(about)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 441, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Zekton"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 100, 71, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Zekton"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Zekton"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        about.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(about)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        about.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(about)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        about.setStatusBar(self.statusbar)

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        about.setWindowTitle(_translate("about", "About", None))
        self.label.setText(_translate("about", "Python GUI tool to Synchronize Subtitles files srt and ass", None))
        self.label_3.setText(_translate("about", "by MGF15", None))
        self.label_4.setText(_translate("about", "Source", None))

