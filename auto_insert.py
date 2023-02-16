import datetime
import pyodbc
import logging

def inserting():
    logging.info("start")

    dzisiejsza_data_nazwa = datetime.date.today()
    wczorajsza_data_nazwa = dzisiejsza_data_nazwa - datetime.timedelta(days=1)
    nazwa_sortujaca = str(wczorajsza_data_nazwa) + " zestawienie" + ".xlsx"

    connection_path = pyodbc.connect((r'Driver={{Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)}};'
                                      r'DBQ=C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\posortowane\\{0}'
                                      .format(nazwa_sortujaca)), autocommit = True)

    logging.info("polaczono z plikiem xlsx")

    cursor = connection_path.cursor()

    for worksheet in cursor.tables():
        print(worksheet)
        tablename = worksheet[2]

    cursor.execute("SELECT [Data transakcji], Kwota, [Nadawca / odbiorca], Opis FROM [{}]".format(tablename))

    logging.info("pobrano dane z zestawienia xlsx")

    koldata = []
    kolkwota = []
    koluser = []
    kolopis = []
    pobrane_rekordy = [koldata, kolkwota, koluser, kolopis]

    logging.info("utworzono tabele z rekordami")

    for row in cursor:
        koldata.append(str(row[0]))
        kolkwota.append(str(row[1]))
        koluser.append(str(row[2]))
        kolopis.append(str(row[3]))

    logging.info("dodano dane do tabeli")

    x = 0

    # zapis do access

    connection_path_2 =  pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Gabriela\Desktop\Moje dokumenty\fil\testdb\testowaDB.accdb;')
    cursor2 = connection_path_2.cursor()

    logging.info("polaczono z baza danych access")

    rekordx = 0
    for rekord in range(len(koldata)):
        cursor2.execute("INSERT INTO tbWplaty (fldDataWplaty, fldKwota, fldUser, fldTytulWplaty) VALUES (?, ?, ?, ?)",
            (koldata[rekordx], float(kolkwota[rekordx]), koluser[rekordx], kolopis[rekordx]))
        rekordx += 1

    logging.info("dodano rekordy do tabeli w access")

    connection_path_2.commit()

    logging.info("dodano rekordy w ilosci:" + str(rekordx))
    logging.info("DZIAŁANIE PROGRAMU ZAKOŃCZONE")