import datetime
import os
import logging
import time

def renaming():
    logging.info("sortowanie pliku wedlug daty:")

    dzisiejsza_data_nazwa = datetime.date.today()
    wczorajsza_data_nazwa = dzisiejsza_data_nazwa - datetime.timedelta(days=1)
    nazwa_sortujaca = str(wczorajsza_data_nazwa) + " zestawienie" + ".xlsx"

    czy_pobrano = os.path.exists(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\Zestawienie operacji.xlsx")

    logging.info("pobrany plik znajduje sie w folderze")

    if czy_pobrano is True:
        os.rename(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\Zestawienie operacji.xlsx",
              r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\posortowane\\" + nazwa_sortujaca)
    else:
        logging.info("pobrany plik nie moze byc zmieniony")

    czy_zmiana_nazwy_ok = os.path.exists(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\posortowane\\" + nazwa_sortujaca)
    logging.info("zmiana nazwy i sortowanie powiodlo sie")

    time.sleep(2)

