# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lone.ui'
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
        Dialog.resize(600, 600)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setContentsMargins(-1, -1, 100, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(600, 40))
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_10 = QLineEdit(self.frame)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(600, 40))
        self.lineEdit_10.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(600, 40))
        self.lineEdit_2.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(600, 40))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(600, 40))
        self.lineEdit_3.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setWrapping(False)
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.dateEdit)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_26)

        self.lineEdit_11 = QLineEdit(self.frame)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(600, 40))
        self.lineEdit_11.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_27)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_11)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(600, 40))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.comboBox_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(90, 30))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.pushButton)

        self.lineEdit_12 = QLineEdit(self.frame)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(600, 40))
        self.lineEdit_12.setFont(font1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.lineEdit_12)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Addher No:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"amount", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"intrest rate", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))

        self.label_5.setText(QCoreApplication.translate("Dialog", u"Check NO:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/M/d", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Jamindar 1", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Jamindar 1", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Remark", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"remark 1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"remark 2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"remark 3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"remark 4", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Dialog", u"remark 5", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Dialog", u"remark 6", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Appove", None))
    # retranslateUi

