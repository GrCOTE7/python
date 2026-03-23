from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


class autoLogin:

    def login():

        # //2do À finir: Idently - AutoLogin - https://www.youtube.com/watch?v=doPo9q6on6c

        username = "User"
        password = "123456"

        driver = webdriver.Firefox()
        # driver = webdriver.Chrome

        url = "http://www.stealmylogin.com/demo.html"
        driver.get(url)
        time.sleep(2)

        nameElt = driver.find_element(By.NAME, "username")
        nameElt.send_keys(username)

        pwElt = driver.find_element(By.NAME, "password")
        pwElt.send_keys(password)

        print("Username and Password sent !")
        # btnElt = driver.find_element(By.ID, "submit")
        btnElt = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        texteBouton = btnElt.get_attribute("value")
        print('Texte du bouton:',texteBouton)

        print(btnElt)
        time.sleep(7)

        btnElt.click()

        time.sleep(7)

        driver.quit()


if __name__ == "__main__":

    autoLogin.login()
