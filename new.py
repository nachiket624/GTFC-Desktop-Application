import sys
import os
from datetime import date
import datetime
from PySide2 import QtWidgets
import dashboard_rc
import database
import loneInfo
from MainWindow import Ui_MainWindow
from PySide2.QtWidgets import(QTableWidget, QTableWidgetItem)
from collect_lone import Ui_Dialog
from database import *
from PySide2.QtGui import QIcon
from updatainformation import *
import updatainformation
# from biodata import Ui_Dialog1
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setIcon()
        # ! ***************************** Database Check *****************************
        # username = os.environ.get('db_user')
        # userpass = os.environ.get('db_pass')
        # conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        # cur = conn.cursor()

        # cur.execute('show databases')
        # for table in cur:
        #    print(table)
        #    if 'green' in table:
        #        print("Find")
        #        continue
        #    else:
        #        cur.execute('CREATE DATABASE IF NOT EXISTS green2')


        # ! ***************************** Dasboard *****************************
        self.stackedWidget.setCurrentWidget(self.dashboard_page)
        self.dashboard_btn.clicked.connect(self.windashboard)
        idtext = rowcount()
        idtext1 = int(idtext - 1)
        self.total_member.setText(str(idtext1))
        totalLone = lonecount()
        self.total_lone.setText(str(totalLone))

 #  ******************************************************* Side Bar *******************************************************
        self.view_btn.clicked.connect(self.WinView)
        self.Manage_btn.clicked.connect(self.WinManage)

        # ! ***************************** inside Function Button *****************************



    def WinManage(self):
        self.stackedWidget.setCurrentWidget(self.pageManage)
        self.update_member_btn.clicked.connect(self.updatamember)
        self.give_lone.clicked.connect(self.giveloneerr)
        self.collect_lone_btn.clicked.connect(self.showlonedig)
        self.new_member_btn.clicked.connect(self.showaddmemberfuntionerr)
    def setIcon(self):
        appIcon = QIcon("gtfc.jpeg")
        self.setWindowIcon(appIcon)

    def WinView(self):
        self.stackedWidget.setCurrentWidget(self.page_view)
        self.viewall_btn.clicked.connect(self.viewallfunction)
        # self.biodataview_btn.clicked.connect(self.ConnecttoBioData)

        # ! ***************************** Dashboard Function *****************************
    def windashboard(self):
        self.stackedWidget.setCurrentWidget(self.dashboard_page)

