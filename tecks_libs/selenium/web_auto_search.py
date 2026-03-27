from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = FirefoxWebDriver()
print("[INFO] Navigateur Firefox démarré")
driver.get("http://www.python.org")
print(f"[INFO] Page ouverte: {driver.current_url}")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon 2024")
elem.send_keys("zzzqwertyuiopasdfghjkl987654321 2024")
elem.send_keys(Keys.RETURN)
print("[INFO] Recherche envoyée")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
WebDriverWait(driver, 10).until(EC.url_contains("search"))
body_text = driver.find_element(By.TAG_NAME, "body").text.lower()

assert "/search/" in driver.current_url and "q=" in driver.current_url
time.sleep(1)
assert "no results found" in body_text or "did not match" in body_text
print("[OK] Test valide: Page de recherche chargée et aucun résultat trouvé")
driver.close()
print("[INFO] Navigateur fermé")
