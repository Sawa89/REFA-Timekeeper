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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(240, 320)
        self.button_1 = QtWidgets.QPushButton(Form)
        self.button_1.setGeometry(QtCore.QRect(10, 199, 61, 61))
        self.button_1.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(Form)
        self.button_2.setGeometry(QtCore.QRect(90, 200, 61, 61))
        self.button_2.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(Form)
        self.button_3.setGeometry(QtCore.QRect(170, 200, 61, 61))
        self.button_3.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_3.setObjectName("button_3")
        self.button_6 = QtWidgets.QPushButton(Form)
        self.button_6.setGeometry(QtCore.QRect(170, 129, 61, 61))
        self.button_6.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_6.setObjectName("button_6")
        self.button_5 = QtWidgets.QPushButton(Form)
        self.button_5.setGeometry(QtCore.QRect(90, 129, 61, 61))
        self.button_5.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_5.setObjectName("button_5")
        self.button_4 = QtWidgets.QPushButton(Form)
        self.button_4.setGeometry(QtCore.QRect(10, 129, 61, 61))
        self.button_4.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_4.setObjectName("button_4")
        self.button_8 = QtWidgets.QPushButton(Form)
        self.button_8.setGeometry(QtCore.QRect(90, 59, 61, 61))
        self.button_8.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_8.setObjectName("button_8")
        self.button_7 = QtWidgets.QPushButton(Form)
        self.button_7.setGeometry(QtCore.QRect(10, 59, 61, 61))
        self.button_7.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_7.setObjectName("button_7")
        self.button_9 = QtWidgets.QPushButton(Form)
        self.button_9.setGeometry(QtCore.QRect(170, 59, 61, 61))
        self.button_9.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_9.setObjectName("button_9")
        self.button_0 = QtWidgets.QPushButton(Form)
        self.button_0.setGeometry(QtCore.QRect(10, 270, 131, 47))
        self.button_0.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.744318 rgba(255, 255, 255, 255));")
        self.button_0.setObjectName("button_0")
        self.button_OK = QtWidgets.QPushButton(Form)
        self.button_OK.setGeometry(QtCore.QRect(150, 270, 81, 47))
        self.button_OK.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(79, 189, 103, 255));")
        self.button_OK.setObjectName("button_OK")
        self.button_bspace = QtWidgets.QPushButton(Form)
        self.button_bspace.setGeometry(QtCore.QRect(90, 5, 141, 51))
        self.button_bspace.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(205, 162, 57, 255));")
        self.button_bspace.setObjectName("button_bspace")
        self.button_x = QtWidgets.QPushButton(Form)
        self.button_x.setGeometry(QtCore.QRect(10, 5, 61, 51))
        self.button_x.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(200, 14, 9, 255));")
        self.button_x.setObjectName("button_x")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button_1.setText(_translate("Form", "1"))
        self.button_2.setText(_translate("Form", "2"))
        self.button_3.setText(_translate("Form", "3"))
        self.button_6.setText(_translate("Form", "6"))
        self.button_5.setText(_translate("Form", "5"))
        self.button_4.setText(_translate("Form", "4"))
        self.button_8.setText(_translate("Form", "8"))
        self.button_7.setText(_translate("Form", "7"))
        self.button_9.setText(_translate("Form", "9"))
        self.button_0.setText(_translate("Form", "0"))
        self.button_OK.setText(_translate("Form", "OK"))
        self.button_bspace.setText(_translate("Form", "Backspace"))
        self.button_x.setText(_translate("Form", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

