# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter2.ui'
#
# Created: Tue Sep 14 15:37:48 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Mbanter2(object):
    def setupUi(self, Mbanter2):
        Mbanter2.setObjectName("Mbanter2")
        Mbanter2.resize(332, 600)
        Mbanter2.setStyleSheet("background-color: rgb(255, 222, 197);\n"
"background-color: rgb(236, 218, 180);")
        self.centralwidget = QtGui.QWidget(Mbanter2)
        self.centralwidget.setObjectName("centralwidget")
        self.list = QtGui.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(40, 90, 261, 461))
        self.list.setStyleSheet("background-color: rgb(236, 218, 180);\n"
"background-color: rgb(255, 255, 255);")
        self.list.setObjectName("list")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 501, 31))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.status = QtGui.QComboBox(self.frame)
        self.status.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.status.setStyleSheet("selection-background-color: rgb(255, 249, 201);\n"
"")
        self.status.setObjectName("status")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Desktop/nn/im-yahoo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Desktop/nn/gdu-smart-healthy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Desktop/nn/media-record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Desktop/nn/gdu-smart-threshold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status.addItem(icon3, "")
        self.signout = QtGui.QPushButton(self.frame)
        self.signout.setGeometry(QtCore.QRect(240, 0, 93, 31))
        self.signout.setObjectName("signout")
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 30, 491, 21))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.invite = QtGui.QPushButton(self.frame_2)
        self.invite.setGeometry(QtCore.QRect(60, 0, 211, 21))
        self.invite.setObjectName("invite")
        Mbanter2.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Mbanter2)
        self.statusbar.setObjectName("statusbar")
        Mbanter2.setStatusBar(self.statusbar)
        self.actionVoice_chat = QtGui.QAction(Mbanter2)
        self.actionVoice_chat.setObjectName("actionVoice_chat")
        self.actionSing_out = QtGui.QAction(Mbanter2)
        self.actionSing_out.setObjectName("actionSing_out")
        self.actionClose = QtGui.QAction(Mbanter2)
        self.actionClose.setObjectName("actionClose")
        self.actionCut = QtGui.QAction(Mbanter2)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(Mbanter2)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(Mbanter2)
        self.actionPaste.setObjectName("actionPaste")

        self.retranslateUi(Mbanter2)
        QtCore.QObject.connect(self.signout, QtCore.SIGNAL("clicked()"), Mbanter2.close)
        QtCore.QObject.connect(self.invite, QtCore.SIGNAL("clicked()"), Mbanter2.update)
        QtCore.QMetaObject.connectSlotsByName(Mbanter2)

    def retranslateUi(self, Mbanter2):
        Mbanter2.setWindowTitle(QtGui.QApplication.translate("Mbanter2", "banter2", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setItemText(0, QtGui.QApplication.translate("Mbanter2", "status", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setItemText(1, QtGui.QApplication.translate("Mbanter2", "available", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setItemText(2, QtGui.QApplication.translate("Mbanter2", "busy", None, QtGui.QApplication.UnicodeUTF8))
        self.status.setItemText(3, QtGui.QApplication.translate("Mbanter2", "idle", None, QtGui.QApplication.UnicodeUTF8))
        self.signout.setText(QtGui.QApplication.translate("Mbanter2", "signout", None, QtGui.QApplication.UnicodeUTF8))
        self.invite.setText(QtGui.QApplication.translate("Mbanter2", "invite a friend", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVoice_chat.setText(QtGui.QApplication.translate("Mbanter2", "voice chat", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSing_out.setText(QtGui.QApplication.translate("Mbanter2", "sign out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("Mbanter2", "close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("Mbanter2", "cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("Mbanter2", "copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("Mbanter2", "paste", None, QtGui.QApplication.UnicodeUTF8))

