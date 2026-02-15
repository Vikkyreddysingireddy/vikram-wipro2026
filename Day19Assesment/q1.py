from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Edge()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://tutorialsninja.com/demo/")
print("Page opened with Implicit Wait applied.")

wait = WebDriverWait(driver, 15)

search_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "search"))
)

print("Explicit Wait: Search box is clickable!")
search_box.send_keys("iPhone")

fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,
    ignored_exceptions=[NoSuchElementException]
)

search_button = fluent_wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#search button"))
)

print("Fluent Wait: Search button is visible now!")

search_button.click()

results = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "content"))
)

if results.is_displayed():
    print("Search performed successfully!")

time.sleep(5)
driver.quit()
