# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from page2 import  Ui_page2
class Ui_page1(object):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_page2()
        self.ui.setupUi(self.window)
        page1.hide()
        self.window.show()
        
    def setupUi(self, page1):
        page1.setObjectName("page1")
        page1.resize(801, 681)
        page1.setStyleSheet("QWidget#page1_centralwidget{\n"
"background-image:url(:/background/WhatsApp Image 2021-11-12 at 12.14.33 PM.jpeg);}")
        self.page1_centralwidget = QtWidgets.QWidget(page1)
        self.page1_centralwidget.setObjectName("page1_centralwidget")
        self.welcome = QtWidgets.QLabel(self.page1_centralwidget)
        self.welcome.setGeometry(QtCore.QRect(140, 70, 521, 151))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.welcome.setFont(font)
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.label = QtWidgets.QLabel(self.page1_centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 199, 801, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.page1_centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 250, 801, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.page1_centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 300, 801, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.start_Button = QtWidgets.QPushButton(self.page1_centralwidget)
        self.start_Button.setGeometry(QtCore.QRect(250, 410, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.start_Button.setFont(font)
        self.start_Button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.start_Button.setObjectName("start_Button")
        
        self.start_Button.clicked.connect(self.openWindow)
        
        page1.setCentralWidget(self.page1_centralwidget)
        self.statusbar = QtWidgets.QStatusBar(page1)
        self.statusbar.setObjectName("statusbar")
        page1.setStatusBar(self.statusbar)

        self.retranslateUi(page1)
        QtCore.QMetaObject.connectSlotsByName(page1)

    def retranslateUi(self, page1):
        _translate = QtCore.QCoreApplication.translate
        page1.setWindowTitle(_translate("page1", "Page 1"))
        self.welcome.setText(_translate("page1", "Welcome"))
        self.label.setText(_translate("page1", "This application allows user to view"))
        self.label_3.setText(_translate("page1", "Cardiotocography result and"))
        self.label_2.setText(_translate("page1", "show the fetal health status"))
        self.start_Button.setText(_translate("page1", "Start"))

#import background_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page1 = QtWidgets.QMainWindow()
    ui = Ui_page1()
    ui.setupUi(page1)
    page1.show()
    sys.exit(app.exec_())

