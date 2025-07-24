import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


class WebsitesSanityChecks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_example_com_is_accessible(self):
        driver = self.driver
        driver.get("http://www.example.com")
        time.sleep(1)
        # Test : la page contient le mot "Example Domain"
        self.assertIn("Example Domain", driver.page_source)

    def test_search_in_python_org(self):
        siteUrl = "http://www.python.org"
        driver = self.driver
        driver.get(siteUrl)
        self.assertIn("Python", driver.title)
        time.sleep(1)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        # time.sleep(7)
        self.assertNotIn("No results found.", driver.page_source)
        # print("\nJe teste " + siteUrl)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":

    unittest.main()
