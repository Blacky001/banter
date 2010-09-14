# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter/details.ui'
#
# Created: Tue Sep 14 13:28:46 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 496)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 62, 18))
        self.label.setObjectName("label")
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 30, 211, 21))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 62, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 62, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 62, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 61, 41))
        self.label_6.setObjectName("label_6")
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 70, 211, 21))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(120, 180, 211, 21))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(120, 130, 211, 21))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(120, 230, 211, 21))
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Pass word:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "call", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "last call\n"
"duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Last \n"
"caller:", None, QtGui.QApplication.UnicodeUTF8))

