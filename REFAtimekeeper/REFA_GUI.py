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
from PyQt5.QtCore import QRunnable, QThreadPool, QThread, QCoreApplication
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from REFAtimekeeper.soundplayer import SoundPlayer
from REFAtimekeeper import Bilder, datenbank, dialog_StNa, Analoguhr, dialog_StStart
import time, sqlite3
from REFAtimekeeper import dialog_KonfFrage, dialog_DatVorh, dialog_Hinweis, dialog_Ende, tastatur
from REFAtimekeeper import dialog_fortfahren, dialog_admin, Nummernblock, dialog_passwort, dialog_Epsi
from REFAtimekeeper import dialog_ergebnis

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Bilder/zeiticon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/Bilder/zeiticon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 401))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(0, -10, 411, 411))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.button_starteStu = QtWidgets.QPushButton(self.frame_2)
        self.button_starteStu.setGeometry(QtCore.QRect(20, 350, 141, 51))
        self.button_starteStu.setStyleSheet("font: 75 12pt \"Arial\";\n""background-color: rgb(111, 206, 33);")
        self.button_starteStu.setObjectName("button_starteStu")
        self.button_NeuStu = QtWidgets.QPushButton(self.frame_2)
        self.button_NeuStu.setGeometry(QtCore.QRect(20, 30, 311, 51))
        self.button_NeuStu.setStyleSheet("font: 75 20pt \"Arial\";\n""background-color: rgb(73, 210, 222);")
        self.button_NeuStu.setObjectName("button_NeuStu")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 351, 71))
        self.label_3.setObjectName("label_3")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 220, 311, 121))
        self.listWidget.setStyleSheet("font: 75 11pt \"Arial\";")
        self.listWidget.setObjectName("listWidget")
        self.button_Ausw = QtWidgets.QPushButton(self.frame_2)
        self.button_Ausw.setGeometry(QtCore.QRect(190, 350, 141, 51))
        self.button_Ausw.setStyleSheet("font: 75 12pt \"Arial\";\n""background-color: rgb(255, 170, 0);")
        self.button_Ausw.setObjectName("button_Ausw")
        self.btn_del = QtWidgets.QPushButton(self.frame_2)
        self.btn_del.setGeometry(QtCore.QRect(20, 180, 151, 31))
        self.btn_del.setStyleSheet("color: rgb(255, 0, 0);\n""background-color: rgb(206, 206, 206);\n""font: 75 14pt \"Arial\";")
        self.btn_del.setObjectName("btn_del")
        self.btn_copy = QtWidgets.QPushButton(self.frame_2)
        self.btn_copy.setGeometry(QtCore.QRect(180, 180, 151, 31))
        self.btn_copy.setStyleSheet("color: rgb(49, 121, 29);\n""background-color: rgb(206, 206, 206);\n""font: 75 14pt \"Arial\";")
        self.btn_copy.setObjectName("btn_copy")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(380, -10, 421, 411))
        self.frame.setStyleSheet("background-image: url(:/Bilder/Stoppuhr.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Analoguhr = QtWidgets.QWidget(self.page_2)
        self.Analoguhr.setGeometry(QtCore.QRect(10, 10, 121, 121))
        self.Analoguhr.setStyleSheet("")
        self.Analoguhr.setObjectName("Analoguhr")
        self.button_UhrStart = QtWidgets.QPushButton(self.page_2)
        self.button_UhrStart.setGeometry(QtCore.QRect(10, 185, 71, 41))
        self.button_UhrStart.setStyleSheet("font: 75 10pt \"Arial\";\n""background-color: rgb(85, 255, 0);")
        self.button_UhrStart.setObjectName("button_UhrStart")
        self.button_Beenden = QtWidgets.QPushButton(self.page_2)
        self.button_Beenden.setGeometry(QtCore.QRect(10, 309, 71, 41))
        self.button_Beenden.setStyleSheet("font: 75 10pt \"Arial\";\n""background-color: rgb(255, 124, 126);")
        self.button_Beenden.setObjectName("button_Beenden")
        self.button_Pause = QtWidgets.QPushButton(self.page_2)
        self.button_Pause.setGeometry(QtCore.QRect(10, 247, 71, 41))
        self.button_Pause.setStyleSheet("font: 75 10pt \"Arial\";\n""background-color: rgb(198, 223, 255);")
        self.button_Pause.setObjectName("button_Pause")
        self.stackedWidget_table = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget_table.setGeometry(QtCore.QRect(140, 0, 661, 361))
        self.stackedWidget_table.setObjectName("stackedWidget_table")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.Tabelle = QtWidgets.QTableWidget(self.page_3)
        self.Tabelle.setGeometry(QtCore.QRect(180, 0, 481, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tabelle.sizePolicy().hasHeightForWidth())
        self.Tabelle.setSizePolicy(sizePolicy)
        self.Tabelle.setRowCount(0)
        self.Tabelle.setColumnCount(0)
        self.Tabelle.setObjectName("Tabelle")
        self.Tabelle0 = QtWidgets.QTableWidget(self.page_3)
        self.Tabelle0.setGeometry(QtCore.QRect(10, 0, 171, 361))
        self.Tabelle0.setObjectName("Tabelle0")
        self.Tabelle0.setColumnCount(0)
        self.Tabelle0.setRowCount(0)
        self.stackedWidget_table.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.Tabelle_ti = QtWidgets.QTableWidget(self.page_4)
        self.Tabelle_ti.setGeometry(QtCore.QRect(180, 0, 481, 361))
        self.Tabelle_ti.setObjectName("Tabelle_ti")
        self.Tabelle_ti.setColumnCount(0)
        self.Tabelle_ti.setRowCount(0)
        self.Tabelle_ti0 = QtWidgets.QTableWidget(self.page_4)
        self.Tabelle_ti0.setGeometry(QtCore.QRect(10, 0, 171, 361))
        self.Tabelle_ti0.setObjectName("Tabelle_ti0")
        self.Tabelle_ti0.setColumnCount(0)
        self.Tabelle_ti0.setRowCount(0)
        self.stackedWidget_table.addWidget(self.page_4)
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 360, 661, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_120 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_120.setObjectName("btn_120")
        self.gridLayout.addWidget(self.btn_120, 0, 2, 1, 1)
        self.btn_90 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_90.setObjectName("btn_90")
        self.gridLayout.addWidget(self.btn_90, 0, 9, 1, 1)
        self.btn_105 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_105.setObjectName("btn_105")
        self.gridLayout.addWidget(self.btn_105, 0, 5, 1, 1)
        self.btn_125 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_125.setObjectName("btn_125")
        self.gridLayout.addWidget(self.btn_125, 0, 1, 1, 1)
        self.btn_80 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_80.setObjectName("btn_80")
        self.gridLayout.addWidget(self.btn_80, 0, 11, 1, 1)
        self.btn_110 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_110.setObjectName("btn_110")
        self.gridLayout.addWidget(self.btn_110, 0, 4, 1, 1)
        self.btn_130 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_130.setObjectName("btn_130")
        self.gridLayout.addWidget(self.btn_130, 0, 0, 1, 1)
        self.btn_100 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_100.setObjectName("btn_100")
        self.gridLayout.addWidget(self.btn_100, 0, 6, 1, 1)
        self.btn_95 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_95.setObjectName("btn_95")
        self.gridLayout.addWidget(self.btn_95, 0, 7, 1, 1)
        self.btn_scrollDown = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_scrollDown.setObjectName("btn_scrollDown")
        self.gridLayout.addWidget(self.btn_scrollDown, 0, 12, 1, 1)
        self.btn_scrollUp = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_scrollUp.setObjectName("btn_scrollUp")
        self.gridLayout.addWidget(self.btn_scrollUp, 0, 13, 1, 1)
        self.btn_85 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_85.setObjectName("btn_85")
        self.gridLayout.addWidget(self.btn_85, 0, 10, 1, 1)
        self.btn_115 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_115.setObjectName("btn_115")
        self.gridLayout.addWidget(self.btn_115, 0, 3, 1, 1)
        self.lcd_abZeit = QtWidgets.QLCDNumber(self.page_2)
        self.lcd_abZeit.setGeometry(QtCore.QRect(10, 135, 51, 31))
        self.lcd_abZeit.setDigitCount(3)
        self.lcd_abZeit.setObjectName("lcd_abZeit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(92, 177, 41, 222))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_scrollRight = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_scrollRight.setObjectName("btn_scrollRight")
        self.verticalLayout.addWidget(self.btn_scrollRight)
        self.btn_scrollLeft = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_scrollLeft.setObjectName("btn_scrollLeft")
        self.verticalLayout.addWidget(self.btn_scrollLeft)
        self.btn_ausklammern = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_ausklammern.setObjectName("btn_ausklammern")
        self.verticalLayout.addWidget(self.btn_ausklammern)
        self.btn_MP = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_MP.setObjectName("btn_MP")
        self.verticalLayout.addWidget(self.btn_MP)
        self.btn_MS = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_MS.setObjectName("btn_MS")
        self.verticalLayout.addWidget(self.btn_MS)
        self.btn_MZ = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_MZ.setObjectName("btn_MZ")
        self.verticalLayout.addWidget(self.btn_MZ)
        self.rbtn_ti = QtWidgets.QRadioButton(self.page_2)
        self.rbtn_ti.setGeometry(QtCore.QRect(52, 365, 31, 22))
        self.rbtn_ti.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.rbtn_ti.setObjectName("rbtn_ti")
        self.rbtn_F = QtWidgets.QRadioButton(self.page_2)
        self.rbtn_F.setGeometry(QtCore.QRect(10, 365, 31, 22))
        self.rbtn_F.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.rbtn_F.setObjectName("rbtn_F")
        self.lcd_ZusatzZeit = QtWidgets.QLCDNumber(self.page_2)
        self.lcd_ZusatzZeit.setGeometry(QtCore.QRect(80, 135, 51, 31))
        self.lcd_ZusatzZeit.setDigitCount(3)
        self.lcd_ZusatzZeit.setObjectName("lcd_ZusatzZeit")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionNeue_Zeitstudie = QtWidgets.QAction(MainWindow)
        self.actionNeue_Zeitstudie.setObjectName("actionNeue_Zeitstudie")
        self.action_ffne_Zeitstudie = QtWidgets.QAction(MainWindow)
        self.action_ffne_Zeitstudie.setObjectName("action_ffne_Zeitstudie")
        self.action_ber_REFA_Zeitaufnahme = QtWidgets.QAction(MainWindow)
        self.action_ber_REFA_Zeitaufnahme.setObjectName("action_ber_REFA_Zeitaufnahme")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ### bis hier generierter Code des Designers


        self.statuslabel = QtWidgets.QLabel()
        self.statuslabel.setStyleSheet("font:bold 12pt \"Arial\";""color: rgb(255, 0, 0);")
        self.statusbar.addWidget(self.statuslabel, 2)


        self.Tabelle.setAlternatingRowColors(True)
        self.Tabelle_ti.setAlternatingRowColors(True)
        

        self.db_tables = datenbank.get_tables()         # bisherige Studien aus der Datenbank auslesen
        self.listWidget.addItems(self.db_tables)        # Studien zur Liste hinzufügen

        self.btn_100.setStyleSheet("background-color: rgb(0, 255, 0);")     # den Standard-Leistungsbutton farbig hervorheben

        
        self.zyklen = 20
        self.sekunden = 0   # Variablen für die Zeitmessung
        self.minuten = 0
        self.stunden = 0
        self.sec_Fortschritt = 0
        self.time_measure_old = 0
        self.abschnittsdauer = 0
        self.gestartet = 0  # Variable für den Start der Zeitmessung
        self.Konfig_behalten = 0    # Variable für Konfiguration der Abschnitte und Zyklen
        self.Leistungsgrad = 100    # Variablen für das Speichern des Leistungsgrads
        self.column_old = 2         # Spaltenvariable beginnt bei 2, da erst dort die einzelnen Zeiten beginnen
        self.row_old = 0
        self.button_old = QtWidgets.QPushButton()             # Variable die den zuletzt betätigten Leistungsgradbutton speichert
        self.loeschen = 0                   # Variable für das Löschen einer falschen Zeit
        self.x = 'xxx'
        self.blinken = 0            # Variable die das Blinken eines Buttons steuert
        self.push_counter = 0       # Variable die speichert, wie oft der jeweilige Button betätigt wurde, um blinken ein oder auszuschalten
        self.ms = 0             # Mensch_Störung
        self.mz = 0             # Mensch_Zusatz
        self.mp = 0             # Mensch_Pause
        self.start_mszp = 0     # Start eines Zusatzabschnittes
        self.dauer_mszp = 0     # Dauer eines Zusatzabschnittes
        self.ende_mszp = 0      # Ende eines Zusatzabschnittes
        self.change_Leistung = 0    # Variable die auf 1 wechselt, sobald ein Leistungsbutton betätigt wurde
        self.scroll = 0         # Variable zum Hochzählen des Integerwertes der Scrollbar
        self.update_possible = 0    # Variable die nach dem Erstellen der Tabellen auf 1 wechselt und ein Update der Abschnittsbezeichnungen ermöglicht
        self.abschnitte_exists = 0
        self.abschnitte = []
        self.daten_verworfen = 0
        self.werte_aus = 0
        
        # Verbindung der Button-Signale mit den entsprechenden Slots
        self.button_Beenden.clicked.connect(self.vorzeitig_beenden)
        self.button_Pause.clicked.connect(self.pausieren)
        self.button_UhrStart.clicked.connect(self.zeige_Hinweis)
        self.button_NeuStu.clicked.connect(self.neueZeitstudie)
        self.button_starteStu.clicked.connect(self.starteZeitstudie)
        self.btn_scrollDown.clicked.connect(self.scroll_down)
        self.btn_scrollUp.clicked.connect(self.scroll_up)
        self.btn_scrollLeft.clicked.connect(self.scroll_left)
        self.btn_scrollRight.clicked.connect(self.scroll_right)
        self.btn_ausklammern.clicked.connect(self.loesche_letzteZeit)
        self.rbtn_F.toggled.connect(self.wechsel_Tabellen)
        self.rbtn_ti.toggled.connect(self.wechsel_Tabellen)
        self.btn_100.clicked.connect(self.set_Leistungsgrad)
        self.btn_105.clicked.connect(self.set_Leistungsgrad)
        self.btn_110.clicked.connect(self.set_Leistungsgrad)
        self.btn_115.clicked.connect(self.set_Leistungsgrad)
        self.btn_120.clicked.connect(self.set_Leistungsgrad)
        self.btn_125.clicked.connect(self.set_Leistungsgrad)
        self.btn_130.clicked.connect(self.set_Leistungsgrad)
        self.btn_95.clicked.connect(self.set_Leistungsgrad)
        self.btn_90.clicked.connect(self.set_Leistungsgrad)
        self.btn_85.clicked.connect(self.set_Leistungsgrad)
        self.btn_80.clicked.connect(self.set_Leistungsgrad)
        self.btn_MP.clicked.connect(self.persoenliche_Pause)
        self.btn_MS.clicked.connect(self.stoerung)
        self.btn_MZ.clicked.connect(self.zusatz_Abschnitt)
        self.button_Ausw.clicked.connect(self.auswertung)
        self.btn_del.clicked.connect(self.loesche_Studie)
        self.btn_copy.clicked.connect(self.kopiere_studie)
        

        self.page_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Analoguhr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.uhr = Analoguhr.AnalogClock(121, 121, self.Analoguhr)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_Uhr)

        self.timer_blinken = QtCore.QTimer()
        self.timer_blinken.timeout.connect(self.btn_blinken)



        self.rbtn_F.setChecked(True)        # Die Tabelle mit den Fortschrittszeiten standardmäßig zu Beginn anzeigen, deshalb entsprechenden Radiobutton setzen


        self.rahmendialog_StStart = QtWidgets.QDialog()
        self.dialog_startStudie = dialog_StStart.Ui_Dialog()
        self.dialog_startStudie.setupUi(self.rahmendialog_StStart)
        self.dialog_startStudie.buttonBox.accepted.connect(self.erstelle_Tabelle)

        self.rahmendialog_neuStu = QtWidgets.QDialog()
        self.rahmendialog_neuStu.resize(760, 400)
        self.dialog_neueStudie = dialog_StNa.Ui_Dialog()
        self.dialog_neueStudie.setupUi(self.rahmendialog_neuStu)
        self.dialog_neueStudie.buttonBox.accepted.connect(self.update_list)

        self.rahmendialog_KonfFrage = QtWidgets.QDialog()
        self.dialog_FrageKonfig = dialog_KonfFrage.Ui_Dialog()
        self.dialog_FrageKonfig.setupUi(self.rahmendialog_KonfFrage)
        self.dialog_FrageKonfig.btn_ja.clicked.connect(self.alte_Konfig)
        self.dialog_FrageKonfig.btn_nein.clicked.connect(self.neue_Konfig)

        self.rahmendialog_DatVorh = QtWidgets.QDialog()
        self.dialog_DatVorh = dialog_DatVorh.Ui_Daten_vorhanden()
        self.dialog_DatVorh.setupUi(self.rahmendialog_DatVorh)
        self.dialog_DatVorh.btn_ja.clicked.connect(self.daten_verwerfen)

        self.rahmendialog_Hinweis = QtWidgets.QDialog()
        self.dialog_Hinweis = dialog_Hinweis.Ui_Hinweis()
        self.dialog_Hinweis.setupUi(self.rahmendialog_Hinweis)
        self.dialog_Hinweis.btn_ok.clicked.connect(self.starte_Uhr)

        self.rahmendialog_Ende = QtWidgets.QDialog()
        self.dialog_Ende = dialog_Ende.Ui_Ende()
        self.dialog_Ende.setupUi(self.rahmendialog_Ende)
        self.dialog_Ende.buttonBox.accepted.connect(self.beenden)
        self.dialog_Ende.buttonBox.rejected.connect(self.beenden)

        self.rahmendialog_ff = QtWidgets.QDialog()
        self.dialog_ff = dialog_fortfahren.Ui_Fortfahren()
        self.dialog_ff.setupUi(self.rahmendialog_ff)
        self.dialog_ff.btn_ja.clicked.connect(self.beenden)

        self.rahmemwidget_Tastatur = QtWidgets.QWidget(self.rahmendialog_neuStu)
        self.tastatur = tastatur.Ui_Form()
        self.tastatur.setupUi(self.rahmemwidget_Tastatur)
        self.rahmemwidget_Tastatur.setGeometry(QtCore.QRect(0, 0, 760, 140))

        self.rahmendialog_admin = QtWidgets.QDialog()
        self.dialog_admin = dialog_admin.Ui_Dialog()
        self.dialog_admin.setupUi(self.rahmendialog_admin)
        self.dialog_admin.btn_ja.clicked.connect(self.passwort_aufruf)
        self.dialog_admin.btn_nein.clicked.connect(self.kein_admin)

        self.rahmendialog_passwort = QtWidgets.QDialog()
        self.dialog_passwort = dialog_passwort.Ui_Dialog()
        self.dialog_passwort.setupUi(self.rahmendialog_passwort)
        self.dialog_passwort.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.nummernblock = Nummernblock.Ui_Form()
        self.nummernblock.setupUi(self.dialog_passwort.widget)

        self.rahmendialog_epsilon = QtWidgets.QDialog()
        self.dialog_epsilon = dialog_Epsi.Ui_Dialog()
        self.dialog_epsilon.setupUi(self.rahmendialog_epsilon)
        self.dialog_epsilon.buttonBox.accepted.connect(self.beginne_auswertung)

        self.rahmendialog_ergebnis = QtWidgets.QDialog()
        self.dialog_ergebnis = dialog_ergebnis.Ui_Dialog()
        self.dialog_ergebnis.setupUi(self.rahmendialog_ergebnis)



        self.infobox_tablename = QtWidgets.QMessageBox()
        self.infobox_tablename.setIcon(QtWidgets.QMessageBox.Critical)
        self.infobox_tablename.setWindowTitle("Error")
        self.infobox_tablename.setText("Keine Sonderzeichen (außer Unterstrich) oder Leerzeichen verwenden!")
        self.infobox_tablename.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.infobox_studienauswahl = QtWidgets.QMessageBox()
        self.infobox_studienauswahl.setIcon(QtWidgets.QMessageBox.Critical)
        self.infobox_studienauswahl.setWindowTitle("Error")
        self.infobox_studienauswahl.setText("Wählen sie eine Studie aus, für die sie die Zeitaufnahme durchführen möchten!")
        self.infobox_studienauswahl.setDefaultButton(QtWidgets.QMessageBox.Ok)

        self.infobox_auswertung = QtWidgets.QMessageBox()
        self.infobox_auswertung.setIcon(QtWidgets.QMessageBox.Critical)
        self.infobox_auswertung.setWindowTitle("Error")
        self.infobox_auswertung.setText("Die Excel-Datei für diese Studie ist nicht vorhanden!")
        self.infobox_auswertung.setDefaultButton(QtWidgets.QMessageBox.Ok)

        self.infobox_passwort = QtWidgets.QMessageBox()
        self.infobox_passwort.setIcon(QtWidgets.QMessageBox.Critical)
        self.infobox_passwort.setWindowTitle("Error")
        self.infobox_passwort.setText("Falsche Passwort!")
        self.infobox_passwort.setDefaultButton(QtWidgets.QMessageBox.Ok)


        self.buttons_Tastatur = [self.tastatur.btn__, self.tastatur.btn_A, self.tastatur.btn_B, self.tastatur.btn_C, self.tastatur.btn_D, self.tastatur.btn_E_2, 
                        self.tastatur.btn_erase, self.tastatur.btn_F, self.tastatur.btn_G, self.tastatur.btn_H, self.tastatur.btn_I_2, 
                        self.tastatur.btn_J, self.tastatur.btn_K, self.tastatur.btn_L, self.tastatur.btn_M, self.tastatur.btn_N, self.tastatur.btn_O_2, self.tastatur.btn_P_2, 
                        self.tastatur.btn_Q_2, self.tastatur.btn_R_2, self.tastatur.btn_S, self.tastatur.btn_T_2, self.tastatur.btn_U_2, 
                        self.tastatur.btn_V, self.tastatur.btn_W_2, self.tastatur.btn_X, self.tastatur.btn_Y, self.tastatur.btn_Z_2]            # Array mit allen Tastaturbuttons

        for button in self.buttons_Tastatur:            
            button.clicked.connect(self.get_Tasten_Tastatur)        # alle Buttons des Arrays mit Funktion verbinden, die den Wert der gedrückten Taste abfragt


        self.buttons_Nummern = [self.nummernblock.button_0, self.nummernblock.button_1, self.nummernblock.button_2, self.nummernblock.button_3,
                                self.nummernblock.button_4, self.nummernblock.button_5, self.nummernblock.button_6, self.nummernblock.button_7,
                                self.nummernblock.button_8, self.nummernblock.button_9, self.nummernblock.button_bspace, self.nummernblock.button_OK, self.nummernblock.button_x]

        for button in self.buttons_Nummern:
            button.clicked.connect(self.get_Tasten_Nummernblock)



        self.Tabelle.itemSelectionChanged.connect(self.get_Zeiten)    #beim Anwählen einer anderen Zelle wird die Funktion aufgerufen, die die Fortschrittszeit in die Tabelle einträgt
        self.Tabelle_ti.itemSelectionChanged.connect(self.get_Zeiten)
        self.Tabelle0.itemChanged.connect(self.update_bezeichnung)
        

        self.rahmendialog_admin.exec_()             # vor dem eigentlichen Start der App nach Admin-Rechten fragen

        
    def get_Tasten_Nummernblock(self):
        taste = self.dialog_passwort.widget.sender()
        value = taste.text()
        if value == 'Backspace':
            self.dialog_passwort.lineEdit.backspace()
        elif value == 'X':
            self.rahmendialog_passwort.reject()
            self.kein_admin()
        elif value == 'OK':
            self.passwort_abfrage()
        else:
            self.dialog_passwort.lineEdit.insert(value)


    def get_Tasten_Tastatur(self):
        taste = self.tastatur.gridLayoutWidget.sender()
        value = taste.text()
        if value != 'Neue Zeitstudie':
            if value == '<--':
                self.dialog_neueStudie.input_studienname.backspace()
            else:
                self.dialog_neueStudie.input_studienname.insert(value)


    def neueZeitstudie(self):
        self.rahmendialog_neuStu.exec_()
        

    def passwort_aufruf(self):
        self.rahmendialog_passwort.exec_()


    def kein_admin(self):
        self.btn_del.setEnabled(False)


    def admin(self):
        self.btn_del.setEnabled(True)


    def passwort_abfrage(self):
        passwort = self.dialog_passwort.lineEdit.text()
        if passwort == '7889':
            self.rahmendialog_passwort.accept()
            self.admin()
        else:
            self.infobox_passwort.exec_()


    def starteZeitstudie(self):
        self.db_tables = datenbank.get_tables()
        if self.listWidget.count() != 0:
            try:
                if self.listWidget.currentItem().text() in self.db_tables:             #prüfen, ob sich die ausgewählte Zeitstudie in der Datenbank befindet
                    if datenbank.check_data_exists(self.listWidget.currentItem().text()) == 1:                                    #prüfen, ob sich in der Datenbank bereits Daten befinden
                        self.rahmendialog_DatVorh.exec_()
                    else:
                        self.dialog_FrageKonfig.lcd_Abschnitte.display(datenbank.get_numberofRows(self.listWidget.currentItem().text()))
                        self.dialog_FrageKonfig.lcd_Zyklen.display(datenbank.get_numberofColumns(self.listWidget.currentItem().text())-3)  # 3 subtrahieren, da die ersten 3 Spalten keine Messzyklen sind
                        self.rahmendialog_KonfFrage.exec_()  
                else:
                    self.rahmendialog_StStart.exec_()
            except AttributeError:
                self.infobox_studienauswahl.setText("Wählen sie eine Studie aus, für die sie die Zeitaufnahme durchführen möchten!")
                self.infobox_studienauswahl.exec_()


    def loesche_Studie(self):
        if self.listWidget.count() != 0:
            if self.listWidget.currentItem() != None:
                try:
                    studie = self.listWidget.currentItem().text()
                    datenbank.delete_table(studie)
                    self.listWidget.takeItem(self.listWidget.currentRow())
                except:
                    self.infobox_studienauswahl.setText("Datenbank gesperrt! Löschen erst nach Neustart der App möglich!")
                    self.infobox_studienauswahl.exec_()
            else:
                self.infobox_studienauswahl.setText("Wählen sie vorher die zu löschende Studie aus!")
                self.infobox_studienauswahl.exec_()
            

    def daten_verwerfen(self):
        self.abschnitte = datenbank.get_abschnitte(self.listWidget.currentItem().text())        # die Bezeichnungen der Abschnitte vor dem Löschen der Tabelle abspeichern
        rows = datenbank.get_numberofRows(self.listWidget.currentItem().text())
        columns = datenbank.get_numberofColumns(self.listWidget.currentItem().text())
        studie = self.listWidget.currentItem().text()
        datenbank.delete_table(studie)                 # Tabelle aus Datenbank löschen
        datenbank.create_table(studie)                 # Gleiche Tabelle neu erstellen, sodass keine Daten mehr vorhanden sind
        datenbank.add_columns(studie, columns-3)
        datenbank.insert_rows(studie, rows)
        self.dialog_FrageKonfig.lcd_Abschnitte.display(rows)
        self.dialog_FrageKonfig.lcd_Zyklen.display(columns-3)    # 3 subtrahieren, da die ersten 3 Spalten keine Messzyklen sind
        self.daten_verworfen = 1
        self.rahmendialog_KonfFrage.exec_()
   

    def neue_Konfig(self):
        self.Konfig_behalten = 0
        self.rahmendialog_StStart.exec_()


    def alte_Konfig(self):
        self.Konfig_behalten = 1
        self.erstelle_Tabelle()


    def update_list(self):
        studien = []
        for i in range(self.listWidget.count()):
            studien.append(self.listWidget.item(i).text())
        studie = self.dialog_neueStudie.input_studienname.text()
        if studie != "" and studie not in studien:
            self.listWidget.addItem(studie)


    def wechsel_Tabellen(self):
        if self.rbtn_F.isChecked():
            self.stackedWidget_table.setCurrentIndex(0)
        else:
            self.stackedWidget_table.setCurrentIndex(1)
            
        
    def erstelle_Tabelle(self): 
        self.update_possible = 0
        if self.Konfig_behalten == 1:
            if self.daten_verworfen == 0:
                self.abschnitte = datenbank.get_abschnitte(self.listWidget.currentItem().text())    # Bezeichnungen der Abschnitte wurden schon ausgelesen, wenn Daten verworfen wurden
            self.abschnitte_exists = 1          # die letzten Bezeichnungen der Abschnitte für die neue Tabelle übernehmen, wenn die aktuelle Konfiguration beibehalten wird
            self.Tabelle.setColumnCount(datenbank.get_numberofColumns(self.listWidget.currentItem().text())-3)  # 3 abziehen, da die ersten 3 Spalten aus der Datenbank nicht in diese Tabelle gehören (nur Zyklen)
            self.Tabelle.setRowCount(datenbank.get_numberofRows(self.listWidget.currentItem().text()))
            self.Tabelle0.setRowCount(datenbank.get_numberofRows(self.listWidget.currentItem().text()))
            self.Tabelle0.setColumnCount(2)
            self.Tabelle_ti.setColumnCount(datenbank.get_numberofColumns(self.listWidget.currentItem().text())-3)
            self.Tabelle_ti.setRowCount(datenbank.get_numberofRows(self.listWidget.currentItem().text()))
            self.Tabelle_ti0.setRowCount(datenbank.get_numberofRows(self.listWidget.currentItem().text()))
            self.Tabelle_ti0.setColumnCount(2)
        else:
            if self.listWidget.currentItem().text() in self.db_tables:
                datenbank.delete_table(self.listWidget.currentItem().text())         #vor dem Erstellen einer neuen Konfiguration, die alte Tabelle löschen, da es sonst zu einem Konflikt kommt
            try:
                datenbank.create_table(self.listWidget.currentItem().text())
            except:
                self.infobox_tablename.exec_()
                self.listWidget.takeItem(self.listWidget.currentRow())
                return
            datenbank.add_columns(self.listWidget.currentItem().text(), self.zyklen)
            datenbank.insert_rows(self.listWidget.currentItem().text(), self.dialog_startStudie.get_rows())
            self.Tabelle.setRowCount(self.dialog_startStudie.get_rows()) 
            self.Tabelle.setColumnCount(self.zyklen)   
            self.Tabelle0.setRowCount(self.dialog_startStudie.get_rows())
            self.Tabelle0.setColumnCount(2)
            self.Tabelle_ti.setRowCount(self.dialog_startStudie.get_rows())
            self.Tabelle_ti.setColumnCount(self.zyklen)
            self.Tabelle_ti0.setRowCount(self.dialog_startStudie.get_rows())
            self.Tabelle_ti0.setColumnCount(2)
        self.column_counter = [0]*self.Tabelle.rowCount()           # Array für das Hochzählen der Tabellenspalten während der Zeitaufnahme
        header = [None] * (self.Tabelle.columnCount()+2)                        #leeres Array für die Header der Tabelle erstellen 
        header[0] = 'Ablaufabschnitt'
        header[1] = 'Zy'
        self.Tabelle0.setColumnWidth(0, 105)
        self.Tabelle0.setColumnWidth(1, 30)
        self.Tabelle_ti0.setColumnWidth(0, 105)
        self.Tabelle_ti0.setColumnWidth(1, 30)
        for row in range(self.Tabelle.rowCount()):
            if self.abschnitte_exists == 1:
                self.Tabelle0.setItem(row, 0, QTableWidgetItem('%s' % (self.abschnitte[row])))
                self.Tabelle_ti0.setItem(row, 0, QTableWidgetItem('%s' % (self.abschnitte[row])))
                datenbank.abschnitt_entry(self.listWidget.currentItem().text(), self.abschnitte[row], row+1)
            else:
                self.Tabelle0.setItem(row, 0, QTableWidgetItem('Abschnitt %s' % (row+1)))
                self.Tabelle_ti0.setItem(row, 0, QTableWidgetItem('Abschnitt %s' % (row+1)))
            self.Tabelle0.setItem(row, 1, QTableWidgetItem('  F'))
            self.Tabelle0.item(row, 0).setBackground(QtGui.QColor(255, 249, 60))
            self.Tabelle0.item(row,0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.Tabelle_ti0.setItem(row, 1, QTableWidgetItem('  ti'))
            self.Tabelle_ti0.item(row, 0).setBackground(QtGui.QColor(255, 249, 60))
            self.Tabelle_ti0.item(row,0).setTextAlignment(QtCore.Qt.AlignCenter)
        for column in range(self.Tabelle.columnCount()):
            header[column+2] = str(column+1)
            self.Tabelle.setColumnWidth(column, 52)
            self.Tabelle_ti.setColumnWidth(column, 40)
        self.Tabelle.setHorizontalHeaderLabels(header[2:])
        self.Tabelle_ti.setHorizontalHeaderLabels(header[2:])
        self.statuslabel.setText("<html><head/><body><p align=\"center\">%s</p></body></html>" % self.listWidget.currentItem().text())
        self.stackedWidget.setCurrentIndex(1)
        self.update_possible = 1
        self.Konfig_behalten = 0
        self.daten_verworfen = 0
        self.abschnitte_exists = 0


    def kopiere_studie(self):
        try:
            try:
                self.db_tables = datenbank.get_tables()
                row = 0
                if self.listWidget.currentItem().text() in self.db_tables:
                    studie = self.listWidget.currentItem().text() + '2'
                    self.abschnitte = datenbank.get_abschnitte(self.listWidget.currentItem().text())    
                    rows = datenbank.get_numberofRows(self.listWidget.currentItem().text())
                    columns = datenbank.get_numberofColumns(self.listWidget.currentItem().text())
                    datenbank.create_table(studie)                 
                    datenbank.add_columns(studie, columns-3)
                    datenbank.insert_rows(studie, rows)
                    for abschnitt in self.abschnitte:
                         row += 1
                         datenbank.abschnitt_entry(studie, abschnitt, row)
                    self.listWidget.addItem(studie)
                else:
                    self.infobox_studienauswahl.setText("Diese Studie ist in der Datenbank noch nicht vorhanden!")
                    self.infobox_studienauswahl.exec_()
            except sqlite3.OperationalError:
                self.infobox_studienauswahl.setText("Von dieser Studie gibt es bereits eine Kopie!")
                self.infobox_studienauswahl.exec_()
        except AttributeError:
            self.infobox_studienauswahl.setText("Wählen sie die zu kopierende Studie aus!")
            self.infobox_studienauswahl.exec_()


    def update_bezeichnung(self):
        if self.update_possible == 1:
            bezeichnung = self.Tabelle0.item(self.Tabelle0.currentRow(), 0).text()
            self.Tabelle_ti0.setItem(self.Tabelle0.currentRow(), 0, QTableWidgetItem('%s' % bezeichnung))
            self.Tabelle_ti0.item(self.Tabelle0.currentRow(), 0).setBackground(QtGui.QColor(255, 249, 60))
            self.Tabelle_ti0.item(self.Tabelle0.currentRow(),0).setTextAlignment(QtCore.Qt.AlignCenter)
            datenbank.abschnitt_entry(self.listWidget.currentItem().text(), bezeichnung, self.Tabelle0.currentRow()+1)


    def zeige_Hinweis(self):                                # Hinweis beim Starten der Uhr zeigen, dass für das Messen der Zeit in die entsprechende Zeile des Abschnitts geklickt werden muss 
        if self.dialog_Hinweis.checkBox.isChecked():
            self.starte_Uhr()
        else:
            self.rahmendialog_Hinweis.exec_()


    def starte_Uhr(self):
        self.update_possible = 0
        self.timer.start(600)
        self.gestartet = 1


    def pausieren(self):
        self.timer.stop()
        self.gestartet = 0


    def vorzeitig_beenden(self):
        self.rahmendialog_ff.exec_()


    def beenden(self):
        self.timer.stop()
        self.timer_blinken.stop()
        self.gestartet = 0      # Variablen für die nächste Zeitmessung zurücksetzen
        self.sekunden = 0
        self.minuten = 0
        self.stunden = 0
        self.sec_Fortschritt = 0
        self.push_counter = 0
        self.ms = 0
        self.mz = 0
        self.mp = 0
        self.abschnittsdauer = 0
        self.lcd_abZeit.display(self.abschnittsdauer)
        self.uhr.erfasseZeit(self.stunden, self.minuten, self.sekunden)
        self.statuslabel.setText("")
        self.time_measure = 0
        self.time_measure_old = 0
        self.Tabelle.setRowCount(0)
        self.Tabelle_ti.setRowCount(0)      # Daten aus Tabelle löschen, indem die Zeilen auf 0 gesetzt werden
        self.stackedWidget.setCurrentIndex(0)
        datenbank.export_toCSV(self.listWidget.currentItem().text())        # beim Beenden der Zeitmessung die aufgenommenen Daten in csv-Dateien schreiben


    def beginne_auswertung(self):
        self.werte_aus = 1


    def auswertung_grafisch(self, soll):
        datenbank.auswertung_abschnittsdauer(self.listWidget.currentItem().text())
        e, n = datenbank.auswertung_zyklisch(soll)
        if n == 0:                              # wenn keine weiteren Zeiten erforderlich sind, Label grün hervorheben
            self.dialog_ergebnis.label_ist.setStyleSheet("font: 75 11pt \"Arial\";\n""background-color: rgb(0, 255, 0);")
        else:
            self.dialog_ergebnis.label_ist.setStyleSheet("font: 75 11pt \"Arial\";\n""background-color: rgb(255, 0, 0);")
        self.dialog_ergebnis.label_ist.setText('%s' % str(e))
        self.dialog_ergebnis.label_soll.setText('%s' % str(soll))
        self.dialog_ergebnis.label_n.setText('%s' % str(n))
        self.rahmendialog_ergebnis.exec_()
        datenbank.auswertung_epsilon(self.listWidget.currentItem().text(), soll)
        

    def auswertung(self):
        try:
            self.db_tables = datenbank.get_tables()
            if self.listWidget.currentItem().text() in self.db_tables:
                if datenbank.check_data_exists(self.listWidget.currentItem().text()) == 0:
                    self.infobox_auswertung.setText("Für diese Studie sind noch keine Daten vorhanden!")
                    self.infobox_auswertung.exec_()
                else:
                    if datenbank.check_eval_possible(self.listWidget.currentItem().text()) == 1:
                        try:
                            self.rahmendialog_epsilon.exec_()
                            if self.werte_aus == 1:
                                if self.dialog_epsilon.rbtn_10.isChecked():
                                    self.auswertung_grafisch(10)
                                else:
                                    self.auswertung_grafisch(5)
                                self.werte_aus = 0
                        except:
                            self.infobox_auswertung.setText("Die Excel-Datei für diese Studie ist nicht vorhanden oder wurde umbenannt!")
                            self.infobox_auswertung.exec_()
                    else:
                        self.infobox_auswertung.setText("Für diese Studie sind nicht genug Daten für die Auswertung vorhanden!")
                        self.infobox_auswertung.exec_()
            else:
                self.infobox_auswertung.setText("Für diese Studie sind noch keine Daten vorhanden!")
                self.infobox_auswertung.exec_()
        except AttributeError:
            self.infobox_studienauswahl.setText("Wählen sie eine Studie aus, für die sie die Auswertung durchführen möchten!")
            self.infobox_studienauswahl.exec_()


    def update_Uhr(self):                   # Methode, die mit dem Timer verbunden ist und im Sekundentakt die Zeiten aufaddiert
        self.sec_Fortschritt += 1
        self.abschnittsdauer += 1
        if self.ms == 1 or self.mp == 1 or self.mz == 1:
            self.dauer_mszp += 1
        self.sekunden += 1
        if self.sekunden >= 100:
            self.minuten = self.minuten + 1
            self.sekunden = 0
        if self.minuten >= 30:
            self.stunden = self.stunden + 1
            self.minuten = 0
        if self.stunden >= 12:
            self.stunden = 0
        self.uhr.erfasseZeit(self.stunden, self.minuten, self.sekunden)
        if self.ms == 0 and self.mp == 0 and self.mz == 0:  # falls ein Zusatzabschnitt aktiv ist, die Anzeige der Abschnittsdauer anhalten
            self.lcd_abZeit.display(self.abschnittsdauer)
        self.lcd_ZusatzZeit.display(self.dauer_mszp)
        #SoundPlayer.playTone(300, 0.05, False, 0)                      # Ton im Sekundentakt abspielen (nur für Raspberry von Relevanz)
        

    def get_Zeiten(self):
        if self.gestartet == 1 and self.ms == 0 and self.mp == 0 and self.mz == 0 and self.abschnittsdauer > 1: # die Zeit eines Abschnitts wird nur gestoppt, solange kein Zusatzabschnitt läuft und die Abschnittsdauer nicht unrealistisch klein ist
            full = datenbank.check_tabel_full(self.listWidget.currentItem().text(), self.Tabelle.rowCount(), self.Tabelle.columnCount()-1)   # zuerst prüfen, ob die Tabelle komplett mit Daten gefüllt ist
            if full == 1:
                datenbank.data_entry_leistung(self.listWidget.currentItem().text(), self.column_old, self.Leistungsgrad, self.row_old) # vor dem Beenden der Zeitaufnahme den letzen Leistungsgrad abspeichern
                self.rahmendialog_Ende.exec_()          # dem Benutzer mitteilen, dass die Zeitaufnahme beendet ist und die Daten erfolgreich gespeichert wurden
            table = self.stackedWidget_table.sender()
            if table.objectName() == 'Tabelle':
                row = self.Tabelle.currentRow()                         # Zeile ausfindig machen, in die geklickt wurde
            else:
                row = self.Tabelle_ti.currentRow()
            
            if self.column_counter[row] < (self.Tabelle.columnCount()):       # solange die Spalten hochzählen, bis alle Zyklen mit Zeiten gefüllt sind
                self.time_measure = self.sec_Fortschritt       # aktuelle Zeit in Variable speichern
                self.Tabelle.setItem(row, self.column_counter[row], QTableWidgetItem(str(self.time_measure)))        # Tabelle in GUI mit der gemessenen Zeit füllen
                self.Tabelle_ti.setItem(row, self.column_counter[row], QTableWidgetItem(str(self.abschnittsdauer)))
                datenbank.data_entry_fortschritt(self.listWidget.currentItem().text(), self.column_counter[row], str(self.time_measure), row) # Fortschrittswerte in die Datenbank schreiben
                datenbank.data_entry_abschnitt(self.listWidget.currentItem().text(), self.column_counter[row], str(self.abschnittsdauer), row) # Abschnittswerte in die Datenbank schreiben
                if self.loeschen == 1:      
                    datenbank.data_entry_fortschritt(self.listWidget.currentItem().text(), self.column_old, self.x, self.row_old) # falsche Zeit aus Datenbank löschen
                    datenbank.data_entry_abschnitt(self.listWidget.currentItem().text(), self.column_old, self.x, self.row_old) # falsche Zeit aus Datenbank löschen
                    self.Tabelle.setItem(self.row_old, self.column_old, QTableWidgetItem(self.x))
                    self.Tabelle_ti.setItem(self.row_old, self.column_old, QTableWidgetItem(self.x))
                    self.loeschen = 0
                if self.change_Leistung == 1:
                    datenbank.data_entry_leistung(self.listWidget.currentItem().text(), self.column_old, self.Leistungsgrad, self.row_old) # Leistungswerte in die Datenbank schreiben
                    self.change_Leistung = 0
                self.Leistungsgrad = 100            # solange kein anderer Leistungsgrad gemessen wurde, den Standardwert 100 eintragen
                datenbank.data_entry_leistung(self.listWidget.currentItem().text(), self.column_counter[row], self.Leistungsgrad, row) # Leistungswerte in die Datenbank schreiben
                self.abschnittsdauer = 0
                self.lcd_abZeit.display(self.abschnittsdauer)
                self.time_measure_old = self.time_measure
                self.button_old.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.btn_100.setStyleSheet("background-color: rgb(0, 255, 0);")
                self.btn_ausklammern.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.row_old = row
                self.column_old = self.column_counter[row]
                self.column_counter[row] = self.column_counter[row] + 1  # pro Klick in eine Zeile, eine Spalte hochzählen, sodass Wert in nächste Spalte eingetragen wird
            


    def set_Leistungsgrad(self):
        if self.gestartet == 1:
            self.change_Leistung = 1
            self.button_old.setStyleSheet("background-color: rgb(255, 255, 255);")  # vorherigen Button farblich zurücksetzen
            self.btn_100.setStyleSheet("background-color: rgb(255, 255, 255);")  
            button = self.stackedWidget.sender()            # Leistungs-Button ausfindig machen, der betätigt wurde, um im nächsten Schritt dessen Wert zu extrahieren
            self.Leistungsgrad = button.text()
            button.setStyleSheet("background-color: rgb(85, 255, 0);")
            self.button_old = button



    def scroll_up(self):
        self.Tabelle.verticalScrollBar().setValue(self.Tabelle.verticalScrollBar().minimum())
        self.Tabelle_ti.verticalScrollBar().setValue(self.Tabelle_ti.verticalScrollBar().minimum())
        self.Tabelle0.verticalScrollBar().setValue(self.Tabelle.verticalScrollBar().minimum())
        self.Tabelle_ti0.verticalScrollBar().setValue(self.Tabelle_ti.verticalScrollBar().minimum())

    def scroll_down(self):
        self.Tabelle.verticalScrollBar().setValue(self.Tabelle.verticalScrollBar().maximum())
        self.Tabelle_ti.verticalScrollBar().setValue(self.Tabelle_ti.verticalScrollBar().maximum())
        self.Tabelle0.verticalScrollBar().setValue(self.Tabelle.verticalScrollBar().maximum())
        self.Tabelle_ti0.verticalScrollBar().setValue(self.Tabelle_ti.verticalScrollBar().maximum())


    def scroll_right(self):
        self.scroll += 8
        self.Tabelle.horizontalScrollBar().setValue(self.scroll)
        self.Tabelle_ti.horizontalScrollBar().setValue(self.scroll)
      

    def scroll_left(self):
        self.scroll = 0
        self.Tabelle.horizontalScrollBar().setValue(self.scroll)
        self.Tabelle_ti.horizontalScrollBar().setValue(self.scroll)


    def loesche_letzteZeit(self):
        if self.gestartet == 1 and self.ms == 0 and self.mz == 0 and self.mp == 0:  # letzte Zeit kann nur gelöscht werden, wenn gerade kein Zusatzabschnitt aktiv ist
            self.btn_ausklammern.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.abschnittsdauer = 0
            self.lcd_abZeit.display(self.abschnittsdauer)
            self.loeschen = 1


    def zusatz_Abschnitt(self):         # Methode für einen zusätzlichen MZ-Abschnitt
        if self.gestartet == 1 and self.mp == 0 and self.ms == 0:
            if self.push_counter < 1:
                self.mz = 1
                self.start_mszp = self.sec_Fortschritt
                self.push_counter += 1
                self.timer_blinken.start(500)
            else:
                self.mz = 0
                self.ende_mszp = self.sec_Fortschritt
                datenbank.additional_row(self.listWidget.currentItem().text(), 'MZ', self.start_mszp, self.ende_mszp, self.dauer_mszp)
                self.push_counter = 0
                self.start_mszp = 0
                self.ende_mszp = 0
                self.abschnittsdauer = self.abschnittsdauer - self.dauer_mszp
                self.dauer_mszp = 0
                self.timer_blinken.stop()
                self.btn_MZ.setStyleSheet("background-color: rgb(255, 255, 255);")


    def persoenliche_Pause(self):       # Methode für einen zusätzlichen MP-Abschnitt
        if self.gestartet == 1 and self.ms == 0 and self.mz == 0:
            if self.push_counter < 1:
                self.mp = 1
                self.start_mszp = self.sec_Fortschritt
                self.push_counter += 1
                self.timer_blinken.start(500)
            else:
                self.push_counter = 0
                self.mp = 0
                self.ende_mszp = self.sec_Fortschritt
                datenbank.additional_row(self.listWidget.currentItem().text(), 'MP', self.start_mszp, self.ende_mszp, self.dauer_mszp)
                self.start_mszp = 0
                self.ende_mszp = 0
                self.abschnittsdauer = self.abschnittsdauer - self.dauer_mszp
                self.dauer_mszp = 0
                self.timer_blinken.stop()
                self.btn_MP.setStyleSheet("background-color: rgb(255, 255, 255);")


    def stoerung(self):         # Methode für einen zusätzlichen MS-Abschnitt
        if self.gestartet == 1 and self.mz == 0 and self.mp == 0:
            if self.push_counter < 1:
                self.ms = 1
                self.start_mszp = self.sec_Fortschritt
                self.push_counter += 1
                self.timer_blinken.start(500)
            else:
                self.push_counter = 0
                self.ms = 0
                self.ende_mszp = self.sec_Fortschritt
                datenbank.additional_row(self.listWidget.currentItem().text(), 'MS', self.start_mszp, self.ende_mszp, self.dauer_mszp)
                self.start_mszp = 0
                self.ende_mszp = 0
                self.abschnittsdauer = self.abschnittsdauer - self.dauer_mszp
                self.dauer_mszp = 0
                self.timer_blinken.stop()
                self.btn_MS.setStyleSheet("background-color: rgb(255, 255, 255);")


    def btn_blinken(self):
        if self.gestartet == 1:
            if self.mz == 1:
                if self.blinken == 0:
                    self.btn_MZ.setStyleSheet("background-color: rgb(0, 205, 205);")
                    self.blinken = 1
                else:
                    self.btn_MZ.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.blinken = 0
            elif self.mp == 1:
                if self.blinken == 0:
                    self.btn_MP.setStyleSheet("background-color: rgb(0, 205, 205);")
                    self.blinken = 1
                else:
                    self.btn_MP.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.blinken = 0
            elif self.ms == 1:
                if self.blinken == 0:
                    self.btn_MS.setStyleSheet("background-color: rgb(0, 205, 205);")
                    self.blinken = 1
                else:
                    self.btn_MS.setStyleSheet("background-color: rgb(255, 255, 255);")
                    self.blinken = 0



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REFA - Zeitaufnahme"))
        self.button_starteStu.setText(_translate("MainWindow", "Zeitaufnahme "))
        self.button_NeuStu.setText(_translate("MainWindow", "Neue Zeitstudie"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Wählen sie eine Studie für die Zeitaufnahme</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">oder die Auswertung aus</span></p></body></html>"))
        self.button_Ausw.setText(_translate("MainWindow", "Auswertung"))
        self.btn_del.setText(_translate("MainWindow", "Löschen"))
        self.btn_copy.setText(_translate("MainWindow", "Kopieren"))
        self.button_UhrStart.setText(_translate("MainWindow", "Start"))
        self.button_Beenden.setText(_translate("MainWindow", "Ende"))
        self.button_Pause.setText(_translate("MainWindow", "Pause"))
        self.btn_120.setText(_translate("MainWindow", "120"))
        self.btn_90.setText(_translate("MainWindow", "90"))
        self.btn_105.setText(_translate("MainWindow", "105"))
        self.btn_125.setText(_translate("MainWindow", "125"))
        self.btn_80.setText(_translate("MainWindow", "80"))
        self.btn_110.setText(_translate("MainWindow", "110"))
        self.btn_130.setText(_translate("MainWindow", "130"))
        self.btn_100.setText(_translate("MainWindow", "100"))
        self.btn_95.setText(_translate("MainWindow", "95"))
        self.btn_scrollDown.setText(_translate("MainWindow", "▼"))
        self.btn_scrollUp.setText(_translate("MainWindow", "▲"))
        self.btn_85.setText(_translate("MainWindow", "85"))
        self.btn_115.setText(_translate("MainWindow", "115"))
        self.btn_scrollRight.setText(_translate("MainWindow", "►"))
        self.btn_scrollLeft.setText(_translate("MainWindow", "◄"))
        self.btn_ausklammern.setText(_translate("MainWindow", "( )"))
        self.btn_MP.setText(_translate("MainWindow", "MP"))
        self.btn_MS.setText(_translate("MainWindow", "MS"))
        self.btn_MZ.setText(_translate("MainWindow", "MZ"))
        self.rbtn_ti.setText(_translate("MainWindow", "ti"))
        self.rbtn_F.setText(_translate("MainWindow", "F"))
        self.actionNeue_Zeitstudie.setText(_translate("MainWindow", "Neue Zeitstudie"))
        self.action_ffne_Zeitstudie.setText(_translate("MainWindow", "Öffne Zeitstudie"))
        self.action_ber_REFA_Zeitaufnahme.setText(_translate("MainWindow", "Über REFA-Zeitaufnahme"))





class MainWIndow_MouseEvent(QtWidgets.QMainWindow):      # Diese Klasse ist nur dafür zuständig, eventuell benötigte Events über den Eventfilter zu registrieren
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
      
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = QtWidgets.QMainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
        
        
        
        
    #def eventFilter(self, source, event):
        #if event.type() == QtCore.QEvent.MouseButtonPress:
            #if source == self.ui.comboBox:
                #self.ui.centralwidget.event(QEvent.TouchEnd) 
            
       # return QtWidgets.QMainWindow.eventFilter(self, source, event)

                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWIndow_MouseEvent()
    MainWindow.show()
    app.installEventFilter(MainWindow)
    sys.exit(app.exec_())
