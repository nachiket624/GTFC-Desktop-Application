# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrintInvoice.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os
import mysql.connector
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMessageBox
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
def setvaiablefunction(loneNumber):
    lone_no = loneNumber
    loen_data(lone_no)

def loen_data(lone_no):
    global lastlone0,lastlone1,lastlone2,lastlone3,lastlone4
    global  lastlonedate0,lastlonedate1,lastlonedate2,lastlonedate3,lastlonedate4
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    query = """select amount,date from transaction_detail where remark = "Saving" and lone_no = """+str(lone_no)
    # "select amount,date from transaction_detail where remark = "test" and addher_no = 1234;"
    cur.execute(query)
    lastfivelone = cur.fetchmany(5)
    lastlone = ["-","-","-","-","-"]
    lastlone11 = []
    lastdate11 =[]
    lastdate = ["-","-","-","-","-"]
    for count,lastfiveloneammount in enumerate (lastfivelone):
        amount = lastfiveloneammount[0]
        lastlone11.append(amount)
        lastlone[count] = lastlone11[count]
        date = (lastfiveloneammount[1])
        lastdate11.append(date)
        lastdate[count] = lastdate11[count]

    print(lastlone)
    print(lastdate)

    # ! last five lone transaction amount
    lastlone0 = lastlone[0]
    lastlone1 = lastlone[1]
    lastlone2 = lastlone[2]
    lastlone3 = lastlone[3]
    lastlone4 = lastlone[4]
    # ! last five lone transaction date
    lastlonedate0 = lastdate[0]
    lastlonedate1 = lastdate[1]
    lastlonedate2 = lastdate[2]
    lastlonedate3 = lastdate[3]
    lastlonedate4 = lastdate[4]

def total_saving(addher_no):
        global totalSaving
        conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
        cur = conn.cursor()
        cur.execute("""select opning_balance from memberinfo where addherNo = """+str(addher_no))
        totalSaving1=cur.fetchone()
        totalSaving = totalSaving1[0]
        print(type(totalSaving))
        cur.close()
        conn.close()


def saving_account(addher_no,remark):
    conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
    cur = conn.cursor()
    cur.execute(f"""select date,amount from transaction_detail where remark =  "{remark}" and addher_no = "{str(addher_no)}"  order By date desc""")
    # print(f"""select date,amount from transaction_detail where remark =  "{remark}" and addher_no = "{str(addher_no)}"  order By date desc""")
    transactionDetail = cur.fetchall()
    print(transactionDetail)
    cur.close()
    conn.close()
    print(transactionDetail)
    return transactionDetail

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(851, 847)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Perview_btn = QPushButton(Dialog)
        self.Perview_btn.setObjectName(u"Perview_btn")

        self.gridLayout.addWidget(self.Perview_btn, 1, 1, 1, 1)

        self.Invoice_print_btn = QPushButton(Dialog)
        self.Invoice_print_btn.setObjectName(u"Invoice_print_btn")

        self.gridLayout.addWidget(self.Invoice_print_btn, 1, 0, 1, 1)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet(u"")
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setReadOnly(False)
        self.textEdit.setPlaceholderText(u"")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)

        QWidget.setTabOrder(self.Invoice_print_btn, self.Perview_btn)
        QWidget.setTabOrder(self.Perview_btn, self.textEdit)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        fname = "Nachiket"
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Perview_btn.setText(QCoreApplication.translate("Dialog", u"perview", None))
        self.Invoice_print_btn.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.textEdit.setDocumentTitle("")
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Green Thought Farmers Club</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Date:</span><span style=\" font-size:12pt;\"> 1-1-2021</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-"
                        "size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Invoice No:</span><span style=\" font-size:12pt;\"> 00001</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Name:</span><span style=\" font-size:12pt;\"> %s  Parjane</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Addher No:</span><span style=\" font-size:12pt;\"> 123456789012</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">           </span><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">SAVING ACCOUNT</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">DATE			AMOUNT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">%s		        %s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;"
                        "\">%s		        %s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">%s		        %s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">%s		        %s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">%s		        %s</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">TOTAL SAVING:</span><span style=\" font-size:12pt;\">  %s</span></p>\n"
"<p style=\"-qt-parag"
                        "raph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">		</span><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">LONE ACCOUNT</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">DATE		AMOUNT	INTREST	TOTAL</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1-1-2021	1000		200		1200</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1-2-2021	500		0		500</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1-3-2021	300		200		500</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1-4-2021	500		0		500</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1-5-2021	500		0		500</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">REAMAING AMMOUNT:</span><span style=\" font-size:12pt;\">	30000</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">CHECK</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None)%(fname,lastlone0,lastlonedate0,lastlone1,lastlonedate1,lastlone2,lastlonedate2,lastlone3,lastlonedate3,lastlone4,lastlonedate4,totalSaving))
    # retranslateUi

# loen_data(1)
# print(lastlone0)

# total_saving(1234)
# saving_account(12345,"Saving")