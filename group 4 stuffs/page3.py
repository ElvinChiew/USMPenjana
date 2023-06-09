# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_page3(object):
    def setupUi(self, page3):
        page3.setObjectName("page3")
        page3.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(page3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 500, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.displaygraph = QtWidgets.QWidget(self.centralwidget)
        self.displaygraph.setGeometry(QtCore.QRect(40, 160, 721, 501))
        self.displaygraph.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.displaygraph.setObjectName("displaygraph")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 681))
        self.widget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.995763, y2:0.96, stop:0 rgba(53, 233, 242, 255), stop:1 rgba(255, 0, 127, 255));")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label.raise_()
        self.displaygraph.raise_()
        page3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(page3)
        self.statusbar.setObjectName("statusbar")
        page3.setStatusBar(self.statusbar)

        self.retranslateUi(page3)
        QtCore.QMetaObject.connectSlotsByName(page3)

    def retranslateUi(self, page3):
        _translate = QtCore.QCoreApplication.translate
        page3.setWindowTitle(_translate("page3", "Page 3"))
        self.label.setText(_translate("page3", "GRAPH ANALYSIS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page3 = QtWidgets.QMainWindow()
    ui = Ui_page3()
    ui.setupUi(page3)
    page3.show()
    sys.exit(app.exec_())

