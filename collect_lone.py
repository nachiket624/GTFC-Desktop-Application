# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collect_lone.ui'
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
        Dialog.resize(745, 618)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lone_no = QLineEdit(Dialog)
        self.lone_no.setObjectName(u"lone_no")
        self.lone_no.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lone_no)

        self.find_btn = QPushButton(Dialog)
        self.find_btn.setObjectName(u"find_btn")
        self.find_btn.setMaximumSize(QSize(120, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.find_btn)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lone_name = QLineEdit(Dialog)
        self.lone_name.setObjectName(u"lone_name")
        self.lone_name.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lone_name)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.addhere_no = QLineEdit(Dialog)
        self.addhere_no.setObjectName(u"addhere_no")
        self.addhere_no.setMaximumSize(QSize(400, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.addhere_no)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.collect_date = QDateEdit(Dialog)
        self.collect_date.setObjectName(u"collect_date")
        self.collect_date.setMaximumSize(QSize(100, 16777215))
        self.collect_date.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.collect_date)

        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.radioButton)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.collect_ammount = QLineEdit(Dialog)
        self.collect_ammount.setObjectName(u"collect_ammount")
        self.collect_ammount.setMaximumSize(QSize(400, 16777215))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.collect_ammount)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.Interst_rate = QLineEdit(Dialog)
        self.Interst_rate.setObjectName(u"Interst_rate")
        self.Interst_rate.setMaximumSize(QSize(400, 16777215))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.Interst_rate)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.print_btn = QPushButton(Dialog)
        self.print_btn.setObjectName(u"print_btn")

        self.gridLayout.addWidget(self.print_btn, 0, 0, 1, 1)

        self.collect_lone_btn = QPushButton(Dialog)
        self.collect_lone_btn.setObjectName(u"collect_lone_btn")

        self.gridLayout.addWidget(self.collect_lone_btn, 0, 1, 1, 1)


        self.formLayout.setLayout(9, QFormLayout.FieldRole, self.gridLayout)

        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(10, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(11, 0, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 300))
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setRowCount(12)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.tableWidget)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Lone No", None))
        self.find_btn.setText(QCoreApplication.translate("Dialog", u"Find", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Addher No", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.collect_date.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/M/d", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"System Date", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Interst", None))
        self.print_btn.setText(QCoreApplication.translate("Dialog", u"Print Invoice", None))
        self.collect_lone_btn.setText(QCoreApplication.translate("Dialog", u"collect", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Month", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Amount", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Interest", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Total", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"January", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u" February", None));
        ___qtablewidgetitem7 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u" March", None));
        ___qtablewidgetitem8 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"April", None));
        ___qtablewidgetitem9 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"May", None));
        ___qtablewidgetitem10 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"June", None));
        ___qtablewidgetitem11 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"July", None));
        ___qtablewidgetitem12 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"August", None));
        ___qtablewidgetitem13 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"September", None));
        ___qtablewidgetitem14 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"October", None));
        ___qtablewidgetitem15 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"November", None));
        ___qtablewidgetitem16 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"December", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

