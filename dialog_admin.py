from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 149)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 241, 51))
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 251, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_ja = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_ja.setObjectName("btn_ja")
        self.horizontalLayout.addWidget(self.btn_ja)
        self.btn_nein = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_nein.setObjectName("btn_nein")
        self.horizontalLayout.addWidget(self.btn_nein)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.btn_ja.clicked.connect(Dialog.accept)
        self.btn_nein.clicked.connect(Dialog.reject)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Adminrechte"))
        self.label.setText(_translate("Dialog", "Sind sie Administrator?"))
        self.btn_ja.setText(_translate("Dialog", "Ja"))
        self.btn_nein.setText(_translate("Dialog", "Nein"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
