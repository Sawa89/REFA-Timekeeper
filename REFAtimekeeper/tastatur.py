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
        Form.resize(762, 140)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 741, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_I_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_I_2.setObjectName("btn_I_2")
        self.gridLayout.addWidget(self.btn_I_2, 0, 7, 1, 1)
        self.btn_O_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_O_2.setObjectName("btn_O_2")
        self.gridLayout.addWidget(self.btn_O_2, 0, 8, 1, 1)
        self.btn_R_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_R_2.setObjectName("btn_R_2")
        self.gridLayout.addWidget(self.btn_R_2, 0, 3, 1, 1)
        self.btn_P_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_P_2.setObjectName("btn_P_2")
        self.gridLayout.addWidget(self.btn_P_2, 0, 9, 1, 1)
        self.btn_Z_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_Z_2.setObjectName("btn_Z_2")
        self.gridLayout.addWidget(self.btn_Z_2, 0, 5, 1, 1)
        self.btn_U_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_U_2.setObjectName("btn_U_2")
        self.gridLayout.addWidget(self.btn_U_2, 0, 6, 1, 1)
        self.btn_T_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_T_2.setObjectName("btn_T_2")
        self.gridLayout.addWidget(self.btn_T_2, 0, 4, 1, 1)
        self.btn_W_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_W_2.setObjectName("btn_W_2")
        self.gridLayout.addWidget(self.btn_W_2, 0, 1, 1, 1)
        self.btn_E_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_E_2.setObjectName("btn_E_2")
        self.gridLayout.addWidget(self.btn_E_2, 0, 2, 1, 1)
        self.btn_L = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_L.setObjectName("btn_L")
        self.gridLayout.addWidget(self.btn_L, 1, 9, 1, 1)
        self.btn_D = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_D.setObjectName("btn_D")
        self.gridLayout.addWidget(self.btn_D, 1, 3, 1, 1)
        self.btn_G = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_G.setObjectName("btn_G")
        self.gridLayout.addWidget(self.btn_G, 1, 5, 1, 1)
        self.btn_F = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_F.setObjectName("btn_F")
        self.gridLayout.addWidget(self.btn_F, 1, 4, 1, 1)
        self.btn_S = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_S.setObjectName("btn_S")
        self.gridLayout.addWidget(self.btn_S, 1, 2, 1, 1)
        self.btn_H = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_H.setObjectName("btn_H")
        self.gridLayout.addWidget(self.btn_H, 1, 6, 1, 1)
        self.btn_J = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_J.setObjectName("btn_J")
        self.gridLayout.addWidget(self.btn_J, 1, 7, 1, 1)
        self.btn_A = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_A.setObjectName("btn_A")
        self.gridLayout.addWidget(self.btn_A, 1, 1, 1, 1)
        self.btn_K = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_K.setObjectName("btn_K")
        self.gridLayout.addWidget(self.btn_K, 1, 8, 1, 1)
        self.btn_C = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_C.setObjectName("btn_C")
        self.gridLayout.addWidget(self.btn_C, 2, 3, 1, 1)
        self.btn_X = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_X.setObjectName("btn_X")
        self.gridLayout.addWidget(self.btn_X, 2, 2, 1, 1)
        self.btn_V = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_V.setObjectName("btn_V")
        self.gridLayout.addWidget(self.btn_V, 2, 4, 1, 1)
        self.btn_Y = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_Y.setObjectName("btn_Y")
        self.gridLayout.addWidget(self.btn_Y, 2, 1, 1, 1)
        self.btn_B = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_B.setObjectName("btn_B")
        self.gridLayout.addWidget(self.btn_B, 2, 5, 1, 1)
        self.btn__ = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn__.setObjectName("btn__")
        self.gridLayout.addWidget(self.btn__, 2, 8, 1, 1)
        self.btn_N = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_N.setObjectName("btn_N")
        self.gridLayout.addWidget(self.btn_N, 2, 6, 1, 1)
        self.btn_M = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_M.setObjectName("btn_M")
        self.gridLayout.addWidget(self.btn_M, 2, 7, 1, 1)
        self.btn_erase = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_erase.setObjectName("btn_erase")
        self.gridLayout.addWidget(self.btn_erase, 0, 10, 1, 1)
        self.btn_Q_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_Q_2.setObjectName("btn_Q_2")
        self.gridLayout.addWidget(self.btn_Q_2, 0, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

       
       



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tastatur"))
        self.btn_I_2.setText(_translate("Form", "I"))
        self.btn_O_2.setText(_translate("Form", "O"))
        self.btn_R_2.setText(_translate("Form", "R"))
        self.btn_P_2.setText(_translate("Form", "P"))
        self.btn_Z_2.setText(_translate("Form", "Z"))
        self.btn_U_2.setText(_translate("Form", "U"))
        self.btn_T_2.setText(_translate("Form", "T"))
        self.btn_W_2.setText(_translate("Form", "W"))
        self.btn_E_2.setText(_translate("Form", "E"))
        self.btn_L.setText(_translate("Form", "L"))
        self.btn_D.setText(_translate("Form", "D"))
        self.btn_G.setText(_translate("Form", "G"))
        self.btn_F.setText(_translate("Form", "F"))
        self.btn_S.setText(_translate("Form", "S"))
        self.btn_H.setText(_translate("Form", "H"))
        self.btn_J.setText(_translate("Form", "J"))
        self.btn_A.setText(_translate("Form", "A"))
        self.btn_K.setText(_translate("Form", "K"))
        self.btn_C.setText(_translate("Form", "C"))
        self.btn_X.setText(_translate("Form", "X"))
        self.btn_V.setText(_translate("Form", "V"))
        self.btn_Y.setText(_translate("Form", "Y"))
        self.btn_B.setText(_translate("Form", "B"))
        self.btn__.setText(_translate("Form", "_"))
        self.btn_N.setText(_translate("Form", "N"))
        self.btn_M.setText(_translate("Form", "M"))
        self.btn_erase.setText(_translate("Form", "<--"))
        self.btn_Q_2.setText(_translate("Form", "Q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