#  ******************************************************* Manage *******************************************************


    # ! ***************************** Manage  Add Member Function *****************************
    def addmemberfuntion(self):
        fname = self.firstname.text()
        mname = self.middlename.text()
        lname = self.lastname.text()
        bgroup = str(self.bloodgroup.currentText())
        nomine = self.nomine.text()
        dob = self.dob.text()
        doj = self.doj.text()
        addherNo = self.addhernumber.text()
        account = self.accountno.text()
        mobile1 = self.mobile1.text()
        mobile2 = self.mobile2.text()
        email = self.email.text()
        opnningBalance = self.balance.text()
        id = self.id.text()
        user_info = [id, fname, mname, lname, bgroup, nomine, dob, doj, addherNo, account, mobile1, mobile2, email,
                     opnningBalance]
        if len(fname) == 0 or len(mname) == 0 or len(lname) == 0 or len(bgroup) == 0 or len(nomine) == 0 or len(
                addherNo) == 0 or len(account) == 0 or len(mobile1) == 0 or len(mobile2) == 0 or len(email) == 0 or len(
            opnningBalance) == 0:
            self.error.setText("Place input all filed")
        else:

            conn = mysql.connector.connect(host="localhost", user= username, password= userpass, database="green")

            cur = conn.cursor()
            cur.execute(
                """INSERT INTO memberinfo(id,first_name, middle_name, last_name, blood_group, nomine, data_of_brith, data_of_joing, addherNo, accountNo, mobile_no1, mobile_no2, email, opning_balance)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                user_info)
            cur.close()
            conn.commit()
            conn.close()

    #     This funtion show error for add member funtion
    def showaddmemberfuntionerr(self):
        self.stackedWidget.setCurrentWidget(self.page_addnewmember)
        idtext = rowcount()
        id = self.id.setText(str(idtext))
        self.addinfo.clicked.connect(self.addmemberfuntion) # add information button


    # ! ***************************** Manage  Update Member Function *****************************
    def updatamember(self):
        self.stackedWidget.setCurrentWidget(self.UpdateInformation)
        self.search.clicked.connect(self.searchfun)
    def searchfun(self):
        id = self.id_2.text()
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("select * from memberinfo where id = "+id)
        for data in cur:
          data
        fname = data[1]
        mname = data[2]
        lname = data[3]
        bgroup = data[4]
        nomine = data[5]
        dob = data[6]
        doj =data[7]
        addherNo = data[8]
        account = data[9]
        mobile1 = data[10]
        mobile2 = data[11]
        email = data[12]
        opnningBalance =data[13]

        # ? @@@@@@@@@@@ setting value to line edit @@@@@@@@@@@
        self.firstname_2.setText(fname) # fname is line edit object name
        self.middlename_2.setText(mname)
        self.lastname_2.setText(lname)
        self.bloodgroup_2.setCurrentText(bgroup)
        self.nomine_2.setText(nomine)
        self.dob_2.setDate(dob)
        self.doj_2.setDate(doj)
        self.addhernumber_2.setText(str(addherNo))
        self.accountno_2.setText(account)
        self.mobile1_2.setText(str(mobile1))
        self.mobile2_2.setText(str(mobile2))
        self.email_2.setText(email)
        self.balance_2.setText(str(opnningBalance))

        self.addinfo_2.clicked.connect(self.getmembervalue)
        # ? @@@@@@@@@@@ Updataing value from line edit @@@@@@@@@@@
    def getmembervalue(self):
      #? @@@@@@@@@@@@@@@@@@@@@@@@@@Assing Value to line edit @@@@@@@@@@@@@@@@@@@@@@@@@@
        id1 = self.id_2.text()
        first_name1 = self.firstname_2.text()
        middle_name1 = self.middlename_2.text()
        last_name1 = self.lastname_2.text()
        blood_group1 = str(self.bloodgroup_2.currentText())
        nomine1 = self.nomine_2.text()
        dob1 = self.dob_2.text()
        doj1 = self.doj_2.text()
        accountno1 = self.accountno_2.text()
        mob11 = self.mobile1_2.text()
        mob12 = self.mobile2_2.text()
        email1 = self.email_2.text()
        balance1 = self.balance_2.text()
        input_data = (first_name1, middle_name1, last_name1, blood_group1, nomine1, dob1, doj1, accountno1, mob11, mob12, email1,balance1, id1)
        username = os.environ.get('db_user')
        userpass = os.environ.get('db_pass')
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("""Update memberinfo set first_name = %s, middle_name = %s, last_name = %s, blood_group = %s, nomine = %s, data_of_brith = %s, data_of_joing = %s, accountNo = %s, mobile_no1 = %s, mobile_no2 = %s, email = %s, opning_balance =  %s where id = %s""",
                input_data)
        cur.close()
        conn.commit()
        conn.close()
    # ! ***************************** Manage  give lone Function *****************************
    def lonefunction(self):

        lone_no = self.loneno.text()
        name = self.name.text()
        addher = self.addherno.text()
        addher2 = addher
        amount = self.amount.text()
        interast = str(self.intrest_rate.currentText())
        checkno = self.checkno.text()
        date1 = self.date1_1.text()
        jam1 = self.jam1_2.text()
        jam2 = self.jam1_3.text()
        remark = str(self.remark_2.currentText())

        lone_info = [lone_no, name, addher, amount, interast, checkno, date1, jam1, jam2, remark]
        if len(name) == 0 or len(jam1) == 0 or len(jam2) == 0 or len(amount) == 0:
            self.error_3.setText("Place input all filed")
        else:
            conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
            cur = conn.cursor()
            cur.execute("""INSERT INTO lone (lone_no, appliername, addherNo, amount, insrast_rate, check_number, lone_date, Jamindar1, Jamindar2, remark) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",lone_info)
            cur.close()
            conn.commit()
            conn.close()
            totalAmounttopay = 100
            totalIntersetpay = 1000
            totalintersetamount = 1000
            tr_type = "Lone Approve"
            database.getdatalone(lone_no,name,addher,amount,interast,totalAmounttopay,totalIntersetpay,totalintersetamount)
            loneInfo.setlone(lone_no,amount,date1,addher,interast,name,tr_type)
    def giveloneerr(self):
        self.stackedWidget.setCurrentWidget(self.pagelone)
        lone_no1 = lastlonen()
        lone_no = self.loneno.setText(str(lone_no1))
        self.approve_btn.clicked.connect(self.lonefunction)
    #  ******************************************************* View *******************************************************

    # ! ***************************** View Information table *****************************
    def viewallfunction(self):
        tableWidget = QTableWidget
        self.stackedWidget.setCurrentWidget(self.table_view)
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        query = "SELECT * FROM memberinfo ORDER BY ID ASC"
        cur.execute(query)
        record = cur.fetchall()

        row = 0
        self.tableWidget.setRowCount(len(record))
        for record in record:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(record[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(record[1])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(record[2])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(record[3])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(record[4])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(record[5])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(record[6])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(record[7])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(record[8])))
            self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(record[9])))
            self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(record[10])))
            self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(record[11])))
            self.tableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(str(record[12])))
            self.tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(record[13])))
            row = row + 1

    def showlonedig(self):
        # self.stackedWidget.setCurrentWidget(self.showlonedig)
        lonewin = Lone_Collection()
        lonewin.show()
        lonewin.exec_()


