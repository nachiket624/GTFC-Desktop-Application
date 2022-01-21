import sys
import os
from datetime import date
import datetime
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
import PrintInvoice
import dashboard_rc
import database
import loneInfo
from MainWindow import Ui_MainWindow
from PySide2.QtWidgets import(QTableWidget, QTableWidgetItem)
from collect_lone import Ui_Dialog
from PrintInvoice import Ui_Dialog1
from saving_account import Ui_Dialog2
from database import *
from PySide2.QtGui import QIcon
from PySide2.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from PySide2.QtCore import QDate,QDateTime
from updatainformation import *
import updatainformation
from create
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
        self.dashboard_btn.setStyleSheet('* {border: none;background-color: rgba(13, 9, 36,0);border-radius: 13;color: rgb(0, 0, 0);border-radius: 13;}')

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
        self.dashboard_btn.setStyleSheet('* {border: none;background-color: rgba(13, 9, 36,0);border-radius: 13;color: rgb(0, 0, 0);border-radius: 13;}')
        self.Manage_btn.setStyleSheet('* {background-color: rgb(0, 0, 0);color: rgb(218, 145, 0);border-radius: 13;}')
        self.update_member_btn.clicked.connect(self.updatamember)
        self.give_lone.clicked.connect(self.giveloneerr)
        self.collect_lone_btn.clicked.connect(self.showlonedig)
        self.new_member_btn.clicked.connect(self.showaddmemberfuntionerr)
        self.add_saving.clicked.connect(self.connect_saving)
    def setIcon(self):
        appIcon = QIcon("gtfc.jpeg")
        self.setWindowIcon(appIcon)

    def WinView(self):
        self.Manage_btn.setStyleSheet('* {border: none;background-color: rgba(13, 9, 36,0);border-radius: 13;color: rgb(0, 0, 0);border-radius: 13;}')
        self.view_btn.setStyleSheet('* {background-color: rgb(0, 0, 0);color: rgb(218, 145, 0);border-radius: 13;}')
        self.view_btn.setStyleSheet('* {border: none;background-color: rgba(13, 9, 36,0);border-radius: 13;color: rgb(0, 0, 0);border-radius: 13;}')

        self.stackedWidget.setCurrentWidget(self.page_view)
        self.viewall_btn.clicked.connect(self.viewallfunction)
        self.transaction_detail_btn.clicked.connect(self.transaction_detail_table)
        # self.biodataview_btn.clicked.connect(self.ConnecttoBioData)

        # ! ***************************** Dashboard Function *****************************
    def windashboard(self):
        self.stackedWidget.setCurrentWidget(self.dashboard_page)
        self.dashboard_btn.setStyleSheet('* {background-color: rgb(0, 0, 0);color: rgb(218, 145, 0);border-radius: 13;}')
        self.Manage_btn.setStyleSheet('* {border: none;background-color: rgba(13, 9, 36,0);border-radius: 13;color: rgb(0, 0, 0);border-radius: 13;}')
        self.view_btn.setStyleSheet('* {border: none;background-color: rgba(13, 9, 36,0);border-radius: 13;color: rgb(0, 0, 0);border-radius: 13;}')

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
                addherNo) == 0 or len(account) == 0 or len(mobile1) == 0 or len(opnningBalance) == 0:
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
            self.clearfiled()

    #     This funtion show error for add member funtion
    def showaddmemberfuntionerr(self):
        self.stackedWidget.setCurrentWidget(self.page_addnewmember)
        idtext = rowcount()
        id = self.id.setText(str(idtext))
        self.addinfo.clicked.connect(self.addmemberfuntion) # add information button
    def clearfiled(self):
        self.firstname.clear()
        self.lastname.clear()
        self.middlename.clear()
        self.bloodgroup.setCurrentIndex(0)
        self.nomine.clear()
        self.dob.setDate(QDate(2000,1,1))
        self.doj.setDate(QDate(2000,1,1))
        self.addhernumber.clear()
        self.accountno.clear()
        self.mobile1.clear()
        self.mobile2.clear()
        self.email.clear()
        self.balance.clear()

    # ! ***************************** Manage  Update Member Function *****************************
    def updatamember(self):
        self.stackedWidget.setCurrentWidget(self.UpdateInformation)
        self.search.clicked.connect(self.searchfun)
    def searchfun(self):
        try:
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
        except Exception as e:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Input device error")
            error_message.showMessage("वैध आयडी एंटर करा")
            print("Plase enter valid ID")

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
        # self.accountno_2.clear(mobile2_2,mobile1_2)
        self.cleartext()
    def cleartext(self, ):
        # self.dob.setMinimumDate('2000/2/1')
        self.id_2.clear()
        self.firstname_2.clear()
        self.middlename_2.clear()
        self.lastname_2.clear()
        self.bloodgroup_2.setCurrentIndex(0)
        self.nomine_2.clear()
        self.dob_2.setDate(QDate(2000,1,1))
        self.doj_2.setDate(QDate(2000, 1, 1))
        self.addhernumber_2.clear()
        self.accountno_2.clear()
        self.mobile1_2.clear()
        self.mobile2_2.clear()
        self.email_2.clear()
        self.balance_2.clear()




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
            self.give_lone_clear()
    def giveloneerr(self):
        self.stackedWidget.setCurrentWidget(self.pagelone)
        lone_no1 = lastlonen()
        lone_no = self.loneno.setText(str(lone_no1))
        self.approve_btn.clicked.connect(self.lonefunction)
    def give_lone_clear(self):
        self.loneno.clear()
        self.name.clear()
        self.addherno.clear()
        self.amount.clear()
        self.intrest_rate.setCurrentIndex(0)
        self.checkno.clear()
        self.date1_1.setDate(QDate(2000,1,1))
        self.jam1_2.clear()
        self.jam1_3.clear()
        self.remark_2.setCurrentIndex(0)
    #  ******************************************************* View *******************************************************

    # ! ***************************** View Information table *****************************
    def viewallfunction(self):
        tableWidget = QTableWidget
        myheader = ['ID','Frist Name','Middle Name','Last Name','Blood Group','Nomine','Data of Brith','Date of Joining', 'Addher No', 'Account No', 'Mobile No 1', 'Mobile No 2', 'Email', 'Opening Balance']
        self.tableWidget.setHorizontalHeaderLabels(myheader)
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
    def transaction_detail_table(self):
        # self.stackedWidget.setCurrentWidget(self.table_view)
        tableWidget = QTableWidget

        self.stackedWidget.setCurrentWidget(self.transaction_detail_page)
        myheader = ['transaction_no', 'Name', 'Addher No', 'Date', 'amount', 'remark', 'lone_no', 'Intrest']
        self.tableWidget_2.setHorizontalHeaderLabels(myheader)
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        query = "SELECT * FROM transaction_detail ORDER BY transaction_no ASC"
        cur.execute(query)
        record = cur.fetchall()
        row = 0
        self.tableWidget_2.setRowCount(len(record))
        for record in record:
            # self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(record[0])))
            self.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(str(record[0])))
            self.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(str(record[1])))
            self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(str(record[2])))
            self.tableWidget_2.setItem(row,3,QtWidgets.QTableWidgetItem(str(record[3])))
            self.tableWidget_2.setItem(row,4,QtWidgets.QTableWidgetItem(str(record[4])))
            self.tableWidget_2.setItem(row,5,QtWidgets.QTableWidgetItem(str(record[5])))
            self.tableWidget_2.setItem(row,6,QtWidgets.QTableWidgetItem(str(record[6])))
            self.tableWidget_2.setItem(row,7,QtWidgets.QTableWidgetItem(str(record[7])))

            row = row + 1
    def showlonedig(self):
        # self.stackedWidget.setCurrentWidget(self.showlonedig)
        lonewin = Lone_Collection()
        lonewin.show()
        lonewin.exec_()
    def connect_saving(self):
        sa = Saving_account()
        sa.show()
        sa.exec()

