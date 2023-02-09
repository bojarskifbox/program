import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

import os

x = ["pass"]

class ClickAndSendKeys():

    def test(self):
        base_url = "https://goonline.bnpparibas.pl/#!/login"
        driver = webdriver.Chrome()

        op = webdriver.ChromeOptions();
        p = {"download.default_directory": r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane"};
        op.add_experimental_option("prefs", p);
        driver = webdriver.Chrome(options=op);

        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(15)

        login_field = driver.find_element(By.XPATH, "//input[@data-test-id='username-input']")
        login_field.send_keys("login")
        time.sleep(3)

        dalej_button = driver.find_element(By.XPATH, "//button[@data-test-id='submit-button']")
        dalej_button.click()
        time.sleep(3)

        try:
            password_field = driver.find_element(By. XPATH, "//input[@data-test-id='password-input']")
            password_field.send_keys("".join(x))
            time.sleep(1)

        except:
            time.sleep(1)

            try:
                for a in range(1, 11):
                    password_fields = driver.find_element(By.XPATH, "//input[@placeholder='" + str(a) + "']")
                    enable = password_fields.is_enabled()
                    if enable is True:
                        password_fields.send_keys(x[a - 1])
                        time.sleep(1)
                    else:
                        time.sleep(1)
            except:
                time.sleep(1)

        dalej_button = driver.find_element(By.XPATH, "//button[@data-test-id='submit-button']")
        dalej_button.click()
        time.sleep(3)


        try:
            sms_field = driver.find_element(By. XPATH, "//input[@id='smsCode']")
            sms_field
            time.sleep(30)

            sms_dalej_button = driver.find_element(By. XPATH, "//button[@data-test-id='submit-button']")
            sms_dalej_button.click()
            time.sleep(3)
        except:
            time.sleep(1)

        wybierz_konto = driver.find_element(By. XPATH, "//div[@data-test-id='profile-box'] ")
        wybierz_profil = driver.find_element(By. XPATH, "//span[@title='Profil pełnomocnictwa']")
        try:
            actions = ActionChains(driver)
            actions.move_to_element(wybierz_konto).click().perform()
            time.sleep(2)

            actions.move_to_element(wybierz_profil).click().perform()
            time.sleep(10)

        except:
            time.sleep(1)

        historia = driver.find_element(By. XPATH, "//a[@data-test-id='main-nav-history']")
        historia.click()
        time.sleep(5)

        try:
            actions = ActionChains(driver)
            wybierz_date = driver.find_element(By. XPATH, "//div[@role='combobox']")
            actions.move_to_element(wybierz_date).click().perform()
            time.sleep(2)

            zakres_dat = driver.find_elements(By. CLASS_NAME, "ng-option")
            zakres_dat[3].click()
            time.sleep(5)

        except:
            time.sleep(1)


        wczorajsza_data_do_formatu = datetime.date.today() -datetime.timedelta(days=1)
        wczorajsza_data = wczorajsza_data_do_formatu.strftime("%d.%m.%Y")

        data_od = driver.find_element(By. XPATH, "//bnp-ui-datepicker//input[@type='text']")
        data_od.clear()
        time.sleep(2)
        data_od.send_keys(wczorajsza_data)
        time.sleep(2)

        data_do = driver.find_element(By. XPATH, "//bnp-ui-datepicker//input[@class='ng-untouched ng-pristine ng-valid']")
        data_do.clear()
        time.sleep(2)
        data_do.send_keys(wczorajsza_data)
        time.sleep(2)

        filtry_link = driver.find_element(By.XPATH, "//a[@data-test-id='toggle-more-filters']")
        uznania_link = "//label[@for='checkbox-group-1-0']"
        pobieranie_link = "//a[@data-test-id='download-history-link']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(filtry_link).click().perform()
            time.sleep(2)

            uznania = driver.find_element(By. XPATH, uznania_link)
            actions.move_to_element(uznania).click().perform()
            time.sleep(2)

            pobieranie = driver.find_element(By.XPATH, pobieranie_link)
            actions.move_to_element(pobieranie).click().perform()
            time.sleep(15)
        except:
            time.sleep(1)

        wyloguj = driver.find_element(By. XPATH, "//a[@data-test-id='logout']")
        wyloguj.click()
        time.sleep(5)
        driver.quit()

start = ClickAndSendKeys()
start.test()

dzisiejsza_data_nazwa = datetime.date.today()
wczorajsza_data_nazwa = dzisiejsza_data_nazwa - datetime.timedelta(days=1)
nazwa_sortujaca = str(wczorajsza_data_nazwa) + " zestawienie" + ".xlsx"

czy_pobrano = os.path.exists(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\Zestawienie operacji.xlsx")
print("czy pobrano " + str(czy_pobrano))

if czy_pobrano is True:
    os.rename(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\Zestawienie operacji.xlsx",
          r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\posortowane\\" + nazwa_sortujaca)
else:
    print("blad pobierania, probuje pobrac ponownie")

czy_zmiana_nazwy_ok = os.path.exists(r"C:\Users\Gabriela\Desktop\Moje dokumenty\fil\selpobrane\posortowane\\" + nazwa_sortujaca)
print("zmiana nazwy " + str(czy_zmiana_nazwy_ok))