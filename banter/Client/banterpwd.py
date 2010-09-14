# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banterpwd.ui'
#
# Created: Tue Sep 14 15:15:59 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_banterpwd(object):
    def setupUi(self, banterpwd):
        banterpwd.setObjectName("banterpwd")
        banterpwd.resize(591, 394)
        self.centralwidget = QtGui.QWidget(banterpwd)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 101, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 160, 631, 31))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 0, 131, 31))
        self.label.setObjectName("label")
        self.username = QtGui.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(310, 0, 181, 31))
        self.username.setObjectName("username")
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 220, 631, 31))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pwd = QtGui.QLineEdit(self.frame_2)
        self.pwd.setGeometry(QtCore.QRect(310, 0, 181, 31))
        self.pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 0, 171, 31))
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 280, 631, 31))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(50, 0, 151, 31))
        self.label_4.setObjectName("label_4")
        self.cpwd = QtGui.QLineEdit(self.frame_3)
        self.cpwd.setGeometry(QtCore.QRect(310, 0, 181, 31))
        self.cpwd.setEchoMode(QtGui.QLineEdit.Password)
        self.cpwd.setObjectName("cpwd")
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(250, 330, 93, 27))
        self.submit.setObjectName("submit")
        banterpwd.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(banterpwd)
        self.statusbar.setObjectName("statusbar")
        banterpwd.setStatusBar(self.statusbar)

        self.retranslateUi(banterpwd)
        QtCore.QObject.connect(self.submit, QtCore.SIGNAL("clicked(bool)"), banterpwd.update)
        QtCore.QObject.connect(self.submit, QtCore.SIGNAL("clicked()"), banterpwd.close)
        QtCore.QObject.connect(self.cpwd, QtCore.SIGNAL("textChanged(QString)"), self.submit.show)
        QtCore.QMetaObject.connectSlotsByName(banterpwd)

    def retranslateUi(self, banterpwd):
        banterpwd.setWindowTitle(QtGui.QApplication.translate("banterpwd", "banterpwd", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("banterpwd", " User name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("banterpwd", "Enter new password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("banterpwd", "Confirm new password:", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("banterpwd", "submit", None, QtGui.QApplication.UnicodeUTF8))

