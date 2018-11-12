# Copyright 2017 Philipp Knippschild 
#
# This file is part of REFA-Timerkeeper.
#
# REFA-Timekeeper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# REFA-Timekeeper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

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
