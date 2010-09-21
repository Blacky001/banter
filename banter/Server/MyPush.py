from PyQt4 import QtCore, QtGui,Qt
class MypushButton(QtGui.QPushButton):
    def __init__(self, *args):
    	
        QtGui.QPushButton.__init__(self, *args)
        
    def event(self, event):
    	
        '''if (event.type()==QtCore.QEvent.KeyPress):
            if(event.key() in range(48,57) ):
            	print  event.key()
            	return QtGui.QPushButton.event(self, event)
            else:
            	return True'''
       
	if (event.type()==QtCore.QEvent.MouseButtonRelease):
		
		
		self.emit(QtCore.SIGNAL("release(String)"),self.objectName().__str__().__str__())
		print type(self.objectName().__str__().__str__())
		print "release"
		return QtGui.QPushButton.event(self,event)
    	return QtGui.QPushButton.event(self, event)
    
