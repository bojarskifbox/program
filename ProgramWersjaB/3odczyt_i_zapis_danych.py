import pyodbc

connection_path = pyodbc.connect((r'Driver={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};DBQ=C:\Users\Gabriela\Desktop\Moje dokumenty\fil\testdb\zestawienieoperacji.xlsx;'), autocommit = True)
cursor = connection_path.cursor()

for worksheet in cursor.tables():

    print(worksheet)

    tablename = worksheet[2]

cursor.execute("SELECT * FROM [{}]".format(tablename))

for row in cursor:
    print(row)
"""

class Rekord(index, data, kwota, platnik, uzytkownik, tytul wplaty, forma wplaty, numer wyciagu, numer KP, osoba przyjmujaca, uwagi, ostatnia aktualizacja)

funkcja stworz obiekt rekord:
obiekt_rekord1 = from RRRR-MM-DD zestawienie.xlsx select dane
obiekt_rekord1 insert to access testowadb
"""

# -------------------------------------------------
#
# connection_path_2 =  pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Gabriela\Desktop\Moje dokumenty\fil\testdb\testdb2.accdb;')
# cursor2 = connection_path_2.cursor()
#
# cursor2.execute("insert into test11(dane)")
#
# cursor2.execute('select * from test11')
# for row in cursor2.fetchall():
#     print(row)
#
# connection_path_2.commit()