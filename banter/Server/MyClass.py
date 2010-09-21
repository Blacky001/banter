from PyQt4 import QtCore, QtGui,Qt
class MyLineEdit(QtGui.QLineEdit):
    def __init__(self, *args):
    	
        QtGui.QLineEdit.__init__(self, *args)
        
    def event(self, event):
    	
        '''if (event.type()==QtCore.QEvent.KeyPress):
            if(event.key() in range(48,57) ):
            	print  event.key()
            	return QtGui.QLineEdit.event(self, event)
            else:
            	return True'''
       
	if (event.type()==QtCore.QEvent.FocusIn):
		
		
		self.emit(QtCore.SIGNAL("FocusIn(String)"),self.objectName().__str__().__str__())
		print "release"
		return QtGui.QLineEdit.event(self,event)
    	return QtGui.QLineEdit.event(self, event)
    
