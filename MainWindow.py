# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import dashboard_rc
import manage_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1140, 697)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(50, 40))
        MainWindow.setStyleSheet(u"background-color:#ecf2f7")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"BACKGROUND-COLOR:#354052")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 100, -1, 0)
        self.dashboard_btn = QPushButton(self.frame)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        sizePolicy1.setHeightForWidth(self.dashboard_btn.sizePolicy().hasHeightForWidth())
        self.dashboard_btn.setSizePolicy(sizePolicy1)
        self.dashboard_btn.setMinimumSize(QSize(0, 0))
        self.dashboard_btn.setMaximumSize(QSize(7567, 40))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(10)
        font1.setKerning(True)
        self.dashboard_btn.setFont(font1)
        self.dashboard_btn.setLayoutDirection(Qt.RightToLeft)
        self.dashboard_btn.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 87 11pt \"Arial Black\";\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-colora: rgb(85, 0, 255,0);\n"
"	color: rgb(218, 145, 0)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:  rgba(13, 9, 36,0);;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/image/dashboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon)
        self.dashboard_btn.setIconSize(QSize(35, 40))
        self.dashboard_btn.setAutoDefault(False)
        self.dashboard_btn.setFlat(False)

        self.verticalLayout.addWidget(self.dashboard_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Manage_btn = QPushButton(self.frame)
        self.Manage_btn.setObjectName(u"Manage_btn")
        sizePolicy1.setHeightForWidth(self.Manage_btn.sizePolicy().hasHeightForWidth())
        self.Manage_btn.setSizePolicy(sizePolicy1)
        self.Manage_btn.setMinimumSize(QSize(120, 50))
        self.Manage_btn.setMaximumSize(QSize(3423, 50))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(10)
        font2.setKerning(True)
        self.Manage_btn.setFont(font2)
        self.Manage_btn.setLayoutDirection(Qt.RightToLeft)
        self.Manage_btn.setStyleSheet(u"QPushButton {\n"
"font: 87 12pt \"Arial Black\";\n"
"\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-colora: rgb(85, 0, 255,0);\n"
"	color: rgb(218, 145, 0)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/image/manage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Manage_btn.setIcon(icon1)
        self.Manage_btn.setIconSize(QSize(40, 40))
        self.Manage_btn.setAutoDefault(False)
        self.Manage_btn.setFlat(False)

        self.verticalLayout.addWidget(self.Manage_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.view_btn = QPushButton(self.frame)
        self.view_btn.setObjectName(u"view_btn")
        sizePolicy1.setHeightForWidth(self.view_btn.sizePolicy().hasHeightForWidth())
        self.view_btn.setSizePolicy(sizePolicy1)
        self.view_btn.setMinimumSize(QSize(120, 50))
        self.view_btn.setMaximumSize(QSize(3242, 50))
        self.view_btn.setFont(font2)
        self.view_btn.setLayoutDirection(Qt.RightToLeft)
        self.view_btn.setStyleSheet(u"QPushButton {\n"
"font: 87 12pt \"Arial Black\";\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-colora: rgb(85, 0, 255,0);\n"
"	color: rgb(218, 145, 0)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/image/icons8-view-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_btn.setIcon(icon2)
        self.view_btn.setIconSize(QSize(40, 40))
        self.view_btn.setAutoDefault(False)
        self.view_btn.setFlat(False)

        self.verticalLayout.addWidget(self.view_btn, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(120, 50))
        self.pushButton_8.setMaximumSize(QSize(32423, 40))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"font: 87 12pt \"Arial Black\";\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-colora: rgb(85, 0, 255,0);\n"
"	color: rgb(218, 145, 0)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/image/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(40, 40))
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_8, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:#ecf2f7")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.dashboard_page.setStyleSheet(u"background-color:#ecf2f7")
        self.gridLayout_16 = QGridLayout(self.dashboard_page)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(self.dashboard_page)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"QWidget#widget1{background-color:background-color:#ecf2f7}")
        self.gridLayout_22 = QGridLayout(self.widget1)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_5 = QFrame(self.widget1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color:rgba(255, 255, 255, 190)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color:rgba(0, 0, 0, 150);\n"
"\n"
"font: 10pt \"Arial\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_18)

        self.label_41 = QLabel(self.frame_5)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"color:rgba(0, 0, 0, 150);\n"
"\n"
"font: 10pt \"Arial\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_41)

        self.label_42 = QLabel(self.frame_5)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_42)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color:rgba(0, 0, 0, 150);\n"
"\n"
"font: 10pt \"Arial\";")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_22)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color:rgba(0, 0, 0, 150);\n"
"\n"
"font: 10pt \"Arial\";")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_20)

        self.label_43 = QLabel(self.frame_5)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color:rgba(0, 0, 0, 150);\n"
"\n"
"font: 10pt \"Arial\";")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_43)

        self.label_44 = QLabel(self.frame_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_44)

        self.label_45 = QLabel(self.frame_5)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color:rgba(0, 0, 0, 150);\n"
