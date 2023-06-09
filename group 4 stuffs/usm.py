# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from decimal import Decimal

# link clicked signal to action function - 
# add below line to Class init 
#   self.calc_tax_button.clicked.connect(self.calculate_tax)
# add below function to Class
def calculate_tax(self):
    price = Decimal(self.price_box.text())
    tax = Decimal(self.tax_rate.value())
    total_price = price  + ((tax / 100) * price)
    total_price_string = "The total price with tax is: {:.2f}".format(total_price)
    self.results_output.setText(total_price_string)
    
class Ui_GSTTaxCalculator(object):
    def setupUi(self, GSTTaxCalculator):
        GSTTaxCalculator.setObjectName("GSTTaxCalculator")
        GSTTaxCalculator.resize(364, 286)
        self.centralwidget = QtWidgets.QWidget(GSTTaxCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.price = QtWidgets.QLabel(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(11, 63, 65, 36))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.price_box = QtWidgets.QLineEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(133, 63, 137, 22))
        self.price_box.setObjectName("price_box")
        self.tax_rate = QtWidgets.QLabel(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(11, 106, 105, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tax_rate.setFont(font)
        self.tax_rate.setObjectName("tax_rate")
        self.tax_rate_box = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate_box.setEnabled(True)
        self.tax_rate_box.setGeometry(QtCore.QRect(133, 106, 40, 22))
        self.tax_rate_box.setProperty("value", 6)
        self.tax_rate_box.setObjectName("tax_rate_box")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(11, 11, 310, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.results_output = QtWidgets.QLabel(self.centralwidget)
        self.results_output.setGeometry(QtCore.QRect(11, 202, 310, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.results_output.setFont(font)
        self.results_output.setText("")
        self.results_output.setObjectName("results_output")
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(11, 146, 115, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calculate_button.setFont(font)
        self.calculate_button.setObjectName("calculate_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(133, 146, 93, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        GSTTaxCalculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GSTTaxCalculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 26))
        self.menubar.setObjectName("menubar")
        GSTTaxCalculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GSTTaxCalculator)
        self.statusbar.setObjectName("statusbar")
        GSTTaxCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(GSTTaxCalculator)
        self.clear_button.clicked.connect(self.price_box.clear)
        QtCore.QMetaObject.connectSlotsByName(GSTTaxCalculator)

    def retranslateUi(self, GSTTaxCalculator):
        _translate = QtCore.QCoreApplication.translate
        GSTTaxCalculator.setWindowTitle(_translate("GSTTaxCalculator", "MainWindow"))
        self.price.setText(_translate("GSTTaxCalculator", "Price"))
        self.tax_rate.setText(_translate("GSTTaxCalculator", "Tax Rate"))
        self.title.setText(_translate("GSTTaxCalculator", "GST Tax Calculator"))
        self.calculate_button.setText(_translate("GSTTaxCalculator", "Calculate"))
        self.clear_button.setText(_translate("GSTTaxCalculator", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GSTTaxCalculator = QtWidgets.QMainWindow()
    ui = Ui_GSTTaxCalculator()
    ui.setupUi(GSTTaxCalculator)
    GSTTaxCalculator.show()
    sys.exit(app.exec_())