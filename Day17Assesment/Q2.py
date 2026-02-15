from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://letcode.in/alert")
time.sleep(3)

driver.find_element(By.ID, "accept").click()

alert = driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()
time.sleep(2)

driver.find_element(By.ID, "confirm").click()
confirm_alert = driver.switch_to.alert
print("Confirm Message:", confirm_alert.text)
confirm_alert.dismiss()
time.sleep(2)

driver.find_element(By.ID, "prompt").click()
prompt_alert = driver.switch_to.alert
print("Prompt Message:", prompt_alert.text)
prompt_alert.send_keys("Abhinay")
prompt_alert.accept()
time.sleep(2)

result = driver.find_element(By.ID, "myName").text
print("Result on Page:", result)
assert "Abhinay" in result

print("JavaScript Alerts handled successfully")

driver.quit()