"\n"
"font: 10pt \"Arial\";")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_45)

        self.label_54 = QLabel(self.frame_5)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_54)

        self.label_55 = QLabel(self.frame_5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color:rgba(0, 0, 0, 150);\n"
"\n"
"font: 10pt \"Arial\";")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_55)

        self.label_56 = QLabel(self.frame_5)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 87 10pt \"Arial Black\";")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_56)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.gridLayout_21.addWidget(self.frame_5, 2, 0, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.total_lone = QLabel(self.widget1)
        self.total_lone.setObjectName(u"total_lone")
        self.total_lone.setStyleSheet(u"padding: 40px;\n"
"font: 75 22pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:#4fa5e1;\n"
"\n"
"border-radius: 30px;")

        self.gridLayout_17.addWidget(self.total_lone, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 453))
        self.label_3.setStyleSheet(u"QLabel#label_3{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"opacity: 0;\n"
"\n"
"}")

        self.gridLayout_17.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel#label_4{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"opacity: 0;\n"
"\n"
"}")

        self.gridLayout_17.addWidget(self.label_4, 0, 1, 1, 1)

        self.total_member = QLabel(self.widget1)
        self.total_member.setObjectName(u"total_member")
        self.total_member.setStyleSheet(u"padding: 40px;\n"
"font: 75 22pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:#4fa5e1;\n"
"\n"
"border-radius: 30px;")
        self.total_member.setScaledContents(True)

        self.gridLayout_17.addWidget(self.total_member, 1, 0, 1, 1)

        self.label_15 = QLabel(self.widget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 500))
        self.label_15.setStyleSheet(u"QLabel#label_15\n"
"{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"opacity: 0;\n"
"\n"
"}")

        self.gridLayout_17.addWidget(self.label_15, 0, 2, 1, 1)

        self.label_16 = QLabel(self.widget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel#label_16\n"
"{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"opacity: 0;\n"
"\n"
"}")

        self.gridLayout_17.addWidget(self.label_16, 0, 3, 1, 1)

        self.total_lone_3 = QLabel(self.widget1)
        self.total_lone_3.setObjectName(u"total_lone_3")
        self.total_lone_3.setStyleSheet(u"padding: 40px;\n"
"font: 75 22pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:#4fa5e1;\n"
"\n"
"border-radius: 30px;")

        self.gridLayout_17.addWidget(self.total_lone_3, 1, 2, 1, 1)

        self.total_lone_4 = QLabel(self.widget1)
        self.total_lone_4.setObjectName(u"total_lone_4")
        self.total_lone_4.setStyleSheet(u"padding: 40px;\n"
"font: 75 22pt \"MS Sans Serif\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:#4fa5e1;\n"
"\n"
"border-radius: 30px;")

        self.gridLayout_17.addWidget(self.total_lone_4, 1, 3, 1, 1)

        self.gridLayout_17.setRowStretch(1, 2)

        self.gridLayout_21.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_7, 1, 0, 1, 1)


        self.gridLayout_22.addLayout(self.gridLayout_21, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget1, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.table_view = QWidget()
        self.table_view.setObjectName(u"table_view")
        self.gridLayout_4 = QGridLayout(self.table_view)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.table_view)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 14):
            self.tableWidget.setColumnCount(14)
        if (self.tableWidget.rowCount() < 100):
            self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #f1f1f1;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.WinPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_9.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.table_view)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.pageManage = QWidget()
        self.pageManage.setObjectName(u"pageManage")
        self.pageManage.setStyleSheet(u"QPushButton{padding: 40px;\n"
"	font: 87 10pt \"Arial Black\";\n"
"color:rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"background-color:#ffa872;}")
        self.gridLayout_6 = QGridLayout(self.pageManage)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(10, 10, 5, 5)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setHorizontalSpacing(20)
        self.gridLayout_23.setVerticalSpacing(40)
        self.gridLayout_23.setContentsMargins(10, 10, 10, 10)
        self.remove_member_btn = QPushButton(self.pageManage)
        self.remove_member_btn.setObjectName(u"remove_member_btn")
        sizePolicy1.setHeightForWidth(self.remove_member_btn.sizePolicy().hasHeightForWidth())
        self.remove_member_btn.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/manage_icon/image/manage/remove member - Copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_member_btn.setIcon(icon4)
        self.remove_member_btn.setIconSize(QSize(150, 150))

        self.gridLayout_23.addWidget(self.remove_member_btn, 0, 1, 1, 1)

        self.update_member_btn = QPushButton(self.pageManage)
        self.update_member_btn.setObjectName(u"update_member_btn")
        sizePolicy1.setHeightForWidth(self.update_member_btn.sizePolicy().hasHeightForWidth())
        self.update_member_btn.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u":/manage_icon/image/manage/Update Member.png", QSize(), QIcon.Normal, QIcon.Off)
        self.update_member_btn.setIcon(icon5)
        self.update_member_btn.setIconSize(QSize(150, 150))

        self.gridLayout_23.addWidget(self.update_member_btn, 0, 2, 1, 1)

        self.collect_lone_btn = QPushButton(self.pageManage)
        self.collect_lone_btn.setObjectName(u"collect_lone_btn")
        sizePolicy1.setHeightForWidth(self.collect_lone_btn.sizePolicy().hasHeightForWidth())
        self.collect_lone_btn.setSizePolicy(sizePolicy1)

        self.gridLayout_23.addWidget(self.collect_lone_btn, 1, 0, 1, 1)

        self.give_lone = QPushButton(self.pageManage)
        self.give_lone.setObjectName(u"give_lone")
        sizePolicy1.setHeightForWidth(self.give_lone.sizePolicy().hasHeightForWidth())
        self.give_lone.setSizePolicy(sizePolicy1)

        self.gridLayout_23.addWidget(self.give_lone, 1, 1, 1, 1)

        self.collection = QPushButton(self.pageManage)
        self.collection.setObjectName(u"collection")
        sizePolicy1.setHeightForWidth(self.collection.sizePolicy().hasHeightForWidth())
        self.collection.setSizePolicy(sizePolicy1)

        self.gridLayout_23.addWidget(self.collection, 1, 2, 1, 1)

        self.new_member_btn = QPushButton(self.pageManage)
        self.new_member_btn.setObjectName(u"new_member_btn")
        sizePolicy1.setHeightForWidth(self.new_member_btn.sizePolicy().hasHeightForWidth())
        self.new_member_btn.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily(u"Arial Black")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(10)
        self.new_member_btn.setFont(font3)
        self.new_member_btn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/manage_icon/image/manage/AddMember.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_member_btn.setIcon(icon6)
        self.new_member_btn.setIconSize(QSize(150, 150))

        self.gridLayout_23.addWidget(self.new_member_btn, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_23, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.pageManage)
        self.UpdateInformation = QWidget()
        self.UpdateInformation.setObjectName(u"UpdateInformation")
        self.gridLayout_15 = QGridLayout(self.UpdateInformation)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.groupBox_4 = QGroupBox(self.UpdateInformation)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font4 = QFont()
        font4.setFamily(u"Verdana")
        font4.setPointSize(10)
        self.groupBox_4.setFont(font4)
        self.gridLayout_14 = QGridLayout(self.groupBox_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_6.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_6.setLabelAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.formLayout_6.setFormAlignment(Qt.AlignCenter)
        self.formLayout_6.setHorizontalSpacing(7)
        self.formLayout_6.setVerticalSpacing(20)
        self.formLayout_6.setContentsMargins(7, 7, 7, 7)
        self.label_40 = QLabel(self.groupBox_4)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_40)

        self.id_2 = QLineEdit(self.groupBox_4)
        self.id_2.setObjectName(u"id_2")
        self.id_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.id_2.sizePolicy().hasHeightForWidth())
        self.id_2.setSizePolicy(sizePolicy1)
        self.id_2.setMaximumSize(QSize(80, 80))
        self.id_2.setLayoutDirection(Qt.LeftToRight)
        self.id_2.setAlignment(Qt.AlignCenter)
        self.id_2.setReadOnly(False)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.id_2)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.firstname_2 = QLineEdit(self.groupBox_4)
        self.firstname_2.setObjectName(u"firstname_2")
        self.firstname_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.firstname_2.sizePolicy().hasHeightForWidth())
        self.firstname_2.setSizePolicy(sizePolicy1)
        self.firstname_2.setMaximumSize(QSize(500, 16777215))
        self.firstname_2.setLayoutDirection(Qt.LeftToRight)
        self.firstname_2.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.firstname_2)

        self.label_33 = QLabel(self.groupBox_4)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_33)

        self.middlename_2 = QLineEdit(self.groupBox_4)
        self.middlename_2.setObjectName(u"middlename_2")
        self.middlename_2.setMaximumSize(QSize(500, 16777215))
        self.middlename_2.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.middlename_2)

        self.label_30 = QLabel(self.groupBox_4)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_30)

        self.lastname_2 = QLineEdit(self.groupBox_4)
        self.lastname_2.setObjectName(u"lastname_2")
        self.lastname_2.setMaximumSize(QSize(500, 16777215))
        self.lastname_2.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.lastname_2)

        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_6.setWidget(5, QFormLayout.LabelRole, self.label_27)

        self.bloodgroup_2 = QComboBox(self.groupBox_4)
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.addItem("")
        self.bloodgroup_2.setObjectName(u"bloodgroup_2")
        self.bloodgroup_2.setMaximumSize(QSize(500, 16777215))

        self.formLayout_6.setWidget(5, QFormLayout.FieldRole, self.bloodgroup_2)

        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_6.setWidget(6, QFormLayout.LabelRole, self.label_28)

        self.nomine_2 = QLineEdit(self.groupBox_4)
        self.nomine_2.setObjectName(u"nomine_2")
        self.nomine_2.setMaximumSize(QSize(500, 16777215))
        self.nomine_2.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(6, QFormLayout.FieldRole, self.nomine_2)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"")

        self.formLayout_6.setWidget(7, QFormLayout.LabelRole, self.label_35)

        self.dob_2 = QDateEdit(self.groupBox_4)
        self.dob_2.setObjectName(u"dob_2")
        self.dob_2.setMaximumSize(QSize(500, 16777215))
        self.dob_2.setCalendarPopup(True)

        self.formLayout_6.setWidget(7, QFormLayout.FieldRole, self.dob_2)

        self.label_38 = QLabel(self.groupBox_4)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_6.setWidget(8, QFormLayout.LabelRole, self.label_38)

        self.doj_2 = QDateEdit(self.groupBox_4)
        self.doj_2.setObjectName(u"doj_2")
        self.doj_2.setMaximumSize(QSize(500, 16777215))
        self.doj_2.setCalendarPopup(True)

        self.formLayout_6.setWidget(8, QFormLayout.FieldRole, self.doj_2)

        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_6.setWidget(9, QFormLayout.LabelRole, self.label_29)

        self.addhernumber_2 = QLineEdit(self.groupBox_4)
        self.addhernumber_2.setObjectName(u"addhernumber_2")
        self.addhernumber_2.setMaximumSize(QSize(500, 16777215))
        self.addhernumber_2.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(9, QFormLayout.FieldRole, self.addhernumber_2)

        self.label_39 = QLabel(self.groupBox_4)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_6.setWidget(10, QFormLayout.LabelRole, self.label_39)

        self.accountno_2 = QLineEdit(self.groupBox_4)
        self.accountno_2.setObjectName(u"accountno_2")
        self.accountno_2.setMaximumSize(QSize(500, 16777215))
        self.accountno_2.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(10, QFormLayout.FieldRole, self.accountno_2)

        self.search = QPushButton(self.groupBox_4)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(186, 40))
        self.search.setMaximumSize(QSize(150, 16777215))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.search)


        self.gridLayout_14.addLayout(self.formLayout_6, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.UpdateInformation)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font4)
        self.gridLayout_13 = QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_9.setHorizontalSpacing(7)
        self.formLayout_9.setVerticalSpacing(30)
        self.formLayout_9.setContentsMargins(7, 7, 7, 7)
        self.label_50 = QLabel(self.groupBox_3)
        self.label_50.setObjectName(u"label_50")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_50)

        self.mobile1_2 = QLineEdit(self.groupBox_3)
        self.mobile1_2.setObjectName(u"mobile1_2")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.mobile1_2)

        self.label_51 = QLabel(self.groupBox_3)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_51)

        self.mobile2_2 = QLineEdit(self.groupBox_3)
        self.mobile2_2.setObjectName(u"mobile2_2")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.mobile2_2)

        self.label_52 = QLabel(self.groupBox_3)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_52)

        self.email_2 = QLineEdit(self.groupBox_3)
        self.email_2.setObjectName(u"email_2")

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.email_2)

        self.label_53 = QLabel(self.groupBox_3)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.label_53)

        self.balance_2 = QLineEdit(self.groupBox_3)
        self.balance_2.setObjectName(u"balance_2")

        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.balance_2)

        self.addinfo_2 = QPushButton(self.groupBox_3)
        self.addinfo_2.setObjectName(u"addinfo_2")

        self.formLayout_9.setWidget(4, QFormLayout.FieldRole, self.addinfo_2)

        self.error_2 = QLabel(self.groupBox_3)
        self.error_2.setObjectName(u"error_2")
        self.error_2.setStyleSheet(u"font: 10pt \"Verdana\";\n"
"color:rgb(255, 0, 0)")

        self.formLayout_9.setWidget(5, QFormLayout.FieldRole, self.error_2)


        self.gridLayout_13.addLayout(self.formLayout_9, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.label_7 = QLabel(self.UpdateInformation)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(1200, 40))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_7.setFont(font5)

        self.gridLayout_15.addWidget(self.label_7, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.UpdateInformation)
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.gridLayout_7 = QGridLayout(self.page_view)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.loneview_btn = QPushButton(self.page_view)
        self.loneview_btn.setObjectName(u"loneview_btn")
        self.loneview_btn.setMinimumSize(QSize(186, 300))
        self.loneview_btn.setMaximumSize(QSize(300, 300))
        font6 = QFont()
        font6.setFamily(u"Verdana")
        font6.setBold(True)
        font6.setItalic(False)
        font6.setWeight(75)
        self.loneview_btn.setFont(font6)
        self.loneview_btn.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.loneview_btn, 0, 1, 1, 1)

        self.transaction_detail_btn = QPushButton(self.page_view)
        self.transaction_detail_btn.setObjectName(u"transaction_detail_btn")
        self.transaction_detail_btn.setMinimumSize(QSize(186, 300))
        self.transaction_detail_btn.setMaximumSize(QSize(300, 300))
        self.transaction_detail_btn.setFont(font6)
        self.transaction_detail_btn.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.transaction_detail_btn, 0, 2, 1, 1)

        self.viewall_btn = QPushButton(self.page_view)
        self.viewall_btn.setObjectName(u"viewall_btn")
        self.viewall_btn.setMinimumSize(QSize(186, 300))
        self.viewall_btn.setMaximumSize(QSize(300, 300))
        self.viewall_btn.setFont(font6)
        self.viewall_btn.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.viewall_btn, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_view)
        self.page_addnewmember = QWidget()
        self.page_addnewmember.setObjectName(u"page_addnewmember")
        self.gridLayout_5 = QGridLayout(self.page_addnewmember)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.page_addnewmember)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font4)
        self.gridLayout_8 = QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_5.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_5.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_5.setFormAlignment(Qt.AlignCenter)
        self.formLayout_5.setHorizontalSpacing(7)
        self.formLayout_5.setVerticalSpacing(30)
        self.formLayout_5.setContentsMargins(7, 7, 7, 7)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.firstname = QLineEdit(self.groupBox)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.firstname.sizePolicy().hasHeightForWidth())
        self.firstname.setSizePolicy(sizePolicy1)
        self.firstname.setMaximumSize(QSize(500, 16777215))
        self.firstname.setLayoutDirection(Qt.LeftToRight)
        self.firstname.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.firstname)

        self.label_31 = QLabel(self.groupBox)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_31)

        self.middlename = QLineEdit(self.groupBox)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setMaximumSize(QSize(500, 16777215))
        self.middlename.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.middlename)

        self.lastname = QLineEdit(self.groupBox)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setMaximumSize(QSize(500, 16777215))
        self.lastname.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lastname)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_23)

        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_24)

        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_32)

        self.label_34 = QLabel(self.groupBox)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.label_34)

        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.label_25)

        self.addhernumber = QLineEdit(self.groupBox)
        self.addhernumber.setObjectName(u"addhernumber")
        self.addhernumber.setMaximumSize(QSize(500, 16777215))
        self.addhernumber.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.addhernumber)

        self.label_36 = QLabel(self.groupBox)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.label_36)

        self.accountno = QLineEdit(self.groupBox)
        self.accountno.setObjectName(u"accountno")
        self.accountno.setMaximumSize(QSize(500, 16777215))
        self.accountno.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.accountno)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_26)

        self.nomine = QLineEdit(self.groupBox)
        self.nomine.setObjectName(u"nomine")
        self.nomine.setMaximumSize(QSize(500, 16777215))
        self.nomine.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.nomine)

        self.label_37 = QLabel(self.groupBox)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.id = QLineEdit(self.groupBox)
        self.id.setObjectName(u"id")
        self.id.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy1)
        self.id.setMaximumSize(QSize(80, 80))
        self.id.setLayoutDirection(Qt.LeftToRight)
        self.id.setAlignment(Qt.AlignCenter)
        self.id.setReadOnly(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.id)

        self.dob = QDateEdit(self.groupBox)
        self.dob.setObjectName(u"dob")
        self.dob.setMaximumSize(QSize(500, 16777215))
        self.dob.setCalendarPopup(True)

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.dob)

        self.doj = QDateEdit(self.groupBox)
        self.doj.setObjectName(u"doj")
        self.doj.setMaximumSize(QSize(500, 16777215))
        self.doj.setCalendarPopup(True)

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.doj)

        self.bloodgroup = QComboBox(self.groupBox)
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.setObjectName(u"bloodgroup")
        self.bloodgroup.setMaximumSize(QSize(500, 16777215))

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.bloodgroup)


        self.gridLayout_8.addLayout(self.formLayout_5, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_addnewmember)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font4)
        self.gridLayout_10 = QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_8.setHorizontalSpacing(7)
        self.formLayout_8.setVerticalSpacing(30)
        self.formLayout_8.setContentsMargins(7, 7, 7, 7)
        self.label_46 = QLabel(self.groupBox_2)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_46)

        self.mobile1 = QLineEdit(self.groupBox_2)
        self.mobile1.setObjectName(u"mobile1")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.mobile1)

        self.label_47 = QLabel(self.groupBox_2)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_47)

        self.mobile2 = QLineEdit(self.groupBox_2)
        self.mobile2.setObjectName(u"mobile2")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.mobile2)

        self.label_48 = QLabel(self.groupBox_2)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_48)

        self.email = QLineEdit(self.groupBox_2)
        self.email.setObjectName(u"email")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.email)

        self.label_49 = QLabel(self.groupBox_2)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_49)

        self.error = QLabel(self.groupBox_2)
        self.error.setObjectName(u"error")
        self.error.setStyleSheet(u"font: 10pt \"Verdana\";\n"
"color:rgb(255, 0, 0)")

        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.error)

        self.addinfo = QPushButton(self.groupBox_2)
        self.addinfo.setObjectName(u"addinfo")

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.addinfo)

        self.balance = QLineEdit(self.groupBox_2)
        self.balance.setObjectName(u"balance")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.balance)


        self.gridLayout_10.addLayout(self.formLayout_8, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_addnewmember)
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.stackedWidget.addWidget(self.setting)
        self.pagelone = QWidget()
        self.pagelone.setObjectName(u"pagelone")
        self.gridLayout_27 = QGridLayout(self.pagelone)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.label_10 = QLabel(self.pagelone)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.horizontalLayout.addWidget(self.label_10)

        self.lone_no = QLabel(self.pagelone)
        self.lone_no.setObjectName(u"lone_no")

        self.horizontalLayout.addWidget(self.lone_no)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_11.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13 = QLabel(self.pagelone)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.lone_ID = QLineEdit(self.pagelone)
        self.lone_ID.setObjectName(u"lone_ID")
        self.lone_ID.setMinimumSize(QSize(0, 30))
        self.lone_ID.setMaximumSize(QSize(150, 20))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lone_ID)

        self.pushButton = QPushButton(self.pagelone)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(150, 16777215))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.pushButton)

        self.label_11 = QLabel(self.pagelone)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.name = QLineEdit(self.pagelone)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 30))
        self.name.setMaximumSize(QSize(800, 16777215))

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.name)

        self.label_9 = QLabel(self.pagelone)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.addherno = QLineEdit(self.pagelone)
        self.addherno.setObjectName(u"addherno")
        self.addherno.setMinimumSize(QSize(0, 30))
        self.addherno.setMaximumSize(QSize(800, 16777215))

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.addherno)

        self.label_12 = QLabel(self.pagelone)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_12)

        self.amount = QLineEdit(self.pagelone)
        self.amount.setObjectName(u"amount")
        self.amount.setMinimumSize(QSize(0, 30))
        self.amount.setMaximumSize(QSize(800, 16777215))

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.amount)

        self.lable = QLabel(self.pagelone)
        self.lable.setObjectName(u"lable")
        self.lable.setFont(font4)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lable)

        self.intrest_rate = QDoubleSpinBox(self.pagelone)
        self.intrest_rate.setObjectName(u"intrest_rate")
        self.intrest_rate.setMaximumSize(QSize(60, 16777215))

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.intrest_rate)

        self.lable_2 = QLabel(self.pagelone)
        self.lable_2.setObjectName(u"lable_2")
        self.lable_2.setFont(font4)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.lable_2)

        self.checkno = QLineEdit(self.pagelone)
        self.checkno.setObjectName(u"checkno")
        self.checkno.setMinimumSize(QSize(0, 30))
        self.checkno.setMaximumSize(QSize(800, 16777215))

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.checkno)

        self.date_of_lone = QLabel(self.pagelone)
        self.date_of_lone.setObjectName(u"date_of_lone")
        self.date_of_lone.setFont(font4)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.date_of_lone)

        self.date_of_lone_2 = QLabel(self.pagelone)
        self.date_of_lone_2.setObjectName(u"date_of_lone_2")
        self.date_of_lone_2.setFont(font4)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.date_of_lone_2)

        self.jam1_2 = QLineEdit(self.pagelone)
        self.jam1_2.setObjectName(u"jam1_2")
        self.jam1_2.setMinimumSize(QSize(0, 30))
        self.jam1_2.setMaximumSize(QSize(800, 16777215))

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.jam1_2)

        self.date_of_lone_3 = QLabel(self.pagelone)
        self.date_of_lone_3.setObjectName(u"date_of_lone_3")
        self.date_of_lone_3.setFont(font4)

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.date_of_lone_3)

        self.jam1_3 = QLineEdit(self.pagelone)
        self.jam1_3.setObjectName(u"jam1_3")
        self.jam1_3.setMinimumSize(QSize(0, 30))
        self.jam1_3.setMaximumSize(QSize(800, 16777215))

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.jam1_3)

        self.remark = QLabel(self.pagelone)
        self.remark.setObjectName(u"remark")
        self.remark.setFont(font4)

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.remark)

        self.remark_2 = QComboBox(self.pagelone)
        self.remark_2.addItem("")
        self.remark_2.addItem("")
        self.remark_2.addItem("")
        self.remark_2.setObjectName(u"remark_2")
        self.remark_2.setMinimumSize(QSize(300, 30))
        self.remark_2.setMaximumSize(QSize(500, 16777215))

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.remark_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.formLayout_2.setItem(13, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.approve_btn = QPushButton(self.pagelone)
        self.approve_btn.setObjectName(u"approve_btn")
        self.approve_btn.setMinimumSize(QSize(130, 0))
        self.approve_btn.setMaximumSize(QSize(160, 16777215))
        self.approve_btn.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.approve_btn)

        self.error_3 = QLabel(self.pagelone)
        self.error_3.setObjectName(u"error_3")

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.error_3)

        self.date1_1 = QDateEdit(self.pagelone)
        self.date1_1.setObjectName(u"date1_1")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.date1_1)


        self.gridLayout_11.addLayout(self.formLayout_2, 1, 0, 1, 1)


        self.gridLayout_27.addLayout(self.gridLayout_11, 0, 0, 2, 2)

        self.stackedWidget.addWidget(self.pagelone)
        self.transaction_detail_page = QWidget()
        self.transaction_detail_page.setObjectName(u"transaction_detail_page")
        self.gridLayout_19 = QGridLayout(self.transaction_detail_page)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.transaction_detail_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_6)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tableWidget_2 = QTableWidget(self.frame_6)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        if (self.tableWidget_2.rowCount() < 100):
            self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.tableWidget_2.setFrameShape(QFrame.WinPanel)
        self.tableWidget_2.setFrameShadow(QFrame.Sunken)
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setAutoScrollMargin(17)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setRowCount(100)
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_18.addWidget(self.tableWidget_2, 1, 0, 1, 2)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_18.addWidget(self.label_5, 0, 0, 1, 2)


        self.gridLayout_19.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.transaction_detail_page)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.email, self.mobile2)
        QWidget.setTabOrder(self.mobile2, self.lone_ID)
        QWidget.setTabOrder(self.lone_ID, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.name)
        QWidget.setTabOrder(self.name, self.addherno)
        QWidget.setTabOrder(self.addherno, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.id)
        QWidget.setTabOrder(self.id, self.firstname)
        QWidget.setTabOrder(self.firstname, self.middlename)
        QWidget.setTabOrder(self.middlename, self.addhernumber)
        QWidget.setTabOrder(self.addhernumber, self.mobile1)
        QWidget.setTabOrder(self.mobile1, self.addinfo)
        QWidget.setTabOrder(self.addinfo, self.view_btn)
        QWidget.setTabOrder(self.view_btn, self.amount)
        QWidget.setTabOrder(self.amount, self.intrest_rate)
        QWidget.setTabOrder(self.intrest_rate, self.checkno)
        QWidget.setTabOrder(self.checkno, self.jam1_2)
        QWidget.setTabOrder(self.jam1_2, self.jam1_3)
        QWidget.setTabOrder(self.jam1_3, self.remark_2)
        QWidget.setTabOrder(self.remark_2, self.approve_btn)
        QWidget.setTabOrder(self.approve_btn, self.lastname)
        QWidget.setTabOrder(self.lastname, self.bloodgroup)
        QWidget.setTabOrder(self.bloodgroup, self.nomine)
        QWidget.setTabOrder(self.nomine, self.dob)
        QWidget.setTabOrder(self.dob, self.id_2)
        QWidget.setTabOrder(self.id_2, self.search)
        QWidget.setTabOrder(self.search, self.firstname_2)
        QWidget.setTabOrder(self.firstname_2, self.middlename_2)
        QWidget.setTabOrder(self.middlename_2, self.lastname_2)
        QWidget.setTabOrder(self.lastname_2, self.bloodgroup_2)
        QWidget.setTabOrder(self.bloodgroup_2, self.nomine_2)
        QWidget.setTabOrder(self.nomine_2, self.dob_2)
        QWidget.setTabOrder(self.dob_2, self.doj_2)
        QWidget.setTabOrder(self.doj_2, self.addhernumber_2)
        QWidget.setTabOrder(self.addhernumber_2, self.accountno_2)
        QWidget.setTabOrder(self.accountno_2, self.mobile1_2)
        QWidget.setTabOrder(self.mobile1_2, self.mobile2_2)
        QWidget.setTabOrder(self.mobile2_2, self.email_2)
        QWidget.setTabOrder(self.email_2, self.balance_2)
        QWidget.setTabOrder(self.balance_2, self.addinfo_2)
        QWidget.setTabOrder(self.addinfo_2, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.transaction_detail_btn)
        QWidget.setTabOrder(self.transaction_detail_btn, self.loneview_btn)
        QWidget.setTabOrder(self.loneview_btn, self.viewall_btn)
        QWidget.setTabOrder(self.viewall_btn, self.new_member_btn)
        QWidget.setTabOrder(self.new_member_btn, self.update_member_btn)
        QWidget.setTabOrder(self.update_member_btn, self.remove_member_btn)
        QWidget.setTabOrder(self.remove_member_btn, self.collect_lone_btn)
        QWidget.setTabOrder(self.collect_lone_btn, self.give_lone)
        QWidget.setTabOrder(self.give_lone, self.collection)
        QWidget.setTabOrder(self.collection, self.doj)
        QWidget.setTabOrder(self.doj, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.dashboard_btn)
        QWidget.setTabOrder(self.dashboard_btn, self.Manage_btn)
        QWidget.setTabOrder(self.Manage_btn, self.balance)
        QWidget.setTabOrder(self.balance, self.accountno)

        self.retranslateUi(MainWindow)

        self.dashboard_btn.setDefault(False)
        self.Manage_btn.setDefault(False)
        self.view_btn.setDefault(False)
        self.pushButton_8.setDefault(False)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.dashboard_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"Button", None))
