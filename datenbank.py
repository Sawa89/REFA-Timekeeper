#pylint:disable=E1101

import sqlite3
import csv
import numpy as np
import matplotlib.pyplot as plt
import os


conn_0 = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'REFA_Zeitstudien.db'))         # Hier wird eine neue Datenbank mit dem entsprechenden Namen erstellt
cursor_0 = conn_0.cursor()

conn_1 = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'REFA_Zeiten.db'))              
cursor_1 = conn_1.cursor()

f = '_Fortschrittsdauer'    # Variablen, um die einzelnen Datenbank-Tabellen zu benennen
t = '_Abschnittsdauer'
l = '_Leistungsgrad'
z = '_Zusatzabschnitte'

ff = 'Fortschrittsdauer'    # Variablen, um die einzelnen CSV-Dateien zu benennen
tt = 'Abschnittsdauer'
ll = 'Leistungsgrad'
zz = 'Zusatzabschnitte'



def create_table(table):    #erstelle eine neue Tabelle in der jeweiligen Datenbank mit dem entsprechenden Grundgerüst an Spalten
    cursor_0.execute("CREATE TABLE IF NOT EXISTS %s (Id INTEGER PRIMARY KEY, Ablaufabschnitt TEXT, Zyklus TEXT)" % (table))
    cursor_1.execute("CREATE TABLE IF NOT EXISTS %s (Id INTEGER PRIMARY KEY, Ablaufabschnitt TEXT, Zyklus TEXT)" % (table + f))
    cursor_1.execute("CREATE TABLE IF NOT EXISTS %s (Id INTEGER PRIMARY KEY, Ablaufabschnitt TEXT, Zyklus TEXT)" % (table + t))
    cursor_1.execute("CREATE TABLE IF NOT EXISTS %s (Id INTEGER PRIMARY KEY, Ablaufabschnitt TEXT, Zyklus TEXT)" % (table + l))
    cursor_1.execute("CREATE TABLE IF NOT EXISTS %s (Id INTEGER PRIMARY KEY, Ablaufabschnitt TEXT, Start TEXT, Ende TEXT, Dauer TEXT)" % (table + z))


def delete_table(table):    #lösche die jeweiligen Tabellen aus der Datenbank
    cursor_0.executescript('DROP TABLE IF EXISTS %s' % (table))
    cursor_1.executescript('DROP TABLE IF EXISTS %s' % (table + f))
    cursor_1.executescript('DROP TABLE IF EXISTS %s' % (table + t))
    cursor_1.executescript('DROP TABLE IF EXISTS %s' % (table + l))
    cursor_1.executescript('DROP TABLE IF EXISTS %s' % (table + z))


def add_columns(table, number): #füge Spalten in der angegebenen Anzahl hinzu
    columns = [None] * number
    for x in range(number):
        columns[x] = str(x+1)
        cursor_0.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                 .format(tn=table, cn=columns[x], ct='TEXT'))
        cursor_1.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                 .format(tn=table + f, cn=columns[x], ct='TEXT'))
        cursor_1.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                 .format(tn=table + t, cn=columns[x], ct='TEXT'))
        cursor_1.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
                 .format(tn=table + l, cn=columns[x], ct='TEXT'))
    conn_0.commit() #speicher Datenbank 0
    conn_1.commit() #speicher Datenbank 1


def add_row(table, value):  # eine Zeile zu der entsprechenden Tabelle hinzufügen
    abschnitt = 'Abschnitt '+ str(value)
    cursor_0.execute("INSERT INTO %s (Ablaufabschnitt, Zyklus) VALUES ('%s', 'F')" % (table, abschnitt))
    cursor_1.execute("INSERT INTO %s (Ablaufabschnitt, Zyklus) VALUES ('%s', 'F')" % (table + f, abschnitt))
    cursor_1.execute("INSERT INTO %s (Ablaufabschnitt, Zyklus) VALUES ('%s', 'ti')" % (table + t, abschnitt))
    cursor_1.execute("INSERT INTO %s (Ablaufabschnitt, Zyklus) VALUES ('%s', 'L')" % (table + l, abschnitt))
    conn_0.commit()
    conn_1.commit()
    

def additional_row(table, art, beginn, ende, dauer):  # füge eine zusätzliche Zeile der entsprechenden Art des Zusatzabschnittes ein
    abschnitt = 'Zusatzabschnitt_' + art
    cursor_1.execute("INSERT INTO %s (Ablaufabschnitt, Start, Ende, Dauer) VALUES ('%s', '%d', '%d', '%d')" % (table + z, abschnitt, beginn, ende, dauer)) 
    conn_1.commit()


