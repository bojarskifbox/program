"""
1. automatyczne uruchomienie programu przez harmonogram zadań windows
2. logowanie, pobranie pliku
3. sortowanie pliku(zmiana nazwy), sprawdzenie
4. odczyt danych z pliku xlsx, zapis danych w odpowiedniej formie do tabeli pośredniej access,
5. zatwierdzanie wpisów automatyczne i reczne do bazy, sprawdzanie okresowe
"""

import time

import auto_import

start_import = auto_import.ClickAndSendKeys()
start_import.test()

import auto_rename

auto_rename.renaming()


import auto_insert

auto_insert.inserting()

print("koniec")
time.sleep(5)