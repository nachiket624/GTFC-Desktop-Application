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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(252, 211, 161, 255), stop:1 rgba(235, 189, 255, 255))")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setKerning(True)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 0, 0)\n"
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

        self.gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy3)
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 0, 0)\n"
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

        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy3.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy3)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 0, 0)\n"
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

        self.gridLayout.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy3.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy3)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(13, 9, 36,0);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 0, 0)\n"
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

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableView = QTableView(self.frame_2)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"Button", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Dashbard", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_8.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_6.setWhatsThis(QCoreApplication.translate("MainWindow", u"Button", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Manage", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"Button", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