#endif // QT_CONFIG(whatsthis)
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u"Dashbard ", None))
#if QT_CONFIG(whatsthis)
        self.Manage_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"Button", None))
#endif // QT_CONFIG(whatsthis)
        self.Manage_btn.setText(QCoreApplication.translate("MainWindow", u"Manage ", None))
#if QT_CONFIG(whatsthis)
        self.view_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"Button", None))
#endif // QT_CONFIG(whatsthis)
        self.view_btn.setText(QCoreApplication.translate("MainWindow", u"View ", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_8.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
#if QT_CONFIG(whatsthis)
        self.label_17.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Name Lastname ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u20b91000", None))
#if QT_CONFIG(whatsthis)
        self.label_41.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Name Lastname ", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u20b91000", None))
#if QT_CONFIG(whatsthis)
        self.label_21.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Name Lastname ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u20b91000", None))
#if QT_CONFIG(whatsthis)
        self.label_19.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Name Lastname ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u20b91000", None))
#if QT_CONFIG(whatsthis)
        self.label_43.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Name Lastname ", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u20b91000", None))
#if QT_CONFIG(whatsthis)
        self.label_45.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Name Lastname ", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u20b91000", None))
#if QT_CONFIG(whatsthis)
        self.label_55.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Name Lastname ", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u20b91000", None))
        self.total_lone.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Total Member</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Total Loan</p></body></html>", None))
        self.total_member.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total Saving", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Total Loan</p></body></html>", None))
        self.total_lone_3.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.total_lone_4.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#4e8d2c;\">Member Information Table </span></p></body></html>", None))
        self.remove_member_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.update_member_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.collect_lone_btn.setText(QCoreApplication.translate("MainWindow", u"Collect Lone", None))
        self.give_lone.setText(QCoreApplication.translate("MainWindow", u"Give Lone", None))
        self.collection.setText(QCoreApplication.translate("MainWindow", u"Add Saving", None))
