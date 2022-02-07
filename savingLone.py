# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'savingLone.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1099, 904)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)


        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_15)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_16)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_17)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_18)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_19)


        self.gridLayout_6.addLayout(self.formLayout, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateEdit)


        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.gridLayout_6.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.gridLayout_6.setRowMinimumHeight(2, 2)

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 280, -1)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.sname_3 = QLineEdit(self.frame_2)
        self.sname_3.setObjectName(u"sname_3")
        self.sname_3.setMaximumSize(QSize(120, 16777215))
        self.sname_3.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.sname_3)

        self.sfind_btn = QPushButton(self.frame_2)
        self.sfind_btn.setObjectName(u"sfind_btn")
        self.sfind_btn.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_2.addWidget(self.sfind_btn)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.scollect_btn = QPushButton(self.frame_2)
        self.scollect_btn.setObjectName(u"scollect_btn")

        self.horizontalLayout.addWidget(self.scollect_btn)


        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.sname = QLineEdit(self.frame_2)
        self.sname.setObjectName(u"sname")
        self.sname.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sname)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.saddher = QLineEdit(self.frame_2)
        self.saddher.setObjectName(u"saddher")
        self.saddher.setMaximumSize(QSize(500, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.saddher)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.sdate = QDateEdit(self.frame_2)
        self.sdate.setObjectName(u"sdate")
        self.sdate.setMinimumSize(QSize(200, 30))
        self.sdate.setMaximumSize(QSize(300, 16777215))
        self.sdate.setCalendarPopup(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.sdate)

        self.snamelabel = QLabel(self.frame_2)
        self.snamelabel.setObjectName(u"snamelabel")
        self.snamelabel.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.snamelabel)

        self.samount = QLineEdit(self.frame_2)
        self.samount.setObjectName(u"samount")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.samount)


        self.gridLayout_4.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.snamelabel_2 = QLabel(self.frame_2)
        self.snamelabel_2.setObjectName(u"snamelabel_2")
        self.snamelabel_2.setStyleSheet(u"QLabel{\n"
"	font: 75 14pt \"Arial\";\n"
"}")

        self.horizontalLayout_3.addWidget(self.snamelabel_2)

        self.member_total_saving = QLabel(self.frame_2)
        self.member_total_saving.setObjectName(u"member_total_saving")
        self.member_total_saving.setStyleSheet(u"font: 75 italic 12pt \"Verdana\";\n"
"color:rgb(255, 122, 61);")

        self.horizontalLayout_3.addWidget(self.member_total_saving)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 1, 1, 1, 1)

        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 120))

        self.gridLayout_5.addWidget(self.label_20, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_13 = QGridLayout(self.tab_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_21 = QLabel(self.tab_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 120))

        self.gridLayout_13.addWidget(self.label_21, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 280, -1)
        self.label_38 = QLabel(self.tab_2)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_6.addWidget(self.label_38)

        self.LoneNo = QLineEdit(self.tab_2)
        self.LoneNo.setObjectName(u"LoneNo")
        self.LoneNo.setMaximumSize(QSize(120, 16777215))
        self.LoneNo.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.LoneNo)

        self.saving_find_btn = QPushButton(self.tab_2)
        self.saving_find_btn.setObjectName(u"saving_find_btn")
        self.saving_find_btn.setMaximumSize(QSize(120, 40))

        self.horizontalLayout_6.addWidget(self.saving_find_btn)


        self.gridLayout_9.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget_2.rowCount() < 12):
            self.tableWidget_2.setRowCount(12)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setItem(6, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setItem(7, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setItem(8, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setItem(9, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setItem(10, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setItem(11, 0, __qtablewidgetitem16)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(0, 300))
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_2.setRowCount(12)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(120)

        self.gridLayout_11.addWidget(self.tableWidget_2, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_11, 2, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_22 = QLabel(self.tab_2)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.label_44 = QLabel(self.tab_2)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_44)

        self.label_45 = QLabel(self.tab_2)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_45)

        self.label_46 = QLabel(self.tab_2)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.label_46)

        self.label_47 = QLabel(self.tab_2)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_8.setWidget(5, QFormLayout.LabelRole, self.label_47)

        self.label_48 = QLabel(self.tab_2)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_48)

        self.label_49 = QLabel(self.tab_2)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.label_49)

        self.label_50 = QLabel(self.tab_2)
        self.label_50.setObjectName(u"label_50")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.label_50)

        self.label_51 = QLabel(self.tab_2)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.label_51)

        self.label_52 = QLabel(self.tab_2)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.label_52)

        self.label_53 = QLabel(self.tab_2)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.label_53)

        self.label_54 = QLabel(self.tab_2)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.label_54)


        self.gridLayout_12.addLayout(self.formLayout_8, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_12, 1, 1, 1, 1)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_39 = QLabel(self.tab_2)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_39)

        self.lone_name_2 = QLineEdit(self.tab_2)
        self.lone_name_2.setObjectName(u"lone_name_2")
        self.lone_name_2.setMinimumSize(QSize(400, 0))
        self.lone_name_2.setMaximumSize(QSize(100, 16777215))

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lone_name_2)

        self.label_40 = QLabel(self.tab_2)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_40)

        self.addhere_no_2 = QLineEdit(self.tab_2)
        self.addhere_no_2.setObjectName(u"addhere_no_2")
        self.addhere_no_2.setMaximumSize(QSize(400, 16777215))

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.addhere_no_2)

        self.label_41 = QLabel(self.tab_2)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_41)

        self.collect_date_2 = QDateEdit(self.tab_2)
        self.collect_date_2.setObjectName(u"collect_date_2")
        self.collect_date_2.setMaximumSize(QSize(100, 16777215))
        self.collect_date_2.setCalendarPopup(True)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.collect_date_2)

        self.label_42 = QLabel(self.tab_2)
        self.label_42.setObjectName(u"label_42")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_42)

        self.collect_ammount_2 = QLineEdit(self.tab_2)
        self.collect_ammount_2.setObjectName(u"collect_ammount_2")
        self.collect_ammount_2.setMaximumSize(QSize(400, 16777215))

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.collect_ammount_2)

        self.label_43 = QLabel(self.tab_2)
        self.label_43.setObjectName(u"label_43")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.label_43)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.collect_lone_btn_2 = QPushButton(self.tab_2)
        self.collect_lone_btn_2.setObjectName(u"collect_lone_btn_2")

        self.gridLayout_10.addWidget(self.collect_lone_btn_2, 0, 0, 1, 1)


        self.formLayout_7.setLayout(5, QFormLayout.FieldRole, self.gridLayout_10)

        self.label_55 = QLabel(self.tab_2)
        self.label_55.setObjectName(u"label_55")

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.label_55)


        self.gridLayout_9.addLayout(self.formLayout_7, 1, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_9, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Analytics</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Total Saving</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Total loan collect</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Total interst </span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Total</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Approve LoneSaving</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.sfind_btn.setText(QCoreApplication.translate("Dialog", u"Find", None))
        self.scollect_btn.setText(QCoreApplication.translate("Dialog", u"Collect", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Addher No", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.sdate.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/M/d", None))
        self.snamelabel.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.snamelabel_2.setText(QCoreApplication.translate("Dialog", u"Total Saving", None))
        self.member_total_saving.setText("")
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; text-decoration: underline;\">Saving</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; text-decoration: underline;\">Loan</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("Dialog", u"LoneSaving No", None))
        self.saving_find_btn.setText(QCoreApplication.translate("Dialog", u"Find", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Month", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Amount", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Interest", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Total", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"January", None));
        ___qtablewidgetitem6 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u" February", None));
        ___qtablewidgetitem7 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u" March", None));
        ___qtablewidgetitem8 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"April", None));
        ___qtablewidgetitem9 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"May", None));
        ___qtablewidgetitem10 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"June", None));
        ___qtablewidgetitem11 = self.tableWidget_2.item(6, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"July", None));
        ___qtablewidgetitem12 = self.tableWidget_2.item(7, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"August", None));
        ___qtablewidgetitem13 = self.tableWidget_2.item(8, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"September", None));
        ___qtablewidgetitem14 = self.tableWidget_2.item(9, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"October", None));
        ___qtablewidgetitem15 = self.tableWidget_2.item(10, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"November", None));
        ___qtablewidgetitem16 = self.tableWidget_2.item(11, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"December", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_22.setText(QCoreApplication.translate("Dialog", u"LoneSaving Taken", None))
        self.label_44.setText(QCoreApplication.translate("Dialog", u"Remaning LoneSaving", None))
        self.label_45.setText(QCoreApplication.translate("Dialog", u"Total LoneSaving Pay", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"Total Intrest Pay", None))
        self.label_47.setText(QCoreApplication.translate("Dialog", u"tTotal Intrest Paid", None))
        self.label_48.setText(QCoreApplication.translate("Dialog", u"Remaning Intrest Pay", None))
        self.label_49.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_50.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_51.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_53.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_54.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_40.setText(QCoreApplication.translate("Dialog", u"Addher No", None))
        self.label_41.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.collect_date_2.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/M/d", None))
        self.label_42.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.label_43.setText(QCoreApplication.translate("Dialog", u"Interst", None))
        self.collect_lone_btn_2.setText(QCoreApplication.translate("Dialog", u"collect", None))
        self.label_55.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
    # retranslateUi

