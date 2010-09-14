import banter1,banter2,banter3,banter4,bantersignup,banterpwd,dialog1
from PyQt4 import QtGui,QtCore
import sys
user=""
pwd=""
u=""
pwd1=""
cpwd1=""
def signin():
	user=obj1.userentry.text()
	print user
	pwd=obj1.pwdentry.text()
	print pwd
	window2.show()
	#not matching
	Dial.show()
	print "MMM"
	t=0
	icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Desktop/nn/im-yahoo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	item = QtGui.QListWidgetItem(obj2.list)
        item.setIcon(icon)
	item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
	obj2.list.item(t).setText(QtGui.QApplication.translate("Mbanter2","krish",None, QtGui.QApplication.UnicodeUTF8))
	t=t+1
def forgetpwd():
	#global u,pwd1,cpwd1
	window6.show()
	obj6.submit.hide()
	'''u=obj6.username.text()
	pwd1=obj6.pwd.text()
	cpwd1=obj6.cpwd.text()
	print u + "hi"'''

	

def signup():
	window5.show()
	obj5.submitup.setEnabled(False)

def submitup():
	firstn=obj5.firstname.text()
	lastn=obj5.lastname.text()
	u=obj5.uname.text()
	pwd1=obj5.pswwd.text()
	cpwd1=obj5.cpswwd.text()
	if(firstn!='' and lastn!='' and u!='' and pwd1!='' and cpwd1!=''):
		obj5.submitup.setEnabled(True)
	else:
		obj5.submitup.setEnabled(False)
   
def submit():
	
	u=obj6.username.text()
	pwd1=obj6.pwd.text()
	cpwd1=obj6.cpwd.text()
	if(u!='' and pwd1!='' and cpwd1!=''):
		obj6.submit.setEnabled(True)
	else:
		obj6.submit.setEnabled(False)
	print "kkkrrr"
	#print pwd1
#	print cpwd1
	#window1.show()

def invitebox():
	window3.show()
	obj3.send.hide()

def chatwindow():
	window4.show()
		
	
app = QtGui.QApplication(sys.argv)

window1 = QtGui.QMainWindow()
obj1 = banter1.Ui_MainWindow()
obj1.setupUi(window1)

window2 = QtGui.QMainWindow()
obj2 = banter2.Ui_Mbanter2()
obj2.setupUi(window2)

window3 = QtGui.QMainWindow()
obj3 = banter3.Ui_Mbanter3()
obj3.setupUi(window3)

window4 = QtGui.QMainWindow()
obj4 = banter4.Ui_Mbanter4()
obj4.setupUi(window4)

window5 = QtGui.QMainWindow()
obj5 = bantersignup.Ui_bantersignup()
obj5.setupUi(window5)


window6=QtGui.QMainWindow()
obj6 = banterpwd.Ui_banterpwd()
obj6.setupUi(window6)



Dial=QtGui.QDialog()
dia1=dialog1.Ui_Dialog()
dia1.setupUi(Dial)
window1.show()

QtCore.QObject.connect(obj1.signin, QtCore.SIGNAL("clicked()"),signin)
QtCore.QObject.connect(obj1.signup, QtCore.SIGNAL("clicked()"),signup)
QtCore.QObject.connect(obj1.forgetid, QtCore.SIGNAL("clicked()"),forgetpwd)
#QtCore.QObject.connect(obj6.submit, QtCore.SIGNAL("clicked()"),submit)
QtCore.QObject.connect(obj6.cpwd, QtCore.SIGNAL("returnPressed()"),submit)

QtCore.QObject.connect(obj5.cpswwd, QtCore.SIGNAL("returnPressed()"),submitup)

QtCore.QObject.connect(obj2.invite, QtCore.SIGNAL("clicked()"),invitebox)
#QtCore.QObject.connect(obj3.add, QtCore.SIGNAL("textEdited()"),invite)
QtCore.QObject.connect(obj2.list, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"),chatwindow)









sys.exit(app.exec_())
