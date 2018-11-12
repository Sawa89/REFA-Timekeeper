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
        Dialog.resize(261, 178)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 140, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 251, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtn_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtn_5.setStyleSheet("font: 75 12pt \"Arial\";")
        self.rbtn_5.setChecked(True)
        self.rbtn_5.setObjectName("rbtn_5")
        self.horizontalLayout.addWidget(self.rbtn_5)
        self.rbtn_10 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtn_10.setStyleSheet("font: 75 12pt \"Arial\";")
        self.rbtn_10.setObjectName("rbtn_10")
        self.horizontalLayout.addWidget(self.rbtn_10)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.label.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Grenzwert auswählen"))
        self.rbtn_5.setText(_translate("Dialog", "5 %"))
        self.rbtn_10.setText(_translate("Dialog", "10 %"))
        self.label.setText(_translate("Dialog", "Vertrauensbereich (ε)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

