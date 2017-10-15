#Python GUI tool to Synchronize Subtitles files srt and ass
#coded by MGF15
#my first Qt :P 
import sys,re,datetime
from PyQt4 import QtCore, QtGui

from sync import Ui_MainWindow
from about import Ui_about

class about(QtGui.QMainWindow):


	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
	
		self.ui = Ui_about()
		self.ui.setupUi(self)

class MyForm(QtGui.QMainWindow):


	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
	
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton_2.clicked.connect(self.getfile)
		self.ui.pushButton_3.clicked.connect(self.savefile)
		self.ui.pushButton.clicked.connect(self.n_sync)
		self.ui.pushButton_4.clicked.connect(self.about)
		self.dialog = about(self)

	fname = None
	sname = None

	def about(self):
		self.dialog.show()

	def edittime(self,reg,new_time):

		if reg == "srt":
			c = str(new_time)
			new = '0'+c+',000' if len(c) < 14 else '0'+c.replace('.',',')[:-3]
		elif reg == "ass" :
			c = str(new_time)
			new = c+'.00' if len(c) < 14 else c[:-4]
		return new

	def sync(self,subfile,sub):

		bom = subfile[:2] 
		#check if the file encoded in utf-16 
		utf16 = True if bom[:2] == '\xff\xfe' else False

		if sub == "srt":
			u = 1 # 10 if .ass 1 if .srt
			rex = r"\d+:\d+:\d+,\d+"
			rex2 = r"(\d+):(\d+):(\d+),(\d+)"
		elif sub == "ass":
			u = 10 # 10 if .ass 1 if .srt
			rex = r"\d:\d+:\d+.\d+"
			rex2 = r"(\d):(\d+):(\d+).(\d+)"

		if utf16 == True :
			subfile = subfile.decode('utf-16')

		f = re.findall(rex,subfile)

		for i in f:
	
			f_time = re.findall(rex2,i)[0]
			time = map(int,f_time)
			
			new_time = datetime.timedelta(hours=time[0]+self.h, minutes=time[1]+self.m, seconds=time[2]+self.s, milliseconds=time[3]*u+self.ms)

			fix_new_time = self.edittime(sub,new_time)

			subfile = re.sub(i,fix_new_time,subfile)

		subfile = subfile.encode('utf-16') if utf16 else subfile

		return subfile

	def getfile(self):

		self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '',"Subtitles files (*.srt *.ass)")

		try:
			self.subfile = open(self.fname,"rb").read()
		except:
			self.fname = None


	def savefile(self):
		try:
			sub = self.fname[-3:]
		except:
			sub = '*'

		self.sname = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '*.'+sub,"Subtitles files (*.srt *.ass)")

	def n_sync(self):

		e = QtGui.QWidget()
		self.h = int(self.ui.spinBox.text())
		self.m = int(self.ui.spinBox_2.text())
		self.s = int(self.ui.spinBox_3.text())
		self.ms = int(self.ui.spinBox_4.text())

		if self.fname == None:	
			q = QtGui.QMessageBox.warning(e , "Message", "please select file first.")
			
		else:
			sub = self.fname[-3:]
			out = self.sname if self.sname !=None else 'newfile.' + sub
			fn = self.sync(self.subfile,sub)
			final = open(out,"wb")
			final.write(fn)
			final.close()
			QtGui.QMessageBox.information(e, "Message", " file saved " +out )
		

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