# ! ***************************** Manage  lone collection class *****************************

class Lone_Collection(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(Lone_Collection, self).__init__()
        self.setupUi(self)
        self.find_btn.clicked.connect(self.find)
        self.radioButton.clicked.connect(self.getdate)
        self.collect_btn.clicked.connect(self.sentto_loneCollection)
    def find(self):
        id_field = self.lone_no.text()
        conn = conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
        cur = conn.cursor()
        cur.execute("""select Name,AddherNo from lone_info where Lone_no = """+id_field)
        for data in cur:
            data
        cur.close()
        conn.commit()
        conn.close()
        self.lone_name.setText(str(data[0]))
        self.addhere_no.setText(str(data[1]))
        self.getdata()
    def getdata(self):
        id_field = self.lone_no.text()
        conn = conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
        cur = conn.cursor()
        cur.execute("""select * from lone_info where lone_no = """+id_field)
        for data in cur:
            data
        print(data)
        print("Type",type(data))
        row = 0
        self.tableWidget.setRowCount(12)
        data1 = 4
        data2 = 5
        for index in range(12):
            self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(str(data[data1])))
            self.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(str(data[data2])))
            data1 = data1+2
            data2 = data2+2
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(data[30])))
    def getdate(self):
        today = datetime.today()
        self.collect_date.setDate(today)
    def sentto_loneCollection(self):
        addher1 = self.addhere_no.text()
        lone_name1 = self.lone_name.text()
        lone_no1=self.lone_no.text()
        collect_date=self.collect_date.text()
        collect_amount = self.collect_ammount.text()
        Interst_rate = self.Interst_rate.text()
        tr_type = "Lone Collect"
        loneInfo.lone_collection(lone_no1,collect_amount,Interst_rate,collect_date,addher1,tr_type,lone_name1)

#*************************************Main*************************************
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()