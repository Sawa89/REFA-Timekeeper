from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ende(object):
    def setupUi(self, Ende):
        Ende.setObjectName("Ende")
        Ende.resize(400, 218)
        self.buttonBox = QtWidgets.QDialogButtonBox(Ende)
        self.buttonBox.setGeometry(QtCore.QRect(30, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Ende)
        self.label.setGeometry(QtCore.QRect(30, 30, 341, 91))
        self.label.setObjectName("label")
        self.retranslateUi(Ende)
        self.buttonBox.accepted.connect(Ende.accept)
        self.buttonBox.rejected.connect(Ende.reject)
        QtCore.QMetaObject.connectSlotsByName(Ende)

    def retranslateUi(self, Ende):
        _translate = QtCore.QCoreApplication.translate
        Ende.setWindowTitle(_translate("Ende", "Abgeschlossen"))
        self.label.setText(_translate("Ende", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Zeitmessung abgeschlossen!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Die Zeiten wurden erfolgreich in der </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Datenbank gespeichert!</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ende = QtWidgets.QDialog()
    ui = Ui_Ende()
    ui.setupUi(Ende)
    Ende.show()
    sys.exit(app.exec_())
