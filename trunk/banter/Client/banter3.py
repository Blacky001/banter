# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter3.ui'
#
# Created: Fri Sep 17 15:02:11 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Mbanter3(object):
    def setupUi(self, Mbanter3):
        Mbanter3.setObjectName("Mbanter3")
        Mbanter3.resize(419, 117)
        Mbanter3.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        Mbanter3.setUnifiedTitleAndToolBarOnMac(True)
        self.add = QtGui.QWidget(Mbanter3)
        self.add.setObjectName("add")
        self.lineEdit = QtGui.QLineEdit(self.add)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 301, 27))
        font = QtGui.QFont()
        font.setFamily("Tlwg Typist")
        font.setPointSize(11)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.send = QtGui.QCommandLinkButton(self.add)
        self.send.setGeometry(QtCore.QRect(250, 60, 91, 31))
        self.send.setObjectName("send")
        Mbanter3.setCentralWidget(self.add)
        self.statusbar = QtGui.QStatusBar(Mbanter3)
        self.statusbar.setObjectName("statusbar")
        Mbanter3.setStatusBar(self.statusbar)

        self.retranslateUi(Mbanter3)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("textChanged(QString)"), self.send.show)
        QtCore.QMetaObject.connectSlotsByName(Mbanter3)

    def retranslateUi(self, Mbanter3):
        Mbanter3.setWindowTitle(QtGui.QApplication.translate("Mbanter3", "banter3", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Mbanter3", "        <add the address>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setProperty("enter", QtGui.QApplication.translate("Mbanter3", "tffttftftf", None, QtGui.QApplication.UnicodeUTF8))
        self.send.setText(QtGui.QApplication.translate("Mbanter3", "send", None, QtGui.QApplication.UnicodeUTF8))

