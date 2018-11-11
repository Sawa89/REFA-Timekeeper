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
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *

class AnalogClock(QtWidgets.QWidget):   # diese Klasse ist für das Erstellen und Aktualisieren der analogen Uhren zuständig
    numbers = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
    numbers_min = ["5", "10", "15", "20", "25", "30"]

    hourHand = QtGui.QPolygon([
        QPoint(5, 6),
        QPoint(-5, 6),
        QPoint(0, -40)
    ])

    minuteHand = QtGui.QPolygon([
        QPoint(5, 6),
        QPoint(-5, 6),
        QPoint(0, -40)
    ])

    secondHand = QtGui.QPolygon([
        QPoint(3, 4),
        QPoint(-3, 4),
        QPoint(0, -90)
    ])
   
    hourColor = QtGui.QColor(0, 0, 255)
    minuteColor = QtGui.QColor(0, 255, 0)
    secondColor = QtGui.QColor(255, 0, 0)
    stunden = 0
    minuten = 0
    sekunden = 0

    def __init__(self, x, y, parent=QWidget):
        super(AnalogClock, self).__init__(parent)

        #timer = QTimer(self)
        #timer.timeout.connect(self.update)
        #timer.start(1000)

        self.resize(x, y)

    def erfasseZeit(self, hour, min, sec):
        self.stunden = hour
        self.minuten = min
        self.sekunden = sec
        self.update()
        

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        #time = QTime.currentTime()
 
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        #painter.setPen(Qt.NoPen)
        #painter.setBrush(AnalogClock.hourColor)

        #painter.save()
        #painter.rotate(30.0 * ((self.stunden + self.minuten / 60.0)))
        #painter.drawConvexPolygon(AnalogClock.hourHand)
        #painter.restore()

        painter.setPen(AnalogClock.hourColor)

        for i in range(20):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(18.0)

        painter.rotate(-30.0)
        for i in range(30):
            if (i % 5) != 0:
                painter.setPen(AnalogClock.minuteColor)
                painter.drawLine(48, 0, 50, 0)
            else:
                painter.setPen(AnalogClock.hourColor)
                painter.drawLine(45, 0, 50, 0)
            painter.rotate(12.0)

        painter.rotate(30.0)

        painter.setFont(QFont('Arial', 12))
        painter.setPen(QColor(Qt.SolidPattern))
        painter.drawText(-13, -65, self.numbers[9]) # 100
        painter.drawText(32, -57, self.numbers[0])  # 10
        painter.drawText(59, -20, self.numbers[1])  # 20
        painter.drawText(59, 32, self.numbers[2])   # 30
        painter.drawText(32, 68, self.numbers[3])   # 40
        painter.drawText(-6.5, 78, self.numbers[4]) # 50
        painter.drawText(-44, 68, self.numbers[5])  # 60
        painter.drawText(-74, 32, self.numbers[6])  # 70
        painter.drawText(-76, -17, self.numbers[7]) # 80
        painter.drawText(-48, -57, self.numbers[8]) # 90

        painter.drawText(-10, -27, self.numbers_min[5])
        painter.drawText(25, -10, self.numbers_min[0])
        painter.drawText(14, 22, self.numbers_min[1])
        painter.drawText(-10, 40, self.numbers_min[2])
        painter.drawText(-30, 22, self.numbers_min[3])
        painter.drawText(-35, -7, self.numbers_min[4])


        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.minuteColor)

        painter.save()
        painter.rotate(12.0 * self.minuten)
        painter.drawConvexPolygon(AnalogClock.minuteHand)
        painter.restore()

        painter.setPen(AnalogClock.minuteColor)

        for j in range(100):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(3.6)

        painter.setPen(Qt.NoPen)
        painter.setBrush(AnalogClock.secondColor)

        painter.save()
        painter.rotate(3.6 * self.sekunden)
        painter.drawConvexPolygon(AnalogClock.secondHand)
        painter.restore()