# ! ***************************** Manage  lone collection class *****************************

class Lone_Collection(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(Lone_Collection, self).__init__()
        self.setupUi(self)
        self.find_btn.clicked.connect(self.find)
        self.radioButton.clicked.connect(self.getdate)
        self.collect_lone_btn.clicked.connect(self.sentto_loneCollection)
        self.print_btn.clicked.connect(self.callmyinvoice)
    def find(self):
        try:
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
            addherNo = str(data[1])
            PrintInvoice.total_saving(addherNo)
            PrintInvoice.loen_data(addherNo)
            self.getdata()
        except Exception as ee:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Input Error")
            error_message.showMessage("Please Enter Valid Lone Number")


    def getdata(self):
        id_field = self.lone_no.text()
        conn = conn = mysql.connector.connect(host="localhost", user="root", password="1900340220", database="green")
        cur = conn.cursor()
        cur.execute("""select * from lone_info where lone_no = """+id_field)
        for data in cur:
            1
        print(data)
        print("Type",type(data))
        row = 0
        self.tableWidget.setRowCount(12)
        data1 = 5
        data2 = 6
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
    def callmyinvoice(self):
        # app1 = QtWidgets.QApplication(sys.argv)
        mywin = MYInvoics()
        mywin.show()
        mywin.exec_()

class MYInvoics(QtWidgets.QDialog,Ui_Dialog1):
    def __init__(self):
        super(MYInvoics, self).__init__()
        self.setupUi(self)
        self.Invoice_print_btn.clicked.connect(self.print_file)
        self.Perview_btn.clicked.connect(self.print_preview_dialog)


    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        diglog = QPrintDialog(printer, self)

        if diglog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)


    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printperview)
        previewDialog.exec_()


    def printperview(self, printer):
        self.textEdit.print_(printer)

