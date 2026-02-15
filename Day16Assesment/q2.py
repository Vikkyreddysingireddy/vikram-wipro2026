from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://tutorialsninja.com/demo/")
print("Home Page Title:", driver.title)
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Desktops").click()
driver.find_element(By.LINK_TEXT, "Mac (1)").click()
print("Mac Page Title:", driver.title)
time.sleep(3)

driver.back()
print("After Back:", driver.title)
time.sleep(3)

driver.forward()
print("After Forward:", driver.title)
time.sleep(3)

driver.refresh()
print("After Refresh:", driver.title)
time.sleep(2)
driver.quit()
