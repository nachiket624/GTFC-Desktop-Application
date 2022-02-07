import mysql.connector
import os
import sys
from PySide2.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from PySide2.QtWidgets import(QTableWidget, QTableWidgetItem)
from PySide2 import QtWidgets
from PySide2.QtCore import QDate,QDateTime,QTime
from LoneSaving import transactiondetail
from PySide2.QtWidgets import *
from savingLone import Ui_Dialog
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
print(username,userpass)
class lonedig(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(lonedig, self).__init__()
        self.setupUi(self)
        self.saving_find_btn.clicked.connect(self.lonefind)
        self.sfind_btn.clicked.connect(self.savingfind)

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
            # PrintInvoice.total_saving(addherNo)
            # PrintInvoice.loen_data(addherNo)
            self.getdata()
        except Exception as ee:
            msg = QtWidgets.QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Place Enter Valid LoneSaving Number")
            msg.setInformativeText("LoneSaving No Should Present in Database")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

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
        data1 = 5
        data2 = 6
        for index in range(12):
            self.tableWidget_2.setItem(index, 2, QtWidgets.QTableWidgetItem(str(data[data1])))
            self.tableWidget_2.setItem(index, 3, QtWidgets.QTableWidgetItem(str(data[data2])))
            data1 = data1 + 2
            data2 = data2 + 2
        self.tableWidget_2.setItem(index, 4, QtWidgets.QTableWidgetItem(str(data[30])))
    def clearfiled(self):
          self.error_4.clear()
          self.saddher.clear()
          self.sname.clear()
          self.samount.clear()

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
        saving_amount = self.samount.text()
        self.scollect_btn.clicked.connect(self.addSavvingAmount)
    def addSavvingAmount(self):
        insert_amount = self.samount.text()
        total_saving = self.member_total_saving.text()
        addsaving = float(insert_amount) + float(total_saving)
        data = [addsaving,savingid]
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("""UPDATE memberinfo set opning_balance = %s where id = %s""",data)
        cur.close()
        conn.commit()
        conn.close()
        self.sendTransactionSaving()
    def sendTransactionSaving(self):
        trid = self.sname_3.text()
        tramount = self.samount.text()
        trdate = self.sdate.text()
        traddher = self.saddher.text()
        transactiondetail.savingtr(tramount,trdate,trid,traddher)
        self.clearfiledsaving()
    def clearfiledsaving(self):
        self.sname_3.clear()
        self.sname.clear()
        self.saddher.clear()
        self.samount.clear()
        self.member_total_saving.clear()

