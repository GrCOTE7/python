import flet as ft
import unittest

import sys

sys.dont_write_bytecode = True

import div.tests.WebsitesSanityChecks as WebsitesSanityChecks
import div.tests.Calc as Calc


def autologin():
    user = "User"
    password = "123456"

    url = "http://www.stealmylogin.com/demo.html"

    driver = webdriver.Chrome
    # ("C:\\Users\\utilisateur\\Downloads\\chromedriver_win32")
    # driver.get('https://www.facebook.com/login.php')

    # print("Ok")


def run_tests():
    suite1 = unittest.defaultTestLoader.loadTestsFromModule(WebsitesSanityChecks)
    suite2 = unittest.defaultTestLoader.loadTestsFromModule(Calc)

    combined_suite = unittest.TestSuite([suite1, suite2])

    runner = unittest.TextTestRunner()

    # print("Je vais tester les accès à 2 sites...\n")
    runner.run(combined_suite)


def main():
    # Lancement de testos..
    run_tests()
    pass


if __name__ == "__main__":

    main()
    print("-" * 100, "FIN", "-" * 14)
