from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

slowo = input("podaj slowo: ")
lista_slow = []
lista_slow_uzytych = []


def silnia(n): return n*silnia(n-1) if n > 1 else 1


for i in range(silnia(len(slowo))):
    while slowo in lista_slow_uzytych:
        slowo = list(slowo)
        random.shuffle(slowo)
        slowo = "".join(random.sample(slowo, len(slowo)))
    lista_slow_uzytych.append(slowo)
    driver.get(
        "https://pl.wiktionary.org/wiki/Wikis%C5%82ownik:Strona_g%C5%82%C3%B3wna")
    driver.find_element(By.ID, "bodySearchInput0.309126385828").click()
    webdriver.ActionChains(driver).send_keys(slowo).perform()
    webdriver.ActionChains(driver).key_down(Keys.ENTER).perform()
    try:
        if driver.find_element(By.CLASS_NAME, "text-pl") != []:
            lista_slow.append(slowo)
    except Exception:
        pass
for i in range(len(lista_slow)):
    print(lista_slow[i])
