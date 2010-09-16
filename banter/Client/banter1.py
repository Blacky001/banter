# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter1.ui'
#
# Created: Thu Sep 16 17:27:15 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 359)
        MainWindow.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signin = QtGui.QPushButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(160, 190, 93, 27))
        self.signin.setObjectName("signin")
        self.signup = QtGui.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(340, 20, 93, 27))
        self.signup.setObjectName("signup")
        self.userentry = QtGui.QLineEdit(self.centralwidget)
        self.userentry.setGeometry(QtCore.QRect(140, 110, 191, 27))
        self.userentry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userentry.setEchoMode(QtGui.QLineEdit.Normal)
        self.userentry.setObjectName("userentry")
        self.pwdentry = QtGui.QLineEdit(self.centralwidget)
        self.pwdentry.setGeometry(QtCore.QRect(140, 150, 191, 27))
        self.pwdentry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pwdentry.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdentry.setObjectName("pwdentry")
        self.forgetid = QtGui.QRadioButton(self.centralwidget)
        self.forgetid.setGeometry(QtCore.QRect(260, 190, 171, 22))
        self.forgetid.setObjectName("forgetid")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 110, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 71, 17))
        self.label_2.setObjectName("label_2")
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
        self.forgetid.setText(QtGui.QApplication.translate("MainWindow", "forgot your password?", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "user name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "password", None, QtGui.QApplication.UnicodeUTF8))

