import mysql.connector
import os
from datetime import datetime
from datetime import date
import sys
from PySide2.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from PySide2.QtWidgets import(QTableWidget, QTableWidgetItem)
from PySide2 import QtWidgets
from PySide2.QtCore import QDate,QDateTime,QTime
from LoneSaving.transactiondetail import trancationSavingLone
from Print import InvoiceGenerator
from Print import importdata
from LoneSaving.transaction_integration import mainTransactionTable
from PySide2.QtWidgets import *
from savingLone import Ui_Dialog
from Print import printcommand
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
print(username,userpass)
class lonedig(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(lonedig, self).__init__()
        self.setupUi(self)
        self.saving_find_btn.clicked.connect(self.lonefind)
        self.sfind_btn.clicked.connect(self.savingfind)
        now = QDate.currentDate()
        self.dateEdit.setDate(now)
        now = QDate.currentDate()
        self.collect_date_2.setDate(now)
        self.analytics_data_find.clicked.connect(self.analyticsdate)
        self.scollect_btn.clicked.connect(self.addSavvingAmount)
        self.collect_lone_btn_2.clicked.connect(self.checktextdit)
    def lonefind(self):
        try:
            id_field = self.LoneNo.text()
            conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass,
                                                  database="green")
            cur = conn.cursor()
            cur.execute("""select Name,AddherNo from lone_info where Lone_no = """ + id_field)
            for data in cur:
                data
            cur.close()
            conn.commit()
            conn.close()
            self.lone_name_2.setText(str(data[0]))
            self.addhere_no_2.setText(str(data[1]))
            addherNo = str(data[1])
            self.getdata()
            self.historyLone(id_field)

            # PrintInvoice.total_saving(addherNo)
            # PrintInvoice.loen_data(addherNo)

        except Exception as ee:
            print(ee)
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Place Enter Valid LoneSaving Number")
            msg.setInformativeText("LoneSaving No Should Present in Database")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    def historyLone(self,id_field):
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("""select last_transaction_date,Lone_take,total_ammount_to_pay,total_interest_he_pay,Intrest from lone_info where lone_no = """ + id_field)
        his = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        his1 = [item for t in his for item in t]
        self.label_49.setText(str(his1[1]))
        self.label_50.setText(str(his1[2]))
        self.label_54.setText(str(his1[3]))
        self.label_56.setText(str(his1[0]))
        self.label_53.setText(str(his1[4]))
    def getdata(self):
        id_field = self.LoneNo.text()
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("""select * from lone_info where lone_no = """ + id_field)
        for data in cur:
            1
        print(data)
        row = 0
        self.tableWidget_2.setRowCount(12)
        data1 = 7
        data2 = 8
        for index in range(12):
            self.tableWidget_2.setItem(index, 1, QtWidgets.QTableWidgetItem(str(data[data1])))
            self.tableWidget_2.setItem(index, 2, QtWidgets.QTableWidgetItem(str(data[data2])))
            data1 = data1 + 2
            data2 = data2 + 2
        self.tableWidget_2.setItem(index, 4, QtWidgets.QTableWidgetItem(str(data[30])))
        self.calintrestrate(id_field)
    #! Intrest calculationb function
    def lone_info(self,lone_id):
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute(
            "select total_ammount_to_pay,Intrest,Lone_take,Total_interest_amount_pay,last_transaction_date from lone_info where lone_no = " + str(
                lone_id))
        loneInfodetile = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        # print(loneInfodetile)
        return loneInfodetile

    def diff_month(self,d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    def clearDate(self,inputdate):
        x5 = inputdate.replace("/", " ")
        datetime_object = datetime.strptime(x5, '%Y %m %d')
        return datetime_object

    def calintrestrate(self,loneid):
        today = date.today()
        d1 = self.collect_date_2.text()
        d1 = self.clearDate(d1)
        print(d1)
        loneInfo = self.lone_info(loneid)
        out = [item for t in loneInfo for item in t]
        # total_amount_to_pay(remmaing amount), intrest,Lone_take,total_intrest_amount(sum of intrestrate and amount),last_transaction_date
        print(out)
        tatp = out[0]
        intrest = out[1]
        tia = out[2]
        ltd = out[4]
        print(ltd)
        time_diff = self.diff_month(d1,ltd)
        print(time_diff)
        intrestlable = (tatp * intrest * time_diff) / 100
        self.label_55.setText(str(intrestlable))
    def total_ammount_to_pay(self,lone_no,amount):
        reammingAmount = self.label_50.text()
        reammingAmount = float(reammingAmount)
        amount = float (amount)
        toremainning = reammingAmount - amount
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("update lone_info set total_ammount_to_pay = "+str(toremainning)+" where lone_no = "+str(lone_no))
        cur.close()
        conn.commit()
        conn.close()
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("select total_ammount_to_pay,Total_interest_pay from lone_info where lone_no = "+lone_no)
        amountIntrest = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        out11 = [item for t in amountIntrest for item in t]
        Total_interest_amount_pay = int(out11[0])+int(out11[1])
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("update lone_info set Total_interest_amount_pay = "+str(Total_interest_amount_pay)+" where lone_no = "+str(lone_no))
        cur.close()
        conn.commit()
        conn.close()
    #! ****************************************************************************************************************************************************
    def checktextdit(self):
        collect_amount = self.collect_ammount_2.text()
        if len(collect_amount)>0:
            id_field = self.LoneNo.text()
            lone_no = self.LoneNo.text()
            collection_date = self.collect_date_2.text()
            amount = self.collect_ammount_2.text()

            # update_intrest_lable =

            intrest = self.label_55.text()
            addher = self.addhere_no_2.text()
            tr_type = 'Lone Collection'
            name = self.lone_name_2.text()
            self.updateloneinfo(lone_no,amount,intrest,collection_date,addher,tr_type,name)
            # def lonetransation(self, addher, lone_no, date, amount, intrest):
            self.lonetransation(addher,id_field,collection_date,amount,intrest)
            print(lone_no,amount)
            self.total_ammount_to_pay(lone_no, amount)
            self.showDialog()
        else:
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Place Enter Valid LoneSaving Number")
            msg.setInformativeText("LoneSaving No Should Present in Database")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def updateloneinfo(self,lone_no,amount,instrest,collection_date,addher,tr_type,name):
        x1 = str(lone_no)
        x2 = str(amount)
        x3 = str(instrest)
        x4 = str(collection_date)
        x5 = x4.replace("/", " ")
        datetime_object = datetime.strptime(x5, '%Y %m %d')
        month_name = datetime_object.strftime("%B")
        month_name1 = datetime_object.strftime("%b")
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        # update lone_info set Lone_take = 700, Intrest = 2 where Lone_no = 8;
        cur.execute("UPDATE lone_info set " + month_name + " = " + x2 + ", interest_" + month_name1 + " = " + x3 + ", last_transaction_date = '"+ str(collection_date)+"' where Lone_no = " + x1)
        cur.close()
        conn.commit()
        conn.close()
    def lonetransation(self,addher,lone_no,date,amount,intrest):
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("SELECT count(*) from lonetransaction")
        count = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        his1 = [item for t in count for item in t]
        print(his1)
        if his1[0] == 0:
            tr_no = 1
            conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
            cur = conn.cursor()
            insertData = [tr_no,addher,lone_no,date,amount,intrest]
            cur.execute("INSERT INTO green.lonetransaction (trNo, addher_no, lone_no, date, amount, intrest) VALUES(%s,%s,%s,%s,%s,%s)",insertData)
            cur.close()
            conn.commit()
            conn.close()
        else:
            conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
            cur = conn.cursor()
            insertData = [addher, lone_no, date, amount, intrest]
            cur.execute(
                "INSERT INTO green.lonetransaction (addher_no, lone_no, date, amount, intrest) VALUES(%s,%s,%s,%s,%s)",
                insertData)
            cur.close()
            conn.commit()
            conn.close()


    def clearfiled(self):
        # self.error_4.clear()
        self.LoneNo.clear()
        self.lone_name_2.clear()
        self.addhere_no_2.clear()
        self.collect_ammount_2.clear()

    def savingfind(self):
        global savingid
        savingid = self.sname_3.text()
        conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("""select first_name, middle_name, last_name, addherNo, opning_balance from memberinfo where id = """+str(savingid))
        saving_data = cur.fetchone()
        first_name = saving_data[0]
        middle_name = saving_data[1]
        last_name = saving_data[2]
        addher_no = saving_data[3]
        saving_amount = saving_data[4]
        full_name = str(first_name+" "+middle_name+" "+last_name)
        self.sname.setText(str(full_name))
        self.saddher.setText(str(addher_no))
        self.member_total_saving.setText(str(saving_amount))
        self.currentDate()
    def currentDate(self):
        now = QDate.currentDate()
        self.sdate.setDate(now)
    def addSavvingAmount(self):
        total_saving = self.member_total_saving.text()
        insert_amount = self.samount.text()
        print(insert_amount,total_saving)
        if len(insert_amount)>0:

            in_amount = float(insert_amount)
            ts_amount = float(total_saving)
            if in_amount.is_integer():
                in_amount = float(insert_amount)
                addsaving = in_amount + ts_amount
                data = [addsaving,savingid]
                conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
                cur = conn.cursor()
                cur.execute("""UPDATE memberinfo set opning_balance = %s where id = %s""",data)
                cur.close()
                conn.commit()
                conn.close()
                self.sendTransactionSaving()
                # self.showDialog()

            else:
                self.member_total_saving.setText("Enter Integer value")

    def convertdate(self):
        lonedate = self.collect_date_2.text()
        x5 = lonedate.replace("/", " ")
        datetime_object = datetime.strptime(x5, '%Y %m %d')
        print("datetime_object", datetime_object)
        return datetime_object
    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Do Your Won Print Invoice")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msgBox.buttonClicked.connect(msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            proLone_no = self.LoneNo.text()
            proLone_no = int(proLone_no)
            proIntert = self.label_53.text()
            proIntert = float(proIntert)
            protoday = self.convertdate()

            InvoiceGenerator.gInvoice(proLone_no,proIntert,protoday)
            pdffile = "C:\pdftemp\invoice.pdf"

            printer_name = 'Canon MF3010'
            printcommand.main(pdffile,printer_name)


            # InvoiceGenerator.dataforProcess(proLone_no,proIntert,protoday)
            # InvoiceGenerator.prolone_no = proLone_no
            # InvoiceGenerator.proIntrest =proIntert



    def savingprint(self):
        print("saving print command is passed")
    def sendTransactionSaving(self):
        trid = self.sname_3.text()
        tramount = self.samount.text()
        trdate = self.sdate.text()
        traddher = self.saddher.text()
        trancationSavingLone.savingtr(tramount,trdate,trid,traddher)
        remark = "saving"
        tr_name = self.sname.text()
        tr_addher = self.saddher.text()
        tr_id = self.sname_3.text()
        tr_amount = self.samount.text()
        tr_data = self.sdate.text()
        mainTransactionTable.transaction_saving(tr_id, tr_name, tr_addher, tr_data, tr_amount, remark)

    def clearfiledsaving(self):
        self.sname_3.clear()
        self.sname.clear()
        self.saddher.clear()
        self.samount.clear()
        self.member_total_saving.clear()

    # ! set date for find the detail
    def analyticsdate(self):
       analdate = str(self.dateEdit.text())
       conn = conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
       cur = conn.cursor()
       cur.execute("""SELECT sum(amount)FROM savingaccounttransaction WHERE MONTH(date) = month('"""+analdate+"""')""")
       total_month=cur.fetchone()
       cur.close()
       conn.commit()
       conn.close()
       self.label_15.setText(str(total_month[0]))


