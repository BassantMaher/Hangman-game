# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hangman.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import ff_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1043, 756)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-image: url(:/newPrefix/R (1).jpeg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(990, 550))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"border-image:none;\n"
"background-color:none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border:0px;")
        self.label_2.setPixmap(QPixmap(u":/newPrefix/1.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 16pt \"Ravie\";")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.guess = QLabel(self.frame_16)
        self.guess.setObjectName(u"guess")
        self.guess.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"")

        self.verticalLayout_11.addWidget(self.guess, 0, Qt.AlignHCenter)

        self.guessLbl = QLabel(self.frame_16)
        self.guessLbl.setObjectName(u"guessLbl")
        self.guessLbl.setStyleSheet(u"color: rgb(170, 0, 0) ;")

        self.verticalLayout_11.addWidget(self.guessLbl, 0, Qt.AlignHCenter)

        self.HintLbl = QPushButton(self.frame_16)
        self.HintLbl.setObjectName(u"HintLbl")
        self.HintLbl.setMinimumSize(QSize(400, 55))
        self.HintLbl.setMaximumSize(QSize(400, 16777215))
        self.HintLbl.setStyleSheet(u"QPushButton:hover{background-color:rgb(170, 0, 0);\n"
"\n"
"color:rgb(255, 255, 0);}\n"
"QPushButton{\n"
"background-color:rgb(255, 255, 0);\n"
"border-radius: 8px;\n"
"color:rgb(170, 0, 0);}")

        self.verticalLayout_11.addWidget(self.HintLbl)


        self.horizontalLayout_5.addWidget(self.frame_16)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"font: 12pt \"Ravie\";\n"
"background-color:rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"color:rgb(255, 255, 0);\n"
"border-image:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(170, 0, 0);\n"
"background-color:rgb(255, 255, 0);\n"
"}\n"
"QFrame{\n"
"border-radius:12px;\n"
"font: 12pt \"Ravie\";\n"
"border-image:none;\n"
"background-color:none;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border:0px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Abtn = QPushButton(self.frame_6)
        self.Abtn.setObjectName(u"Abtn")
        self.Abtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.Abtn)

        self.Ibtn = QPushButton(self.frame_6)
        self.Ibtn.setObjectName(u"Ibtn")
        self.Ibtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.Ibtn)

        self.Qbtn = QPushButton(self.frame_6)
        self.Qbtn.setObjectName(u"Qbtn")
        self.Qbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_2.addWidget(self.Qbtn)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:0px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Bbtn = QPushButton(self.frame_12)
        self.Bbtn.setObjectName(u"Bbtn")
        self.Bbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.Bbtn)

        self.Jbtn = QPushButton(self.frame_12)
        self.Jbtn.setObjectName(u"Jbtn")
        self.Jbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.Jbtn)

        self.Rbtn = QPushButton(self.frame_12)
        self.Rbtn.setObjectName(u"Rbtn")
        self.Rbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_3.addWidget(self.Rbtn)


        self.horizontalLayout_2.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border:0px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_13)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Cbtn = QPushButton(self.frame_13)
        self.Cbtn.setObjectName(u"Cbtn")
        self.Cbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.Cbtn)

        self.Kbtn = QPushButton(self.frame_13)
        self.Kbtn.setObjectName(u"Kbtn")
        self.Kbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.Kbtn)

        self.Sbtn = QPushButton(self.frame_13)
        self.Sbtn.setObjectName(u"Sbtn")
        self.Sbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_4.addWidget(self.Sbtn)


        self.horizontalLayout_2.addWidget(self.frame_13)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border:0px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Dbtn = QPushButton(self.frame_7)
        self.Dbtn.setObjectName(u"Dbtn")
        self.Dbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.Dbtn)

        self.Lbtn = QPushButton(self.frame_7)
        self.Lbtn.setObjectName(u"Lbtn")
        self.Lbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.Lbtn)

        self.Tbtn = QPushButton(self.frame_7)
        self.Tbtn.setObjectName(u"Tbtn")
        self.Tbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_5.addWidget(self.Tbtn)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border:0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Ebtn = QPushButton(self.frame_8)
        self.Ebtn.setObjectName(u"Ebtn")
        self.Ebtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_6.addWidget(self.Ebtn)

        self.Mbtn = QPushButton(self.frame_8)
        self.Mbtn.setObjectName(u"Mbtn")
        self.Mbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_6.addWidget(self.Mbtn)

        self.Ubtn = QPushButton(self.frame_8)
        self.Ubtn.setObjectName(u"Ubtn")
        self.Ubtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_6.addWidget(self.Ubtn)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border:0px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Fbtn = QPushButton(self.frame_9)
        self.Fbtn.setObjectName(u"Fbtn")
        self.Fbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_7.addWidget(self.Fbtn)

        self.Nbtn = QPushButton(self.frame_9)
        self.Nbtn.setObjectName(u"Nbtn")
        self.Nbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_7.addWidget(self.Nbtn)

        self.Vbtn = QPushButton(self.frame_9)
        self.Vbtn.setObjectName(u"Vbtn")
        self.Vbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_7.addWidget(self.Vbtn)


        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:0px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Gbtn = QPushButton(self.frame_10)
        self.Gbtn.setObjectName(u"Gbtn")
        self.Gbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_8.addWidget(self.Gbtn)

        self.Obtn = QPushButton(self.frame_10)
        self.Obtn.setObjectName(u"Obtn")
        self.Obtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_8.addWidget(self.Obtn)

        self.Wbtn = QPushButton(self.frame_10)
        self.Wbtn.setObjectName(u"Wbtn")
        self.Wbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_8.addWidget(self.Wbtn)


        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border:0px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.Hbtn = QPushButton(self.frame_11)
        self.Hbtn.setObjectName(u"Hbtn")
        self.Hbtn.setMinimumSize(QSize(0, 35))
        self.Hbtn.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.Hbtn)

        self.Pbtn = QPushButton(self.frame_11)
        self.Pbtn.setObjectName(u"Pbtn")
        self.Pbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_9.addWidget(self.Pbtn)

        self.Xbtn = QPushButton(self.frame_11)
        self.Xbtn.setObjectName(u"Xbtn")
        self.Xbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_9.addWidget(self.Xbtn)


        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border:0px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Ybtn = QPushButton(self.frame_14)
        self.Ybtn.setObjectName(u"Ybtn")
        self.Ybtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_10.addWidget(self.Ybtn)

        self.Zbtn = QPushButton(self.frame_14)
        self.Zbtn.setObjectName(u"Zbtn")
        self.Zbtn.setMinimumSize(QSize(0, 35))

        self.verticalLayout_10.addWidget(self.Zbtn)


        self.horizontalLayout_2.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.guess.setText("")
        self.guessLbl.setText("")
        self.HintLbl.setText(QCoreApplication.translate("MainWindow", u"change word", None))
        self.Abtn.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.Ibtn.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.Qbtn.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.Bbtn.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.Jbtn.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.Rbtn.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.Cbtn.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Kbtn.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.Sbtn.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.Dbtn.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.Lbtn.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.Tbtn.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.Ebtn.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.Mbtn.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.Ubtn.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.Fbtn.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.Nbtn.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.Vbtn.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.Gbtn.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.Obtn.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.Wbtn.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.Hbtn.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.Pbtn.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.Xbtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.Ybtn.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.Zbtn.setText(QCoreApplication.translate("MainWindow", u"Z", None))
    # retranslateUi

