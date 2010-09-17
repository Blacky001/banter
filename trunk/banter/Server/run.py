import server,details,message,start
from PyQt4 import QtGui,QtCore
import sys,os,icon_rc
class det():
	def __init__(self):
		self.name1=raw_input()
		self.password=raw_input()
		self.cldrtn=raw_input()
		self.lstcldrtn=raw_input()
		self.lstclr=raw_input()
def start1():
	print "start"
	ip=strt.lineEdit.text()
	port_no=strt.lineEdit_2.text()
	print ip,port_no
	window.show()
	Start.close()
def restart():
	print "restart"
def stop():
	window.close()
	Message.close()
	Detail.close()
	print "stop"
def search():
	t=0
	while main.listWidget.count()>t:
		if main.lineEdit.text()==main.listWidget.item(t).text():
			main.listWidget.findItems(main.lineEdit.text(),QtCore.Qt.MatchExactly)[0].setSelected(True)
			display()
			return
		t=t+1
	print "no such user"

def display():	
	Detail.show()
	dtls.textBrowser.setText(name.name1)
	dtls.textBrowser_2.setText(name.password)
	dtls.textBrowser_3.setText(name.cldrtn)
	dtls.textBrowser_4.setText(name.lstcldrtn)
	dtls.textBrowser_5.setText(name.lstclr)
def select(item):
	msg.lineEdit.setText(msg.lineEdit.text()+item.text()+",")
def sendmessage():
	Message.show()
	QtCore.QObject.connect(main.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),select)
	QtCore.QObject.disconnect(main.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),display)
def sendbutton():
	msg.textEdit.setText(msg.textEdit.toPlainText()+"\nserver:"+msg.lineEdit_2.text())
	print "to-"+msg.lineEdit.text()
	print "message"+msg.lineEdit_2.text()
	msg.lineEdit_2.setText("")

def sendtosingle():
	sendmessage()
	msg.lineEdit.setText(name.name1+",")
	
def discard():
	QtCore.QObject.disconnect(main.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),select)
	QtCore.QObject.connect(main.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),display)
	msg.textEdit.setText("")
	msg.lineEdit.setText("")
	msg.lineEdit_2.setText("type here")
	Message.close()
def users(i):
	A={}
	A=['ajay','divya','vijesh','swami','sangitha','krishna','shyja','noble','dhanya']
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap(":/newPrefix/banter/gdu-smart-failing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	item = QtGui.QListWidgetItem(main.listWidget)
	item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
	main.listWidget.item(i).setText(QtGui.QApplication.translate("MainWindow",A[i],None, QtGui.QApplication.UnicodeUTF8))
	item.setIcon(icon)

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
main = server.Ui_MainWindow()
main.setupUi(window)
Start=QtGui.QDialog()
strt=start.Ui_Dialog()
strt.setupUi(Start)
Start.show()
Detail=QtGui.QDialog()
dtls=details.Ui_Dialog()
dtls.setupUi(Detail)
Message=QtGui.QDialog()
msg=message.Ui_Dialog()
msg.setupUi(Message)
print "enter"
name=det()
print "stop"
for i in range(0,9):
	users(i)
item = QtGui.QListWidgetItem(main.listWidget_2)
main.listWidget_2.item(0).setText(QtGui.QApplication.translate("MainWindow","divya calling ajay",None, QtGui.QApplication.UnicodeUTF8))


QtCore.QObject.connect(main.pushButton, QtCore.SIGNAL("clicked()"), search)
QtCore.QObject.connect(main.actionTotal_call_duration, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(main.actionLast_call_duration, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(main.actionCurrently_logged_in_3, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(main.actionSend_message_to, QtCore.SIGNAL("triggered()"),sendmessage)
QtCore.QObject.connect(main.actionCall_History, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(main.actionStart, QtCore.SIGNAL("triggered()"),start1)
QtCore.QObject.connect(main.actionRestart, QtCore.SIGNAL("triggered()"),restart)
QtCore.QObject.connect(main.actionStop, QtCore.SIGNAL("triggered()"),stop)
QtCore.QObject.connect(main.actionPresently_connected, QtCore.SIGNAL("triggered()"),display)
QtCore.QObject.connect(main.lineEdit, QtCore.SIGNAL("returnPressed()"),search)
QtCore.QObject.connect(main.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),display)
QtCore.QObject.connect(msg.pushButton, QtCore.SIGNAL("clicked()"), sendbutton)
QtCore.QObject.connect(msg.pushButton_2, QtCore.SIGNAL("clicked()"), discard)
QtCore.QObject.connect(dtls.pushButton, QtCore.SIGNAL("clicked()"),sendtosingle)
QtCore.QObject.connect(msg.lineEdit_2, QtCore.SIGNAL("returnPressed()"),sendbutton)
QtCore.QObject.connect(strt.pushButton, QtCore.SIGNAL("clicked()"),start1)
sys.exit(app.exec_())
