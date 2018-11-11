from PyQt5 import QtCore, QtGui, QtWidgets

import datenbank
import REFA_GUI

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(760, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(650, 220, 80, 132))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 110, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.input_studienname = QtWidgets.QLineEdit(Dialog)
        self.input_studienname.setGeometry(QtCore.QRect(100, 230, 421, 41))
        self.input_studienname.setStyleSheet("font: 75 14pt \"Arial\";")
        self.input_studienname.setText("")
        self.input_studienname.setObjectName("input_studienname")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Name der Zeitstudie"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Geben sie einen Namen für </span></p><p align=\"center\"><span style=\" font-weight:600;\">die neue Zeitstudie ein:</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">(ohne Leerzeichen&Sonderzeichen, Unterstrich ist erlaubt)</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



   
