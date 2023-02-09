"""

1. AUTOMATYCZNE URUCHAMIANIE PROGRAMU O JAKIEJS GODZINIE:
harmonogram zadań systemu windows

2. LOGOWANIE:
transakcje odrzucone - czy oznaczyć?

jak nie ma w danym dniu zadnej transakcji -> sciaga plik w ktorym sa tylko nazwy kolumn a nie ma rekordow

3. ODCZYT I ZAPIS DANYCH:
utworzenie obiektu z danych z pliku xlsx
jeden wpis bankowy to moze byc jeden lub kilka rekordów ktore trzeba rozszyc

4. ZATWIERDZANIE WPISÓW:
REGEXY do rozpoznawania danych
w formie aplikacji okienkowej
niezatwierdzone zapamietane do zatwierdzenia

sprawdzanie co miesiac poprawnosci dzialania programu przez porownanie danych

-mozliwosc cofania zle zapisanych rekordow

-w bazie plus wysylka alertu
"""
import datetime

x = datetime.date.today()
xx = x - datetime.timedelta(days=1)
xxx2 = str(xx) + ".xlsx"
# xxx = xx.strftime("%d.%m.%Y")
#
# print(x)
# print(xx)
# print(xxx)
#
# wczorajsza_data_do_formatu = datetime.date.today() -datetime.timedelta(days=1)
# wczorajsza_data = wczorajsza_data_do_formatu.strftime("%d.%m.%Y")
#
# print(wczorajsza_data)
# print(wczorajsza_data_do_formatu)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



base_url = "https://www.google.com/"
driver = webdriver.Chrome()
# op = webdriver.ChromeOptions();
# p = {"download.default_directory": r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane"};
# op.add_experimental_option("prefs", p);
# driver = webdriver.Chrome(options=op);
#
driver.maximize_window()
driver.get(base_url)


klucz = input("podaj kod")

x1 = driver.find_element(By. XPATH, "//input[@title='Szukaj']")
time.sleep(15)
x1.send_keys(klucz)
time.sleep(5)

driver.find_element()
x1.
#
# x=driver.find_element(By. XPATH, "//a[@href='https://www.rarlab.com/rar/winrar-x32-611pl.exe']")
# x.click()
# time.sleep(10)

# import os
#
# x2=os.path.exists(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\Zestawienie operacji.xlsx")
# print(x2)
#
# os.rename(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\Zestawienie operacji.xlsx",
#           r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\posortowane\\" + xxx2)


import re

wzor = "Jn Kowalski"
x = "Jan Kowalski"

for index, value in enumerate(wzor):
    print('{} - {}'.format(index, value))

for index, value in enumerate(x):
    print('{} - {}'.format(index, value))

# tes = re.findall("J[an kowalsk]i")
# one = re.sub(wzor, x, x)
# print(one)

# ind = -1
# wz = len(wzor)
# xxa = len(x)
#
# print(wz)
# print(xxa)
# if wz == xxa:
#     print("rowne")
# else:
#     print("g")