# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter4.ui'
#
# Created: Fri Sep 17 14:51:38 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Mbanter4(object):
    def setupUi(self, Mbanter4):
        Mbanter4.setObjectName("Mbanter4")
        Mbanter4.resize(418, 321)
        Mbanter4.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.centralwidget = QtGui.QWidget(Mbanter4)
        self.centralwidget.setObjectName("centralwidget")
        self.chatwindow = QtGui.QTextEdit(self.centralwidget)
        self.chatwindow.setGeometry(QtCore.QRect(40, 30, 341, 161))
        self.chatwindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.chatwindow.setObjectName("chatwindow")
        self.userwindow = QtGui.QTextEdit(self.centralwidget)
        self.userwindow.setGeometry(QtCore.QRect(70, 200, 281, 84))
        self.userwindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userwindow.setObjectName("userwindow")
        self.person = QtGui.QLabel(self.centralwidget)
        self.person.setGeometry(QtCore.QRect(300, 10, 81, 21))
        self.person.setText("")
        self.person.setObjectName("person")
        Mbanter4.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Mbanter4)
        self.statusbar.setObjectName("statusbar")
        Mbanter4.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(Mbanter4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 25))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Mbanter4.setMenuBar(self.menubar)
        self.actionCut = QtGui.QAction(Mbanter4)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(Mbanter4)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(Mbanter4)
        self.actionPaste.setObjectName("actionPaste")
        self.actionVoice_chat = QtGui.QAction(Mbanter4)
        self.actionVoice_chat.setObjectName("actionVoice_chat")
        self.actionCut_2 = QtGui.QAction(Mbanter4)
        self.actionCut_2.setObjectName("actionCut_2")
        self.actionCopy_2 = QtGui.QAction(Mbanter4)
        self.actionCopy_2.setObjectName("actionCopy_2")
        self.actionPaste_2 = QtGui.QAction(Mbanter4)
        self.actionPaste_2.setObjectName("actionPaste_2")
        self.actionVoice_call = QtGui.QAction(Mbanter4)
        self.actionVoice_call.setObjectName("actionVoice_call")
        self.actionCut_call = QtGui.QAction(Mbanter4)
        self.actionCut_call.setObjectName("actionCut_call")
        self.actionCall_duration = QtGui.QAction(Mbanter4)
        self.actionCall_duration.setObjectName("actionCall_duration")
        self.actionChat_history = QtGui.QAction(Mbanter4)
        self.actionChat_history.setObjectName("actionChat_history")
        self.menuEdit.addAction(self.actionCut_2)
        self.menuEdit.addAction(self.actionCopy_2)
        self.menuEdit.addAction(self.actionPaste_2)
        self.menuFile.addAction(self.actionVoice_call)
        self.menuFile.addAction(self.actionCut_call)
        self.menuFile.addAction(self.actionCall_duration)
        self.menuFile.addAction(self.actionChat_history)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(Mbanter4)
        QtCore.QMetaObject.connectSlotsByName(Mbanter4)

    def retranslateUi(self, Mbanter4):
        Mbanter4.setWindowTitle(QtGui.QApplication.translate("Mbanter4", "Mbanter4", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Mbanter4", "edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Mbanter4", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("Mbanter4", "cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("Mbanter4", "copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("Mbanter4", "paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVoice_chat.setText(QtGui.QApplication.translate("Mbanter4", "voice chat", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut_2.setText(QtGui.QApplication.translate("Mbanter4", "cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy_2.setText(QtGui.QApplication.translate("Mbanter4", "copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste_2.setText(QtGui.QApplication.translate("Mbanter4", "paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVoice_call.setText(QtGui.QApplication.translate("Mbanter4", "voice call", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut_call.setText(QtGui.QApplication.translate("Mbanter4", "cut call", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCall_duration.setText(QtGui.QApplication.translate("Mbanter4", "call duration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChat_history.setText(QtGui.QApplication.translate("Mbanter4", "chat history", None, QtGui.QApplication.UnicodeUTF8))
