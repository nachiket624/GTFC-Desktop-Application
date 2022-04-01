# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edittextscript.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from PySide2 import QtWidgets
# from edittextscript import Ui_Dialog
import os
import mysql.connector
from datetime import datetime, timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
# from
username = os.environ.get('db_user')
userpass = os.environ.get('db_pass')
conn = mysql.connector.connect(host="localhost", user=username, password=userpass, database="green")
cur = conn.cursor()
cur.execute("select * from lone_info where id = 1 and last_transaction_date = '2022-04-09' and Intrest = '2'")
data = cur.fetchall()
cur.close()
conn.commit()
conn.close()
out = [item for t in data for item in t]
class monthlydata:
    def get_forward_month_list(self):
        global monthis
        monthaddone = 2
        my_date = datetime(2022, (3) + monthaddone, 6)
        my_time = datetime.min.time()
        now = datetime.combine(my_date, my_time)
        monthis = my_date.strftime("%m")
        return ([(now + relativedelta(months=i)).strftime('%b') for i in range(12)])
    def amountval(self,monthis):
        global month_num
        month_num = (int(monthis) - 1)
        monthdata = out[7:31]
        monthno = []
        indexval = 0
        for i in range(len(monthdata)):
            if indexval <= 23:
                sub_list = [(monthdata[indexval])]
                monthno.append(sub_list)
                indexval = indexval + 2
        mn = int(month_num)

        start_month = monthno[mn - 1:12]
        lenofm = ((monthno[mn:12]))

        lenofm2 = (monthno[0:mn])
        res_list1 = [*lenofm, *lenofm2]
        print('\n')
        return (res_list1)
    def intrestrate(self,month_num):
        print('\n')
        monthdata = out[7:31]
        monthno = []
        monthno1 = []
        indexval = 0
        monthdata = out[7:31]
        monthno = []
        monthno1 = []
        indexval = 0
        for i in range(len(monthdata)):
            if indexval <= 24:

                if indexval == 0:

                    sub_list1 = [(monthdata[indexval])]
                    monthno1.append(sub_list1)
                    indexval = indexval + 1
                else:
                    sub_list = [(monthdata[indexval])]
                    monthno.append(sub_list)
                    indexval = indexval + 2
        mn = int(month_num)
        start_month = monthno[mn - 1:12]
        lenofm = (monthno[mn:12])
        lenofm2 = (monthno[0:mn])
        res_list2 = [*lenofm, *lenofm2]
        return res_list2
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        global monthlydata
        monthlist = (monthlydata.get_forward_month_list(self))
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 800)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.edittext_print_btn = QPushButton(Dialog)
        self.edittext_print_btn.setObjectName(u"edittext_print_btn")

        self.gridLayout_2.addWidget(self.edittext_print_btn, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    # def elmentslist(,list2,list3):
    #     self.list1 = month_name
    #     self.list2 =

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">		Green Thought Framers Club</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Date: 2022/2/2</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To: Firstname Middlename Lastname</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Addher No: 123456789012</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Total Lone: 8000</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Remainng Lone: 2000</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Month 		Amount 		Intrest Rate	 Total</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\"><span style=\" font-size:10pt;\">%s 		100 		2		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">February		100		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">March		100		2		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">April 		100		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">May 		100 		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">June 		100 		2"
                        " 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">July 		0 		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">August 		0 		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">September 	0 		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">October 		500 		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">November 	100 		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-b"
                        "ottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">December 	100 		2 		102</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Total 		1300 		24 		1488</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span></p></body></html>", None)%str('anme'))
        self.edittext_print_btn.setText(QCoreApplication.translate("Dialog", u"Print", None))
    # retranslateUi

