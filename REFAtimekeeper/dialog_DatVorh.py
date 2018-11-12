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

class Ui_Daten_vorhanden(object):
    def setupUi(self, Daten_vorhanden):
        Daten_vorhanden.setObjectName("Daten_vorhanden")
        Daten_vorhanden.resize(400, 196)
        self.btn_ja = QtWidgets.QPushButton(Daten_vorhanden)
        self.btn_ja.setGeometry(QtCore.QRect(30, 150, 91, 31))
        self.btn_ja.setStyleSheet("")
        self.btn_ja.setObjectName("btn_ja")
        self.btn_nein = QtWidgets.QPushButton(Daten_vorhanden)
        self.btn_nein.setGeometry(QtCore.QRect(280, 150, 91, 31))
        self.btn_nein.setStyleSheet("")
        self.btn_nein.setObjectName("btn_nein")
        self.label = QtWidgets.QLabel(Daten_vorhanden)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 81))
        self.label.setObjectName("label")
        self.retranslateUi(Daten_vorhanden)
        QtCore.QMetaObject.connectSlotsByName(Daten_vorhanden)


        self.btn_ja.clicked.connect(Daten_vorhanden.accept)
        self.btn_nein.clicked.connect(Daten_vorhanden.reject)
        



    def retranslateUi(self, Daten_vorhanden):
        _translate = QtCore.QCoreApplication.translate
        Daten_vorhanden.setWindowTitle(_translate("Daten_vorhanden", "Daten vorhanden"))
        self.btn_ja.setText(_translate("Daten_vorhanden", "Ja"))
        self.btn_nein.setText(_translate("Daten_vorhanden", "Nein"))
        self.label.setText(_translate("Daten_vorhanden", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Diese Studie enthält bereits Daten!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Wollen sie die Daten verwerfen?</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Daten_vorhanden = QtWidgets.QDialog()
    ui = Ui_Daten_vorhanden()
    ui.setupUi(Daten_vorhanden)
    Daten_vorhanden.show()
    sys.exit(app.exec_())
