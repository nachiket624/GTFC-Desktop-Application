import sys
from PySide2 import QtWidgets
from lone import Ui_Dialog

class mydilog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(mydilog,self).__init__()
        self.setupUi(self)

#main
app = QtWidgets.QApplication(sys.argv)

lone = mydilog()
lone.show()
lone.exec_()
