from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os, time
import unittest

def extract01():
    """Simple search"""
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    # elem.clear()
    elem.send_keys("pycon 2024")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    time.sleep(3)
    driver.close()
    print("Request finish")

def facebook():
    driver = webdriver.Firefox()
    driver.get("http://www.facebook.com")
    assert "Facebook" in driver.title
    elem = driver.find_element(By.NAME, "email")
    elem.send_keys("loginEmail")
    elem = driver.find_element(By.NAME, "pass")
    elem.send_keys("password")
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
    driver.close()
    print("Request finish")


if __name__ == "__main__":
    extract01()
    # unittest.main(module="test_python_org_search", argv=["ignored"], exit=False)
    # facebook()
    # pass

