from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.find_element(By.NAME, "my-text").send_keys("Abhinay")
driver.find_element(By.NAME, "my-password").send_keys("Wipro@123")

driver.find_element(By.ID, "my-radio-2").click()

driver.find_element(By.ID, "my-check-2").click()

dropdown = Select(driver.find_element(By.NAME, "my-select"))
dropdown.select_by_visible_text("Two")

time.sleep(1)

driver.find_element(By.TAG_NAME, "button").click()

confirmation = wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
).text

print("Confirmation Message:", confirmation)
assert "Received!" in confirmation

print("Form submitted successfully")

driver.quit()
