# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter1.ui'
#
# Created: Tue Sep 14 15:14:02 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(608, 421)
        MainWindow.setStyleSheet("background-color: rgb(236, 218, 180);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signin = QtGui.QPushButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(220, 280, 93, 27))
        self.signin.setObjectName("signin")
        self.signup = QtGui.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(220, 320, 93, 27))
        self.signup.setObjectName("signup")
        self.userentry = QtGui.QLineEdit(self.centralwidget)
        self.userentry.setGeometry(QtCore.QRect(170, 150, 271, 27))
        self.userentry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userentry.setEchoMode(QtGui.QLineEdit.Normal)
        self.userentry.setObjectName("userentry")
        self.pwdentry = QtGui.QLineEdit(self.centralwidget)
        self.pwdentry.setGeometry(QtCore.QRect(170, 190, 271, 27))
        self.pwdentry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pwdentry.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdentry.setObjectName("pwdentry")
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(70, 150, 81, 27))
        self.username.setObjectName("username")
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(70, 190, 81, 27))
        self.password.setObjectName("password")
        self.forgetid = QtGui.QRadioButton(self.centralwidget)
        self.forgetid.setGeometry(QtCore.QRect(190, 240, 161, 22))
        self.forgetid.setObjectName("forgetid")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.signin, QtCore.SIGNAL("clicked()"), MainWindow.update)
        QtCore.QObject.connect(self.forgetid, QtCore.SIGNAL("clicked()"), MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "banter1", None, QtGui.QApplication.UnicodeUTF8))
        self.signin.setText(QtGui.QApplication.translate("MainWindow", "sign in", None, QtGui.QApplication.UnicodeUTF8))
        self.signup.setText(QtGui.QApplication.translate("MainWindow", "sign up", None, QtGui.QApplication.UnicodeUTF8))
        self.username.setText(QtGui.QApplication.translate("MainWindow", "username", None, QtGui.QApplication.UnicodeUTF8))
        self.password.setText(QtGui.QApplication.translate("MainWindow", "password", None, QtGui.QApplication.UnicodeUTF8))
        self.forgetid.setText(QtGui.QApplication.translate("MainWindow", "forgot your password?", None, QtGui.QApplication.UnicodeUTF8))

