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
        Dialog.resize(489, 527)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setVerticalSpacing(15)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.collect_lone_no = QLineEdit(self.frame)
        self.collect_lone_no.setObjectName(u"collect_lone_no")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.collect_lone_no)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.collect_id = QLineEdit(self.frame)
        self.collect_id.setObjectName(u"collect_id")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.collect_id)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.collect_name = QLineEdit(self.frame)
        self.collect_name.setObjectName(u"collect_name")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.collect_name)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.collect_addher_no = QLineEdit(self.frame)
        self.collect_addher_no.setObjectName(u"collect_addher_no")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.collect_addher_no)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.collec_date = QDateEdit(self.frame)
        self.collec_date.setObjectName(u"collec_date")
        self.collec_date.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.collec_date)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.collect_amount = QLineEdit(self.frame)
        self.collect_amount.setObjectName(u"collect_amount")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.collect_amount)

        self.collect_collect = QPushButton(self.frame)
        self.collect_collect.setObjectName(u"collect_collect")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.collect_collect)

        self.lone_error = QLabel(self.frame)
        self.lone_error.setObjectName(u"lone_error")
        self.lone_error.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color:rgb(255, 0, 4)")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lone_error)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lone_trancation_no = QLineEdit(self.frame)
        self.lone_trancation_no.setObjectName(u"lone_trancation_no")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lone_trancation_no)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Lone No", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Addher No", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.collec_date.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/M/d", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.collect_collect.setText(QCoreApplication.translate("Dialog", u"collect", None))
        self.lone_error.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"trancation No", None))
    # retranslateUi

