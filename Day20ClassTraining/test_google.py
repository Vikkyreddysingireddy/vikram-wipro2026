import pytest
from driverfactory import getdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_googletitle(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com")

    WebDriverWait(driver, 10).until(
        EC.title_contains("Google")
    )

    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_search(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium grid")
    search_box.submit()

    WebDriverWait(driver, 15).until(
        EC.url_contains("selenium+grid")
    )

    assert "selenium" in driver.current_url.lower()
    driver.quit()
