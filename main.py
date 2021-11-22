import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QGroupBox
import mysql.connector
class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("mainwindow.ui",self)
        self.add_info.clicked.connect(self.gotoAddInfo)


    def gotoAddInfo(self):
        firstname = self.fname.text()
        middlename = self.mname.text()
        lastname = self.lname.text()
        fmailememeber = self.nofc.text()
        blood_group = self.bloodGroup.text()
        addhernumber = self.addherNo.text()
        dataofbrith = self.DOB.text()
        dataofjoing = self.DOJ.text()
        nomine = self.Nomine.text()
        mob1 = self.Mobile1.text()
        mob2 = self.Mobile2.text()
        Email = self.email.text()

        # print ("all ok")
        if len(firstname) == 0 or len(middlename) ==0 or len(lastname) == 0 or len(fmailememeber) == 0 or len(blood_group) == 0 or len(addhernumber) ==0 or len(dataofbrith) ==0 or len(dataofjoing) == 0 or len(nomine) == 0 or len(mob1) == 0 or len(mob2) == 0 or len(Email) == 0:
            self.error.setText("Please input all fields.")
        else:
            self.error.setText("Data send")

class

# main
app = QApplication(sys.argv)
login = LoginScreen()
login.setWindowTitle("Login")

login.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")