#if QT_CONFIG(whatsthis)
        self.new_member_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.new_member_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Basic information", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"last Name", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Blood group", None))
        self.bloodgroup_2.setItemText(0, QCoreApplication.translate("MainWindow", u"A+", None))
        self.bloodgroup_2.setItemText(1, QCoreApplication.translate("MainWindow", u"A-", None))
        self.bloodgroup_2.setItemText(2, QCoreApplication.translate("MainWindow", u"B+", None))
        self.bloodgroup_2.setItemText(3, QCoreApplication.translate("MainWindow", u"B-", None))
        self.bloodgroup_2.setItemText(4, QCoreApplication.translate("MainWindow", u"AB+", None))
        self.bloodgroup_2.setItemText(5, QCoreApplication.translate("MainWindow", u"AB-", None))
        self.bloodgroup_2.setItemText(6, QCoreApplication.translate("MainWindow", u"O+", None))
        self.bloodgroup_2.setItemText(7, QCoreApplication.translate("MainWindow", u"O-", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Nomine", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Data of Birth", None))
        self.dob_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Data Of Joing", None))
        self.doj_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Addher Number", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Account No:", None))
        self.search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Contact  Information", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Mobile No 1", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Mobile No 2", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Opning balance", None))
        self.addinfo_2.setText(QCoreApplication.translate("MainWindow", u"Update Information", None))
        self.error_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Updata Information</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.loneview_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.loneview_btn.setText(QCoreApplication.translate("MainWindow", u"Lone", None))