def insert_rows(table, rows):   #Zeilen in der angegebenen Anzahl zu der entsprechenden Tabelle hinzufügen
    for x in range(rows):
        add_row(table, (x+1))


def abschnitt_entry(table, abschnitt, row):
    cursor_1.execute("UPDATE %s SET 'Ablaufabschnitt' = '%s' WHERE Id = '%d'" % (table + f, abschnitt, row))
    cursor_1.execute("UPDATE %s SET 'Ablaufabschnitt' = '%s' WHERE Id = '%d'" % (table + t, abschnitt, row))
    cursor_1.execute("UPDATE %s SET 'Ablaufabschnitt' = '%s' WHERE Id = '%d'" % (table + l, abschnitt, row))
    conn_1.commit()


def get_abschnitte(table):
    abschnitte = []
    cursor_1.execute("SELECT * FROM %s" % (table + f))
    data = cursor_1.fetchall()
    for row in data:
        abschnitte.append(row[1])
    return abschnitte


def data_entry_fortschritt(table, column, value, row):  # füge Daten in die Fortschrittstabelle ein
    cursor_1.execute("UPDATE %s SET '%d' = '%s' WHERE Id = '%d'" % (table + f, (column+1), value, (row+1)))
    conn_1.commit()
    

def data_entry_abschnitt(table, column, value, row):    # füge Daten in die Abschnittstabelle ein
    cursor_1.execute("UPDATE %s SET '%d' = '%s' WHERE Id = '%d'" % (table + t, (column+1), value, (row+1)))
    conn_1.commit()


def data_entry_leistung(table, column, value, row): # füge Daten in die Leistungstabelle ein
    cursor_1.execute("UPDATE %s SET '%d' = '%s' WHERE Id = '%d'" % (table + l, (column+1), value, (row+1)))
    conn_1.commit()


def get_tables():   # Funktion, um die bisher angelegten Zeitstudien auszulesen
    cursor_0.execute("SELECT name FROM sqlite_master WHERE type='table'")
    data = cursor_0.fetchall()
    data = ["%s" % x for x in data ]  #Daten vom Typ Tuple in List umwandeln 
    return data


def get_numberofColumns(table):
    columnsQuery = "PRAGMA table_info(%s)" % table
    cursor_0.execute(columnsQuery)
    numberOfColumns = len(cursor_0.fetchall())
    return numberOfColumns


def get_numberofRows(table):
    rowsQuery = "SELECT Count() FROM %s" % table
    cursor_0.execute(rowsQuery)
    numberOfRows = cursor_0.fetchone()[0]
    return numberOfRows


def check_data_exists(table):    # Funktion um herauszufinden, ob sich schon Daten in den einzelnen Tabellen befinden
    cursor_1.execute("SELECT * FROM %s" % (table + f))  # es genügt, nur die Fortschrittstabelle zu untersuchen, da sich dann automatisch auch Daten in den übrigen Tabellen befinden
    data = cursor_1.fetchall()
    data_exists = 0
    for row in data:
        if row[3] != None:      # die erste Spalte mit möglichen Daten untersuchen
            data_exists = 1
    return data_exists


def check_eval_possible(table):     # Funktion um herauszufinden, ob für eine Auswertung genug Zeiten aufgenommen wurden
    cursor_1.execute("SELECT * FROM %s" % (table + f))
    data = cursor_1.fetchall()
    full_cell = 0
    possible = 0
    count = 0
    abschnitte = 0
    liste = []
    for row in data:
        liste.append([])
        for value in row[3:]:
            if value != None and value != 'xxx':
                liste[abschnitte].append(value)
        abschnitte += 1
    for abschnitt in liste:
        count += 1
        if len(abschnitt) >= 2:
            full_cell += 1
    if full_cell == count:      # nur wenn für jeden Abschnitt mindestens zwei Zeiten vorliegen, kann eine Auswertuung durchgeführt werden
        possible = 1
    return possible


def check_tabel_full(table, rows, column):      # Funktion die überprüft, ob die Tabelle mit Daten gefüllt ist und die Zeitaufnahme beendet werden kann
    cursor_1.execute("SELECT * FROM %s" % (table + f))
    data = cursor_1.fetchall()
    isFull = 0
    full_cell = 0
    for x in data:
        if x[column+1] != None:
            full_cell += 1
    if full_cell == rows:
        isFull = 1
    return isFull


