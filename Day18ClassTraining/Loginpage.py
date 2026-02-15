from selenium import webdriver
from selenium.webdriver.common.by import By


class loginpage:
    def __init__(self, driver):
        self.driver = driver;

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginbutton = (By.XPATH, "//button[@type='submit']")

    def enterusername(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enterpassword(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def clicklogin(self):
        self.driver.find_element(*self.loginbutton).click()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Day18ClassTraining.Loginpage import loginpage

driver = webdriver.Firefox()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
# time.sleep(5)
loginobj = loginpage(driver)
loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()



