# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter4.ui'
#
# Created: Tue Sep 14 15:20:07 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Mbanter4(object):
    def setupUi(self, Mbanter4):
        Mbanter4.setObjectName("Mbanter4")
        Mbanter4.resize(399, 308)
        Mbanter4.setStyleSheet("background-color: rgb(236, 218, 180);")
        self.centralwidget = QtGui.QWidget(Mbanter4)
        self.centralwidget.setObjectName("centralwidget")
        self.chatwindow = QtGui.QTextEdit(self.centralwidget)
        self.chatwindow.setGeometry(QtCore.QRect(20, 10, 341, 161))
        self.chatwindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.chatwindow.setObjectName("chatwindow")
        self.userwindow = QtGui.QTextEdit(self.centralwidget)
        self.userwindow.setGeometry(QtCore.QRect(50, 180, 281, 84))
        self.userwindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userwindow.setObjectName("userwindow")
        Mbanter4.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Mbanter4)
        self.statusbar.setObjectName("statusbar")
        Mbanter4.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(Mbanter4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
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
        self.menuFile.addAction(self.actionVoice_call)
        self.menuFile.addAction(self.actionCut_call)
        self.menuFile.addAction(self.actionCall_duration)
        self.menuFile.addAction(self.actionChat_history)
        self.menuEdit.addAction(self.actionCut_2)
        self.menuEdit.addAction(self.actionCopy_2)
        self.menuEdit.addAction(self.actionPaste_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(Mbanter4)
        QtCore.QMetaObject.connectSlotsByName(Mbanter4)

    def retranslateUi(self, Mbanter4):
        Mbanter4.setWindowTitle(QtGui.QApplication.translate("Mbanter4", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Mbanter4", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Mbanter4", "edit", None, QtGui.QApplication.UnicodeUTF8))
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