def check_csv_path(table):      # neuen Ordner für die CSV Dateien erstellen, falls dieser noch nicht existiert
    path = os.path.join(os.path.dirname(__file__), "CSV", "%s") % (table)
    if not os.path.exists(path):
        os.makedirs(os.path.join(os.path.dirname(__file__), "CSV", "%s") % (table))


def write_csv(table, header, add):
    cursor_1.execute("SELECT * FROM %s" % (table + '_' + add))
    data = cursor_1.fetchall()                                          # alle Daten der Fortschrittstabelle in der Variable 'data' speichern
    with open(os.path.join(os.path.dirname(__file__), "CSV", "%s", "%s.csv") % (table, add), "w") as write_file:
        writeRow = ",".join([str(i) for i in header])
        write_file.write(writeRow + "\n")
        for row in data:
            writeRow = ",".join([str(i) for i in row])
            write_file.write(writeRow + "\n")
    

def export_toCSV(table):        # Funktion, die alle Tabellen einer Zeitaufnahme in csv Dateien exportiert, sodass diese in Excel verarbeitet werden können
    check_csv_path(table)
    cursor_0.execute("SELECT * FROM %s" % (table))
    names = [description[0] for description in cursor_0.description]    # die einzelnen Header des Tabellenkopfes müssen separat ausgelesen werden
    write_csv(table, names, ff)
    write_csv(table, names, tt)
    write_csv(table, names, ll)

    names = []
    count = 0
    cursor_1.execute("PRAGMA table_info('%s')" % (table + z))
    data = cursor_1.fetchall()
    for column in data:
        string = data[count][1]
        names.append(string)
        count += 1
    write_csv(table, names, zz)


def auswertung_abschnittsdauer(studie):             # Funktion, die die Durchschnittswerte der aufgenommenen Zeiten berechnet und grafisch darstellt
    global stdw
    global mean_t
    global str_liste
    global number_t
    global varianz
    global mean_ti
    global zyklus_sum
    number_t = []
    mean_L = []     # Liste mit Durchschnittswerten des Leistungsgrads
    mean_ti = []    # Liste mit Durchschnittswerten der Abschnittszeiten
    int_liste_a = []    # Liste mit Integerwerten der einzelnen Abschnitte
    int_liste_z = []    # Liste mit Integerwerten der einzelnen Zyklen
    str_liste = []  # Liste mit den Achs - Beschriftungen
    zyklus_sum = []
    varianz = []
    stdw = []
    mean_t = []
    count = 0
    # csv-Dateien mit Abschnittsdauer und Leistungsgrad auslesen, in Listen speichern und grafisch aufbereiten
    with open(os.path.join(os.path.dirname(__file__), "CSV", "%s", "Abschnittsdauer.csv") % (studie), newline ='') as file:
        csv_file = csv.reader(file, delimiter = ',', quotechar = '"')       # die csv Datei einlesen
        for line in csv_file:           # jede Zeile der Datei durchgehen und die Daten in Listen speichern
            zyklus = 0
            count += 1
            if count == 1:
                for element in line[3:]:
                    int_liste_z.append([])  # Verschachtelte Liste mit einzelnen Zyklen erstellen
            if count > 1:       # den Tabellenkopf, in dem sich keine relevanten Daten befinden, überspringen
                str_liste.append('%s' % line[1])
                for element in line[3:]:                        # [3:] --> ersten zwei Spalten, in denen sich keine Daten befinden, überspringen
                    try:
                        # nur Zahlen zu der Liste hinzufügen, da entfernte Zeiten als 'xxx' und nicht aufgenommene Zyklen als 'None' in der Tabelle auftauchen und für die Berechnung nicht relevant sind
                        int_liste_z[zyklus].append(int(element))
                        int_liste_a.append(int(element))
                        zyklus += 1
                    except:
                        zyklus += 1 
                number_t.append(len(int_liste_a))
                stdw.append(np.array(int_liste_a).std(dtype=np.float64, ddof = 1))        # Standardabweichungen berechnen und zum Array hinzufügen
                varianz.append(np.array(int_liste_a).var(dtype=np.float64, ddof = 1))     # Varianzen berechnen und zum Array hinzufügen
                mean = round(np.array(int_liste_a).mean(), 2)                             # Durchschnittswerte berechnen
                mean_ti.append(mean)
                int_liste_a = []          # die Liste mit den relevanten Daten für jeden Abschnitt zurücksetzen, sodass der Durchschnitt einer Zeile berechnet wird

    for zyklus in int_liste_z:
        if len(zyklus) > 0:
            zyklus_sum.append(np.array(zyklus).sum())       # die Summe der Einzelzeiten eines Zyklus zur Liste hinzufügen

    count = 0
    with open(os.path.join(os.path.dirname(__file__), "CSV", "%s", "Leistungsgrad.csv") % (studie), newline ='') as file:
        csv_file = csv.reader(file, delimiter = ',', quotechar = '"')
        for line in csv_file:
            count += 1
            if count > 1:
                for element in line[3:]:
                    try:
                        int_liste_a.append(int(element))
                    except:
                        continue
                mean = round(np.array(int_liste_a).mean(), 2)
                mean_L.append(mean)
                int_liste_a = []
    count = 0
    
    for x in range(len(mean_L)):
        mean = round(mean_L[x]/100 * mean_ti[x], 1) # Durschnittliche Dauer eines Abschnitts unter Berücksichtigung des Leistungsgrads berechnen
        mean_t.append(mean)                         # Die berechneten Zeitwerte in einer Liste speichern

    # Bar-Chart erstellen
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(str_liste))
    ax.clear()
    ax.barh(y_pos, mean_t, align='center',
        color='blue', ecolor='black')
    for i, v in enumerate(mean_t):
        ax.text(v + 0.2, i + .05, str(v), color='black', fontweight='bold')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(str_liste)
    ax.invert_yaxis()  # oben mit dem ersten Abschnitt beginnen
    ax.set_xlim(0, max(mean_t)+1)
    ax.set_xlabel('Durchschnittliche Dauer in HM (Leistungsgrad, Pausen und andere Zusatzabschnitte berücksichtigt)')
    ax.set_title('Zeitstudie: %s ' % studie + '(Abschnittsdauer)')
    


