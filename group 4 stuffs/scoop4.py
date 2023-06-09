# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoop4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 333)
        self.projecttitle = QtWidgets.QLabel(Dialog)
        self.projecttitle.setGeometry(QtCore.QRect(260, 0, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.projecttitle.setFont(font)
        self.projecttitle.setObjectName("projecttitle")
        self.durian = QtWidgets.QRadioButton(Dialog)
        self.durian.setGeometry(QtCore.QRect(111, 153, 16, 16))
        self.durian.setText("")
        self.durian.setObjectName("durian")
        self.choc = QtWidgets.QRadioButton(Dialog)
        self.choc.setGeometry(QtCore.QRect(111, 84, 16, 16))
        self.choc.setText("")
        self.choc.setObjectName("choc")
        self.Straw = QtWidgets.QRadioButton(Dialog)
        self.Straw.setGeometry(QtCore.QRect(111, 107, 16, 16))
        self.Straw.setText("")
        self.Straw.setObjectName("Straw")
        self.boba = QtWidgets.QCheckBox(Dialog)
        self.boba.setGeometry(QtCore.QRect(421, 61, 16, 16))
        self.boba.setText("")
        self.boba.setObjectName("boba")
        self.vannill_lbl = QtWidgets.QLabel(Dialog)
        self.vannill_lbl.setGeometry(QtCore.QRect(11, 58, 38, 16))
        self.vannill_lbl.setObjectName("vannill_lbl")
        self.choc_lbl = QtWidgets.QLabel(Dialog)
        self.choc_lbl.setGeometry(QtCore.QRect(11, 81, 56, 16))
        self.choc_lbl.setObjectName("choc_lbl")
        self.strawlbl = QtWidgets.QLabel(Dialog)
        self.strawlbl.setGeometry(QtCore.QRect(11, 104, 64, 16))
        self.strawlbl.setObjectName("strawlbl")
        self.flava_lbl = QtWidgets.QLabel(Dialog)
        self.flava_lbl.setGeometry(QtCore.QRect(11, 35, 42, 16))
        self.flava_lbl.setObjectName("flava_lbl")
        self.sprinkle_lbl = QtWidgets.QLabel(Dialog)
        self.sprinkle_lbl.setGeometry(QtCore.QRect(306, 104, 44, 16))
        self.sprinkle_lbl.setObjectName("sprinkle_lbl")
        self.chiplbl = QtWidgets.QLabel(Dialog)
        self.chiplbl.setGeometry(QtCore.QRect(306, 81, 87, 16))
        self.chiplbl.setObjectName("chiplbl")
        self.boba_lbl = QtWidgets.QLabel(Dialog)
        self.boba_lbl.setGeometry(QtCore.QRect(306, 58, 28, 16))
        self.boba_lbl.setObjectName("boba_lbl")
        self.topping_lbl = QtWidgets.QLabel(Dialog)
        self.topping_lbl.setGeometry(QtCore.QRect(306, 35, 46, 16))
        self.topping_lbl.setObjectName("topping_lbl")
        self.cchip = QtWidgets.QCheckBox(Dialog)
        self.cchip.setGeometry(QtCore.QRect(421, 84, 16, 16))
        self.cchip.setText("")
        self.cchip.setObjectName("cchip")
        self.sprink = QtWidgets.QCheckBox(Dialog)
        self.sprink.setGeometry(QtCore.QRect(421, 107, 16, 16))
        self.sprink.setText("")
        self.sprink.setObjectName("sprink")
        self.total_lbl = QtWidgets.QLabel(Dialog)
        self.total_lbl.setGeometry(QtCore.QRect(10, 210, 61, 16))
        self.total_lbl.setObjectName("total_lbl")
        self.calculateButton = QtWidgets.QPushButton(Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(10, 260, 93, 28))
        self.calculateButton.setObjectName("calculateButton")
        self.resetButton = QtWidgets.QPushButton(Dialog)
        self.resetButton.setGeometry(QtCore.QRect(190, 260, 93, 28))
        self.resetButton.setObjectName("resetButton")
        self.Price_Lbl = QtWidgets.QLabel(Dialog)
        self.Price_Lbl.setGeometry(QtCore.QRect(201, 41, 28, 16))
        self.Price_Lbl.setObjectName("Price_Lbl")
        self.Price_Lbl2 = QtWidgets.QLabel(Dialog)
        self.Price_Lbl2.setGeometry(QtCore.QRect(526, 48, 28, 16))
        self.Price_Lbl2.setObjectName("Price_Lbl2")
        self.hargaVanilla = QtWidgets.QLabel(Dialog)
        self.hargaVanilla.setGeometry(QtCore.QRect(201, 64, 25, 16))
        self.hargaVanilla.setObjectName("hargaVanilla")
        self.hargaStrawberry = QtWidgets.QLabel(Dialog)
        self.hargaStrawberry.setGeometry(QtCore.QRect(201, 110, 25, 16))
        self.hargaStrawberry.setObjectName("hargaStrawberry")
        self.hargaChocolate = QtWidgets.QLabel(Dialog)
        self.hargaChocolate.setGeometry(QtCore.QRect(201, 87, 25, 16))
        self.hargaChocolate.setObjectName("hargaChocolate")
        self.hargasprinkle = QtWidgets.QLabel(Dialog)
        self.hargasprinkle.setGeometry(QtCore.QRect(526, 117, 18, 16))
        self.hargasprinkle.setObjectName("hargasprinkle")
        self.hargaBoba = QtWidgets.QLabel(Dialog)
        self.hargaBoba.setGeometry(QtCore.QRect(526, 71, 18, 16))
        self.hargaBoba.setObjectName("hargaBoba")
        self.hargaChocChip = QtWidgets.QLabel(Dialog)
        self.hargaChocChip.setGeometry(QtCore.QRect(526, 94, 18, 16))
        self.hargaChocChip.setObjectName("hargaChocChip")
        self.total_textBox = QtWidgets.QTextEdit(Dialog)
        self.total_textBox.setGeometry(QtCore.QRect(110, 200, 104, 31))
        self.total_textBox.setObjectName("total_textBox")
        self.durian_lbl = QtWidgets.QLabel(Dialog)
        self.durian_lbl.setGeometry(QtCore.QRect(11, 150, 37, 16))
        self.durian_lbl.setObjectName("durian_lbl")
        self.cornlbl = QtWidgets.QLabel(Dialog)
        self.cornlbl.setGeometry(QtCore.QRect(11, 127, 27, 16))
        self.cornlbl.setObjectName("cornlbl")
        self.vanila = QtWidgets.QRadioButton(Dialog)
        self.vanila.setGeometry(QtCore.QRect(111, 61, 16, 16))
        self.vanila.setText("")
        self.vanila.setObjectName("vanila")
        self.corn = QtWidgets.QRadioButton(Dialog)
        self.corn.setGeometry(QtCore.QRect(111, 130, 16, 16))
        self.corn.setText("")
        self.corn.setObjectName("corn")
        self.hargaDurian = QtWidgets.QLabel(Dialog)
        self.hargaDurian.setGeometry(QtCore.QRect(201, 156, 25, 16))
        self.hargaDurian.setObjectName("hargaDurian")
        self.hargaCorn = QtWidgets.QLabel(Dialog)
        self.hargaCorn.setGeometry(QtCore.QRect(201, 133, 25, 16))
        self.hargaCorn.setObjectName("hargaCorn")

        self.retranslateUi(Dialog)
        self.resetButton.clicked.connect(self.total_textBox.clear)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.projecttitle.setText(_translate("Dialog", "SCOOP"))
        self.vannill_lbl.setText(_translate("Dialog", "Vanilla"))
        self.choc_lbl.setText(_translate("Dialog", "Chocolate"))
        self.strawlbl.setText(_translate("Dialog", "Strawberry"))
        self.flava_lbl.setText(_translate("Dialog", "Flavour"))
        self.sprinkle_lbl.setText(_translate("Dialog", "sprinkle"))
        self.chiplbl.setText(_translate("Dialog", "chcocolate chip"))
        self.boba_lbl.setText(_translate("Dialog", "Boba"))
        self.topping_lbl.setText(_translate("Dialog", "Topping"))
        self.total_lbl.setText(_translate("Dialog", "Total"))
        self.calculateButton.setText(_translate("Dialog", "Calculate"))
        self.resetButton.setText(_translate("Dialog", "Reset"))
        self.Price_Lbl.setText(_translate("Dialog", "price"))
        self.Price_Lbl2.setText(_translate("Dialog", "price"))
        self.hargaVanilla.setText(_translate("Dialog", "2.02"))
        self.hargaStrawberry.setText(_translate("Dialog", "1.66"))
        self.hargaChocolate.setText(_translate("Dialog", "1.40"))
        self.hargasprinkle.setText(_translate("Dialog", "0.5"))
        self.hargaBoba.setText(_translate("Dialog", "0.8"))
        self.hargaChocChip.setText(_translate("Dialog", "0.3"))
        self.durian_lbl.setText(_translate("Dialog", "Durian"))
        self.cornlbl.setText(_translate("Dialog", "Corn"))
        self.hargaDurian.setText(_translate("Dialog", "5.00"))
        self.hargaCorn.setText(_translate("Dialog", "3.00"))

    def calculating(self):
        total=0 
        if self.vanila.isChecked() ==True:
            total=total+ 2.02
        if self.choc.isChecked() ==True:
            total=total + 1.40 
        if self.Straw.isChecked() ==True:
            total=total + 1.66
        if self.corn.isChecked()==True:
            total=total + 3
        if self.durian.isChecked()==True:
            total=total + 5
        if self.boba.isChecked()==True:
            total=total + 1
            self.total_textBox.setText(total)
        self.total_textBox.setText("RM " + str(total)  )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

