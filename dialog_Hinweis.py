from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hinweis(object):
    def setupUi(self, Hinweis):
        Hinweis.setObjectName("Hinweis")
        Hinweis.resize(400, 212)
        self.btn_ok = QtWidgets.QPushButton(Hinweis)
        self.btn_ok.setGeometry(QtCore.QRect(290, 170, 91, 31))
        self.btn_ok.setObjectName("btn_ok")
        self.label = QtWidgets.QLabel(Hinweis)
        self.label.setGeometry(QtCore.QRect(0, 20, 401, 101))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Hinweis)
        self.checkBox.setGeometry(QtCore.QRect(30, 115, 291, 41))
        self.checkBox.setObjectName("checkBox")
        self.retranslateUi(Hinweis)
        QtCore.QMetaObject.connectSlotsByName(Hinweis)


        self.checkBox.setChecked(False)
        self.btn_ok.clicked.connect(Hinweis.accept)




    def retranslateUi(self, Hinweis):
        _translate = QtCore.QCoreApplication.translate
        Hinweis.setWindowTitle(_translate("Hinweis", "Hinweis"))
        self.btn_ok.setText(_translate("Hinweis", "OK"))
        self.label.setText(_translate("Hinweis", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Um die Zeit eines Abschnitts zu stoppen, </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">einfach in die entsprechende Zeile klicken!</span></p></body></html>"))
        self.checkBox.setText(_translate("Hinweis", "Diesen Hinweis nicht mehr anzeigen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hinweis = QtWidgets.QDialog()
    ui = Ui_Hinweis()
    ui.setupUi(Hinweis)
    Hinweis.show()
    sys.exit(app.exec_())