def auswertung_zyklisch(value):
    soll = value
    mean_tz = np.array(zyklus_sum).mean()
    zyklus_stdw = np.array(zyklus_sum).std(dtype=np.float64, ddof = 1)
    v = round((zyklus_stdw / mean_tz) * 100, 1)
    epsilon = round(1.96 * zyklus_stdw / np.sqrt(len(zyklus_sum)) / mean_tz * 100, 1)
    if epsilon > soll:
        einzelzeiten = round((1.96 * v / soll) ** 2, 0)
    else:
        einzelzeiten = 0
    ergebnis = (epsilon, einzelzeiten)
    return ergebnis


def auswertung_epsilon(studie, value):
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ok = False
    bool_array = []
    v = []
    epsilon = []                # Liste mit den Istwerten der einzelnen Abschnitte
    sollwert = value            # Sollwert Epsilon in %
    count = 0

    for value in stdw:
        v.append(round(value / mean_ti[count] * 100, 2))     # Variationszahlen in %
        count += 1
    count = 0

    for value in stdw:
        epsilon.append(round(1.96 * value / np.sqrt(number_t[count]) / mean_ti[count] * 100, 1))
        count += 1

    for value in epsilon:       # Werte ausfindig machen, die über dem geforderten Grenzwert liegen und für die somit mehr Messungen erforderlich sind
        if value <= sollwert:
            ok = True
        else:
            ok = False
        bool_array.append(ok)
    
    for i, ok in enumerate(bool_array):
        if ok == False:
            value = round((1.96 * v[i] / sollwert) ** 2, 0)
            ax.text(i-0.2, epsilon[i]+0.5 , 'n='+str(value), color='black', fontweight='bold')

    values = np.array(epsilon)
    x = np.arange(len(str_liste))

    # die Werte aufsplitten in den Grenzwert überschreitende und unterschreitende Werte
    above_sollwert = np.maximum(values - sollwert, 0)
    below_sollwert = np.minimum(values, sollwert)

    # den horizontalen Bar-Chart erstellen
    ax.bar(x, below_sollwert, 0.35, color="g") # Werte darunter in grün
    ax.bar(x, above_sollwert, 0.35, color="r", # Werte darüber in rot
            bottom=below_sollwert)

    ax.set_ylabel('Istwert ε in %')
    ax.set_xticks(x)
    ax.set_xticklabels(x+1)
    ax.set_xlabel('Abschnitte (n gibt die Anzahl erforderlicher Einzelzeiten an)')
    ax.set_title('Zeitstudie: %s ' % studie + '(Vertrauensbereich)')
    # Grenzwert durch eine horizontale Linie kennzeichnen
    ax.plot([-0.2, len(str_liste)-0.8], [sollwert, sollwert], "k--")
    plt.show()
    

        