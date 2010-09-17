# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter1.ui'
#
# Created: Fri Sep 17 12:38:58 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 307)
        MainWindow.setStyleSheet("background-color: rgb(90, 45, 67);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userentry = QtGui.QLineEdit(self.centralwidget)
        self.userentry.setGeometry(QtCore.QRect(230, 120, 191, 27))
        self.userentry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userentry.setEchoMode(QtGui.QLineEdit.Normal)
        self.userentry.setObjectName("userentry")
        self.pwdentry = QtGui.QLineEdit(self.centralwidget)
        self.pwdentry.setGeometry(QtCore.QRect(230, 180, 191, 27))
        self.pwdentry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pwdentry.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdentry.setObjectName("pwdentry")
        self.forgetid = QtGui.QRadioButton(self.centralwidget)
        self.forgetid.setGeometry(QtCore.QRect(240, 220, 171, 22))
        self.forgetid.setStyleSheet("color: rgb(0, 0, 0);")
        self.forgetid.setObjectName("forgetid")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 100, 71, 20))
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 160, 71, 17))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.signup = QtGui.QCommandLinkButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(330, 20, 101, 41))
        self.signup.setStyleSheet("color: rgb(255, 170, 127);")
        self.signup.setObjectName("signup")
        self.signin = QtGui.QCommandLinkButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(330, 250, 91, 41))
        self.signin.setStyleSheet("color: rgb(255, 170, 127);")
        self.signin.setObjectName("signin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.forgetid, QtCore.SIGNAL("clicked()"), MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "banter1", None, QtGui.QApplication.UnicodeUTF8))
        self.forgetid.setText(QtGui.QApplication.translate("MainWindow", "forgot your password?", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "user name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.signup.setText(QtGui.QApplication.translate("MainWindow", "sign up", None, QtGui.QApplication.UnicodeUTF8))
        self.signin.setText(QtGui.QApplication.translate("MainWindow", "sign in", None, QtGui.QApplication.UnicodeUTF8))

