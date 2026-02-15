import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDay16q1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_day16q1(self):
        self.driver.get("https://tutorialsninja.com/demo/")
        time.sleep(5)
        self.driver.set_window_size(1552, 832)
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("abhinay")
        time.sleep(5)
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys("reddy")
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "form-control").click()
        self.driver.find_element(By.ID, "input-email").send_keys("abhi139912@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "input-telephone").send_keys("1451451450")
        self.driver.find_element(By.CSS_SELECTOR, "input#input-password").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#input-password").send_keys("1234567")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[contains(@name,'confirm')]").click()
        self.driver.find_element(By.XPATH, "//input[contains(@name,'confirm')]").send_keys("1234567")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[contains(@value,'1')][contains(@name,'newsletter')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[contains(@value,'1')][contains(@name,'agree')]").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(10)
        msg='Your Account Has Been Created!'
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(msg)
        time.sleep(5)
        self.driver.close()