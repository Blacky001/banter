import server,details
from PyQt4 import QtGui,QtCore
import sys,os,icon_rc
class det():
	def __init__(self):
		self.name1=raw_input()
		self.password=raw_input()
		self.cldrtn=raw_input()
		self.lstcldrtn=raw_input()
		self.lstclr=raw_input()
def search():
	t=0
	while obj.listWidget.count()>t:
		if obj.lineEdit.text()==obj.listWidget.item(t).text():
			obj.listWidget.findItems(obj.lineEdit.text(),QtCore.Qt.MatchExactly)[0].setSelected(True)
			display()
			return
		t=t+1
	print "no such user"

def display():	
	Detail.show()
	obj1.textBrowser.setText(name.name1)
	obj1.textBrowser_2.setText(name.password)
	obj1.textBrowser_3.setText(name.cldrtn)
	obj1.textBrowser_4.setText(name.lstcldrtn)
	obj1.textBrowser_5.setText(name.lstclr)
def users(i):
	A={}
	A=['ajay','divya','vijesh','swami','sangitha','krishna','shyja','noble','dhanya']
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap(":/newPrefix/banter/gdu-smart-failing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	item = QtGui.QListWidgetItem(obj.listWidget)
	item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
	obj.listWidget.item(i).setText(QtGui.QApplication.translate("MainWindow",A[i],None, QtGui.QApplication.UnicodeUTF8))
	item.setIcon(icon)

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
obj = server.Ui_MainWindow()
obj.setupUi(window)
window.show()
Detail=QtGui.QDialog()
obj1=details.Ui_Dialog()
obj1.setupUi(Detail)
print "enter"
name=det()
print "stop"
for i in range(0,9):
	users(i)
item = QtGui.QListWidgetItem(obj.listWidget_2)
obj.listWidget_2.item(0).setText(QtGui.QApplication.translate("MainWindow","divya calling ajay",None, QtGui.QApplication.UnicodeUTF8))



QtCore.QObject.connect(obj.pushButton, QtCore.SIGNAL("clicked()"), search)
QtCore.QObject.connect(obj.actionTotal_call_duration, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(obj.actionLast_call_duration, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(obj.actionCurrently_logged_in_3, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(obj.actionCall_History, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(obj.actionPresently_connected, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(obj.lineEdit, QtCore.SIGNAL("returnPressed()"),search)
QtCore.QObject.connect(obj.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),display)
sys.exit(app.exec_())
