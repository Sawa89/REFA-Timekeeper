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
        Dialog.resize(400, 217)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 71))
        self.label.setObjectName("label")
        self.btn_ja = QtWidgets.QPushButton(Dialog)
        self.btn_ja.setGeometry(QtCore.QRect(300, 110, 91, 31))
        self.btn_ja.setObjectName("btn_ja")
        self.btn_nein = QtWidgets.QPushButton(Dialog)
        self.btn_nein.setGeometry(QtCore.QRect(300, 170, 91, 31))
        self.btn_nein.setObjectName("btn_nein")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 161, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 101, 31))
        self.label_3.setObjectName("label_3")
        self.lcd_Abschnitte = QtWidgets.QLCDNumber(Dialog)
        self.lcd_Abschnitte.setGeometry(QtCore.QRect(40, 140, 71, 51))
        self.lcd_Abschnitte.setDigitCount(2)
        self.lcd_Abschnitte.setObjectName("lcd_Abschnitte")
        self.lcd_Zyklen = QtWidgets.QLCDNumber(Dialog)
        self.lcd_Zyklen.setGeometry(QtCore.QRect(180, 140, 71, 51))
        self.lcd_Zyklen.setDigitCount(2)
        self.lcd_Zyklen.setObjectName("lcd_Zyklen")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        self.btn_ja.clicked.connect(Dialog.accept)
        self.btn_nein.clicked.connect(Dialog.reject)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Studie schon vorhanden"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Wollen sie die aktuelle Konfiguration </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">der bestehenden Zeitstudie beibehalten?</span></p></body></html>"))
        self.btn_ja.setText(_translate("Dialog", "Ja"))
        self.btn_nein.setText(_translate("Dialog", "Nein"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Ablaufabschnitte</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Zyklen</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
