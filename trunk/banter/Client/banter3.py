# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter3.ui'
#
# Created: Tue Sep 14 15:13:47 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Mbanter3(object):
    def setupUi(self, Mbanter3):
        Mbanter3.setObjectName("Mbanter3")
        Mbanter3.resize(451, 293)
        Mbanter3.setStyleSheet("background-color: rgb(236, 218, 180);")
        Mbanter3.setUnifiedTitleAndToolBarOnMac(True)
        self.add = QtGui.QWidget(Mbanter3)
        self.add.setObjectName("add")
        self.lineEdit = QtGui.QLineEdit(self.add)
        self.lineEdit.setGeometry(QtCore.QRect(62, 60, 301, 27))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(11)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.send = QtGui.QPushButton(self.add)
        self.send.setGeometry(QtCore.QRect(150, 110, 93, 27))
        self.send.setObjectName("send")
        Mbanter3.setCentralWidget(self.add)
        self.statusbar = QtGui.QStatusBar(Mbanter3)
        self.statusbar.setObjectName("statusbar")
        Mbanter3.setStatusBar(self.statusbar)

        self.retranslateUi(Mbanter3)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textChanged(QString)"), self.send.show)
        QtCore.QObject.connect(self.send, QtCore.SIGNAL("clicked()"), Mbanter3.close)
        QtCore.QMetaObject.connectSlotsByName(Mbanter3)

    def retranslateUi(self, Mbanter3):
        Mbanter3.setWindowTitle(QtGui.QApplication.translate("Mbanter3", "banter3", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Mbanter3", "        <add the address>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setProperty("enter", QtGui.QApplication.translate("Mbanter3", "tffttftftf", None, QtGui.QApplication.UnicodeUTF8))
        self.send.setText(QtGui.QApplication.translate("Mbanter3", "send", None, QtGui.QApplication.UnicodeUTF8))

