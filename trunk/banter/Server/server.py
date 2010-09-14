# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'banter/server.ui'
#
# Created: Tue Sep 14 13:25:59 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 529)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 113, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 0, 51, 31))
        self.pushButton.setStyleSheet("border-color: rgb(170, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 30, 161, 451))
        self.listWidget.setStyleSheet("background-color: rgb(240, 220, 190);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 0, 431, 481))
        self.listWidget_2.setStyleSheet("background-color: rgb(236, 218, 180);")
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 25))
        self.menubar.setObjectName("menubar")
        self.menuUsers = QtGui.QMenu(self.menubar)
        self.menuUsers.setObjectName("menuUsers")
        self.menuCall_history = QtGui.QMenu(self.menubar)
        self.menuCall_history.setObjectName("menuCall_history")
        self.menuCall_duration = QtGui.QMenu(self.menubar)
        self.menuCall_duration.setObjectName("menuCall_duration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCurrently_logged_in = QtGui.QAction(MainWindow)
        self.actionCurrently_logged_in.setObjectName("actionCurrently_logged_in")
        self.actionSas = QtGui.QAction(MainWindow)
        self.actionSas.setObjectName("actionSas")
        self.actionCurrently_logged_in_3 = QtGui.QAction(MainWindow)
        self.actionCurrently_logged_in_3.setObjectName("actionCurrently_logged_in_3")
        self.actionLast_call_duration = QtGui.QAction(MainWindow)
        self.actionLast_call_duration.setObjectName("actionLast_call_duration")
        self.actionTotal_call_duration = QtGui.QAction(MainWindow)
        self.actionTotal_call_duration.setObjectName("actionTotal_call_duration")
        self.actionPresently_connected = QtGui.QAction(MainWindow)
        self.actionPresently_connected.setObjectName("actionPresently_connected")
        self.actionCall_History = QtGui.QAction(MainWindow)
        self.actionCall_History.setObjectName("actionCall_History")
        self.menuUsers.addSeparator()
        self.menuUsers.addAction(self.actionCurrently_logged_in_3)
        self.menuCall_history.addAction(self.actionPresently_connected)
        self.menuCall_history.addAction(self.actionCall_History)
        self.menuCall_duration.addAction(self.actionLast_call_duration)
        self.menuCall_duration.addAction(self.actionTotal_call_duration)
        self.menubar.addAction(self.menuUsers.menuAction())
        self.menubar.addAction(self.menuCall_history.menuAction())
        self.menubar.addAction(self.menuCall_duration.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUsers.setTitle(QtGui.QApplication.translate("MainWindow", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCall_history.setTitle(QtGui.QApplication.translate("MainWindow", "Calls", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCall_duration.setTitle(QtGui.QApplication.translate("MainWindow", "Call duration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCurrently_logged_in.setText(QtGui.QApplication.translate("MainWindow", "currently logged in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSas.setText(QtGui.QApplication.translate("MainWindow", "sas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCurrently_logged_in_3.setText(QtGui.QApplication.translate("MainWindow", "Currently logged in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLast_call_duration.setText(QtGui.QApplication.translate("MainWindow", "Last call duration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTotal_call_duration.setText(QtGui.QApplication.translate("MainWindow", "Total call duration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPresently_connected.setText(QtGui.QApplication.translate("MainWindow", "presently connected", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCall_History.setText(QtGui.QApplication.translate("MainWindow", "Call History", None, QtGui.QApplication.UnicodeUTF8))