#if QT_CONFIG(whatsthis)
        self.transaction_detail_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.transaction_detail_btn.setText(QCoreApplication.translate("MainWindow", u"transaction_detail", None))
#if QT_CONFIG(whatsthis)
        self.viewall_btn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.viewall_btn.setText(QCoreApplication.translate("MainWindow", u"View All ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Basic information", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Blood group", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Nomine", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Data of Birth", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Data Of Joing", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Addher Number", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Account No:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"last Name", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.dob.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.doj.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.bloodgroup.setItemText(0, QCoreApplication.translate("MainWindow", u"A+", None))
        self.bloodgroup.setItemText(1, QCoreApplication.translate("MainWindow", u"A-", None))
        self.bloodgroup.setItemText(2, QCoreApplication.translate("MainWindow", u"B+", None))
        self.bloodgroup.setItemText(3, QCoreApplication.translate("MainWindow", u"B-", None))
        self.bloodgroup.setItemText(4, QCoreApplication.translate("MainWindow", u"AB+", None))
        self.bloodgroup.setItemText(5, QCoreApplication.translate("MainWindow", u"AB-", None))
        self.bloodgroup.setItemText(6, QCoreApplication.translate("MainWindow", u"O+", None))
        self.bloodgroup.setItemText(7, QCoreApplication.translate("MainWindow", u"O-", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Contact  Information", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Mobile No 1", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Mobile No 2", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Opning balance", None))
        self.error.setText("")
        self.addinfo.setText(QCoreApplication.translate("MainWindow", u"Add information", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lone No", None))
        self.lone_no.setText(QCoreApplication.translate("MainWindow", u"lone_NO:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Addher Number", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.lable.setText(QCoreApplication.translate("MainWindow", u"Intrest Rate", None))
        self.lable_2.setText(QCoreApplication.translate("MainWindow", u"Check Number", None))
        self.date_of_lone.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.date_of_lone_2.setText(QCoreApplication.translate("MainWindow", u"Jamindar 1", None))
        self.date_of_lone_3.setText(QCoreApplication.translate("MainWindow", u"Jamindar 2", None))
        self.remark.setText(QCoreApplication.translate("MainWindow", u"Remark", None))
        self.remark_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Remark 1", None))
        self.remark_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Remark 2", None))
        self.remark_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Remark 3", None))

        self.approve_btn.setText(QCoreApplication.translate("MainWindow", u"Approve", None))
        self.error_3.setText(QCoreApplication.translate("MainWindow", u"info", None))
        self.date1_1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/M/d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#4e8d2c;\">Transaction Details</span></p></body></html>", None))
    # retranslateUi

