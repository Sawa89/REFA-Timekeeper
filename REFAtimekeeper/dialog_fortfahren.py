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

class Ui_Fortfahren(object):
    def setupUi(self, Fortfahren):
        Fortfahren.setObjectName("Fortfahren")
        Fortfahren.resize(400, 207)
        self.label = QtWidgets.QLabel(Fortfahren)
        self.label.setGeometry(QtCore.QRect(0, 20, 401, 81))
        self.label.setObjectName("label")
        self.btn_nein = QtWidgets.QPushButton(Fortfahren)
        self.btn_nein.setGeometry(QtCore.QRect(40, 120, 91, 61))
        self.btn_nein.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"font: 75 12pt \"Arial\";")
        self.btn_nein.setObjectName("btn_ja")
        self.btn_ja = QtWidgets.QPushButton(Fortfahren)
        self.btn_ja.setGeometry(QtCore.QRect(280, 140, 91, 41))
        self.btn_ja.setStyleSheet("background-color: rgb(255, 83, 49);")
        self.btn_ja.setObjectName("btn_nein")
        self.retranslateUi(Fortfahren)
        QtCore.QMetaObject.connectSlotsByName(Fortfahren)


        self.btn_nein.clicked.connect(Fortfahren.reject)
        self.btn_ja.clicked.connect(Fortfahren.accept)


    def retranslateUi(self, Fortfahren):
        _translate = QtCore.QCoreApplication.translate
        Fortfahren.setWindowTitle(_translate("Fortfahren", "Dialog"))
        self.label.setText(_translate("Fortfahren", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Es wurden nicht alle Zeiten aufgenommen!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Trotzdem beenden?</span></p></body></html>"))
        self.btn_nein.setText(_translate("Fortfahren", "Nein"))
        self.btn_ja.setText(_translate("Fortfahren", "Ja"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fortfahren = QtWidgets.QDialog()
    ui = Ui_Fortfahren()
    ui.setupUi(Fortfahren)
    Fortfahren.show()
    sys.exit(app.exec_())
