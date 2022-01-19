# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saving_account.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(533, 469)
        Dialog.setStyleSheet(u"\n"
"QDialog#Dialog{\n"
"	background-color: qlineargradient(spread:pad, x1:0.18408, y1:0.5, x2:0.995, y2:0.943, stop:0 rgba(141, 210, 12, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"QLineEdit{\n"
"border: 2px  solid rgb(112, 112, 112);\n"
"border-radius:10px;\n"
"color:#FFF;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"background-color:rgba(170, 255, 127,100);\n"
"}\n"
"QLineEdit{\n"
"	font: 75 12pt \"Verdana\";\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"")
        self.snamelabel_2 = QLabel(Dialog)
        self.snamelabel_2.setObjectName(u"snamelabel_2")
        self.snamelabel_2.setGeometry(QRect(10, 390, 131, 31))
        self.snamelabel_2.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")
        self.member_total_saving = QLabel(Dialog)
        self.member_total_saving.setObjectName(u"member_total_saving")
        self.member_total_saving.setGeometry(QRect(150, 390, 151, 31))
        self.member_total_saving.setStyleSheet(u"font: 75 italic 12pt \"Verdana\";\n"
"color:rgb(255, 122, 61);")
        self.error_4 = QLabel(Dialog)
        self.error_4.setObjectName(u"error_4")
        self.error_4.setGeometry(QRect(10, 290, 441, 31))
        self.error_4.setStyleSheet(u"font: 10pt \"Verdana\";\n"
"color:rgb(0, 102, 255)")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(12, 31, 71, 19))
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")
        self.sname = QLineEdit(Dialog)
        self.sname.setObjectName(u"sname")
        self.sname.setGeometry(QRect(160, 20, 351, 40))
        self.sname.setMinimumSize(QSize(50, 40))
        self.sname.setMaximumSize(QSize(500, 16777215))
        self.sname.setStyleSheet(u"")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 121, 19))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")
        self.saddher = QLineEdit(Dialog)
        self.saddher.setObjectName(u"saddher")
        self.saddher.setGeometry(QRect(160, 120, 351, 40))
        self.saddher.setMinimumSize(QSize(50, 40))
        self.saddher.setMaximumSize(QSize(500, 16777215))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 71, 19))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")
        self.sdate = QDateEdit(Dialog)
        self.sdate.setObjectName(u"sdate")
        self.sdate.setGeometry(QRect(160, 170, 241, 31))
        self.sdate.setMinimumSize(QSize(200, 30))
        self.sdate.setMaximumSize(QSize(300, 16777215))
        self.sdate.setCalendarPopup(True)
        self.snamelabel = QLabel(Dialog)
        self.snamelabel.setObjectName(u"snamelabel")
        self.snamelabel.setGeometry(QRect(10, 250, 111, 19))
        self.snamelabel.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")
        self.samount = QLineEdit(Dialog)
        self.samount.setObjectName(u"samount")
        self.samount.setGeometry(QRect(160, 240, 341, 40))
        self.samount.setMinimumSize(QSize(150, 40))
        self.samount.setMaximumSize(QSize(500, 16777215))
        self.sfind_btn = QPushButton(Dialog)
        self.sfind_btn.setObjectName(u"sfind_btn")
        self.sfind_btn.setGeometry(QRect(190, 70, 101, 28))
        self.sfind_btn.setMaximumSize(QSize(120, 40))
        self.scollect_btn = QPushButton(Dialog)
        self.scollect_btn.setObjectName(u"scollect_btn")
        self.scollect_btn.setGeometry(QRect(0, 330, 151, 41))
        self.sprint_btn = QPushButton(Dialog)
        self.sprint_btn.setObjectName(u"sprint_btn")
        self.sprint_btn.setGeometry(QRect(210, 330, 151, 41))
        QWidget.setTabOrder(self.sname, self.sfind_btn)
        QWidget.setTabOrder(self.sfind_btn, self.saddher)
        QWidget.setTabOrder(self.saddher, self.sdate)
        QWidget.setTabOrder(self.sdate, self.samount)
        QWidget.setTabOrder(self.samount, self.scollect_btn)
        QWidget.setTabOrder(self.scollect_btn, self.sprint_btn)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.snamelabel_2.setText(QCoreApplication.translate("Dialog", u"Total Saving", None))
        self.member_total_saving.setText("")
        self.error_4.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Addher No", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.sdate.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/M/d", None))
        self.snamelabel.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.sfind_btn.setText(QCoreApplication.translate("Dialog", u"Find", None))
        self.scollect_btn.setText(QCoreApplication.translate("Dialog", u"Collect", None))
        self.sprint_btn.setText(QCoreApplication.translate("Dialog", u"Print Invoice", None))
    # retranslateUi

