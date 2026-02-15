from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")
wait = WebDriverWait(driver, 10)
assert "Your Store" in driver.title

driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Register").click()

heading = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
).text.strip()

print("Heading:", heading)
assert heading == "Register Account"

driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

warning = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
).text

assert "Privacy Policy" in warning

driver.find_element(By.ID, "input-firstname").send_keys("abhinay")
driver.find_element(By.ID, "input-lastname").send_keys("reddy")
driver.find_element(By.ID, "input-email").send_keys("abhinay066995143@gmail.com")
driver.find_element(By.ID, "input-telephone").send_keys("9876543210")

driver.find_element(By.ID, "input-password").send_keys("wprooo1234")
driver.find_element(By.ID, "input-confirm").send_keys("wprooo1234")

driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
driver.find_element(By.NAME, "agree").click()

driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

success_msg = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/h1"))
).text.strip()

assert success_msg == "Your Account Has Been Created!"

driver.find_element(By.LINK_TEXT, "Continue").click()

driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Order History").click()

print("Lab 5 executed successfully")

driver.quit()