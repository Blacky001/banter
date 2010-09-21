# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/banter1/trunk/banter/Server/details.ui'
#
# Created: Mon Sep 20 12:51:18 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 430)
        Dialog.setStyleSheet("""background-color: rgb(220, 225,255);
background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(157, 177, 195, 255));""")
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
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 62, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 62, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 211, 71, 20))
        self.label_6.setObjectName("label_6")
        self.textBrowser_2 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 70, 211, 21))
        self.textBrowser_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(120, 110, 211, 21))
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(120, 160, 211, 21))
        self.textBrowser_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(120, 210, 211, 21))
        self.textBrowser_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_5.setObjectName("textBrowser_5")
 #       self.pushButton = QtGui.QPushButton(Dialog)
  #      self.pushButton.setGeometry(QtCore.QRect(160, 370, 161, 31))
   #     self.pushButton.setStyleSheet("""background-color: rgb(141, 141, 106);
#background-color: rgb(117, 127, 135);""")
  #      self.pushButton.setObjectName("pushButton")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 71, 18))
        self.label_3.setObjectName("label_3")
        self.textBrowser_6 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(120, 260, 211, 21))
        self.textBrowser_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 310, 62, 18))
        self.label_7.setObjectName("label_7")
        self.textBrowser_7 = QtGui.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(120, 310, 211, 21))
        self.textBrowser_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_7.setObjectName("textBrowser_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Pass word:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "call\n"
"duration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "last call\n"
"duration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Last caller:", None, QtGui.QApplication.UnicodeUTF8))
       # self.pushButton.setText(QtGui.QApplication.translate("Dialog", "send message to", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "IP address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Port no:", None, QtGui.QApplication.UnicodeUTF8))