class Saving_account(QtWidgets.QDialog,Ui_Dialog2):
    def __init__(self):
        super(Saving_account, self).__init__()
        self.setupUi(self)
        now = QDate.currentDate()
        self.sdate.setDate(now)
        self.sfind_btn.clicked.connect(self.findmember)
        self.scollect_btn.clicked.connect(self.addbalancetosaving)
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("select first_name,middle_name,last_name from memberinfo")
        lt = (cur.fetchall())
        cur.close()
        conn.commit()
        conn.close()
        member_name = ["%s %s %s" % x for x in lt]
        print(member_name)
        completer = QCompleter(member_name)
        self.sname.setCompleter(completer)

    def findmember(self):
        name = self.sname.text()
        myList = [name]
        conList = (myList[0].split())
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        first_name = str(conList[0])
        middle_name = str(conList[1])
        last_name = str(conList[2])
        cur.execute(f"""select addherNo from memberinfo where first_name = "{first_name}" and middle_name = "{middle_name}" and last_name = "{last_name}" """)
        addher = cur.fetchone()
        cur.close()
        conn.commit()
        conn.close()
        self.saddher.setText(str(addher[0]))
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("select opning_balance from memberinfo where addherNo ="+str(addher[0]))
        totalsaving = (cur.fetchone())
        cur.close()
        conn.commit()
        conn.close()
        self.member_total_saving.setText(str(totalsaving[0]))


    def addbalancetosaving(self,addher_no):
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        addher = self.saddher.text()
        addsave = self.samount.text()
        if len(addsave)>=0:
            self.error_4.setText("Place fill all the filed")
        totalsaving = self.member_total_saving.text()
        addsavingsum = int(totalsaving) + int(addsave)
        print(addsavingsum)
        print(addher)
        data = [addsavingsum,addher]
        # UPDATE  memberinfo set opning_balance = 1000001  where   addherNo = '333333333333';
        cur.execute("UPDATE memberinfo SET opning_balance = %s WHERE  addherNo = %s",data)
        cur.close()
        conn.commit()
        conn.close()
        self.saving_transaction_detail()
        self.clearfiled()
    def saving_transaction_detail(self):
        stname = self.sname.text()
        staddher = self.saddher.text();
        stdate = self.sdate.text();
        stamount = self.samount.text()
        tr_type = "Saving"
        loneInfo.saving_account(stname,staddher,stdate,stamount,tr_type)

    def clearfiled(self):
        self.error_4.clear()
        self.saddher.clear()
        self.sname.clear()
        self.samount.clear()



#*************************************Main*************************************
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()