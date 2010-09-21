import server,details,message,start,message1
from PyQt4 import QtGui,QtCore
import sys,os,icon_rc
from MyClass import *
from MyPush import *
dtls={}
Detail={}
Message1={}
msg1={}
current_user=""
class det():
	def __init__(self):
		self.name1="divya"
		self.password="current_user"
		self.cldrtn="99:34:12"
		self.lstcldrtn="12:23"
		self.lstclr="ajay"
		self.ip="192.168.1.5"
		self.port="3000"

def start1():
	Start.show()
def connect():
	window.show()
	ip=strt.lineEdit.text()
	port_no=strt.lineEdit_2.text()
	print ip,port_no
	for i in range(0,9):
		users(i)
	item = QtGui.QListWidgetItem(main.listWidget_2)
	main.listWidget_2.item(0).setText(QtGui.QApplication.translate("MainWindow","server ip-"+ip+"\nport-"+port_no,None, QtGui.QApplication.UnicodeUTF8))
	Start.close()
	main.menuUsers.setEnabled(True)
	main.menuCall_history.setEnabled(True)
	main.menuCall_duration.setEnabled(True)
	main.pushButton.setEnabled(True)
	main.actionRestart.setEnabled(True)
	main.actionStart.setEnabled(False)
def restart():
	stop()
	Start.show()
def stop():
	window.close()

def search():
	t=0
	while main.listWidget.count()>t:
		if main.lineEdit.text()==main.listWidget.item(t).text():
			main.listWidget.findItems(main.lineEdit.text(),QtCore.Qt.MatchExactly)[0].setSelected(True)
			display()
			return
		t=t+1
	print "no such user"

def display(a):	
	nam=a.text()
	Detail[a]=QtGui.QDialog()
	dtls[a]=details.Ui_Dialog()
	dtls[a].setupUi(Detail[a])
	dtls[a].textBrowser.setText(a.text())
	dtls[a].textBrowser_2.setText(name.password)
	dtls[a].textBrowser_3.setText(name.cldrtn)
	dtls[a].textBrowser_4.setText(name.lstcldrtn)
	dtls[a].textBrowser_5.setText(name.lstclr)
	dtls[a].textBrowser_6.setText(name.ip)
	dtls[a].textBrowser_7.setText(name.port)
        dtls[a].pushButton = MypushButton(Detail[a])
        dtls[a].pushButton.setGeometry(QtCore.QRect(160, 370, 161, 31))
        dtls[a].pushButton.setStyleSheet("""background-color: rgb(141, 141, 106);background-color: rgb(117, 127, 135);""")
	dtls[a].pushButton.setObjectName(nam)	
	dtls[a].pushButton.setText("send message")
	QtCore.QObject.connect(dtls[a].pushButton, QtCore.SIGNAL("release(String)"),sendtosingle)
	Detail[a].show()
	
def select(item):
	a=msg.lineEdit.text()
	msg.lineEdit.setText(a+item.text()+",")
def sendmessage():
	Message.show()
	QtCore.QObject.connect(main.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),select)
	QtCore.QObject.disconnect(main.listWidget, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),display)
def sendbutton():
	msg.textEdit.setText(msg.textEdit.toPlainText()+"\nserver:"+msg.lineEdit_2.text())
	print "to-"+msg.lineEdit.text()
	print "message"+msg.lineEdit_2.text()
	msg.lineEdit_2.setText("")
def chat(nam):
	global current_user
	current_user=nam
	print "in my class "+nam
	QtCore.QObject.connect(msg1[nam].pushButton_2, QtCore.SIGNAL("clicked()"), discard1)
	QtCore.QObject.connect(msg1[nam].pushButton, QtCore.SIGNAL("clicked()"), sendbutton1)
def sendbutton1():
	global current_user
	msg1[current_user].textEdit.setText(msg1[current_user].textEdit.toPlainText()+"\nserver:"+msg1[current_user].lineEdit_2.text())
	QtCore.QObject.disconnect(msg1[current_user].pushButton_2, QtCore.SIGNAL("clicked()"), discard1)
	QtCore.QObject.disconnect(msg1[current_user].pushButton, QtCore.SIGNAL("clicked()"), sendbutton1)
def discard1():
	global current_user
	msg1[current_user].textEdit.setText("")
	msg1[current_user].lineEdit.setText("")
	msg1[current_user].lineEdit_2.setText("type here")
	Message1[current_user].close()
def sendtosingle(nam):
	Message1[nam]=QtGui.QDialog()
	msg1[nam]=message.Ui_Dialog()
	msg1[nam].setupUi(Message1[nam])
	msg1[nam].lineEdit.setText(nam+",")
  	msg1[nam].lineEdit_2 = MyLineEdit(Message1[nam])
        msg1[nam].lineEdit_2.setGeometry(QtCore.QRect(0, 270, 401, 41))
        msg1[nam].lineEdit_2.setStyleSheet("background-color: rgb(220, 225, 255);")
        msg1[nam].lineEdit_2.setObjectName(nam)
	Message1[nam].show()
	QtCore.QObject.connect(msg1[nam].lineEdit_2, QtCore.SIGNAL("FocusIn(String)"), chat)

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
	if main.listWidget.item(i).text()!="":
		item.setIcon(icon)


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
main = server.Ui_MainWindow()
main.setupUi(window)
window.show()
Start=QtGui.QDialog()
strt=start.Ui_Dialog()
strt.setupUi(Start)
Message=QtGui.QDialog()
msg=message1.Ui_Dialog()
msg.setupUi(Message)
name=det()




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
QtCore.QObject.connect(strt.pushButton, QtCore.SIGNAL("clicked()"),connect)
QtCore.QObject.connect(Message, QtCore.SIGNAL("rejected()"),discard)
sys.exit(app.exec_())
