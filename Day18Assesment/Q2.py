from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://letcode.in/frame")

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

driver.find_element(By.NAME, "fname").send_keys("Abhinay")
driver.find_element(By.NAME, "lname").send_keys("reddy")

driver.switch_to.default_content()

parent_window = driver.current_window_handle

driver.execute_script("window.open('https://letcode.in/windows','_blank');")

windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    print("Window title:", driver.title)

for window in windows:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()

driver.switch_to.window(parent_window)
print("Returned to parent window:", driver.title)

driver.quit()
