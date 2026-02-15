import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GRID_URL = "http://localhost:4444/wd/hub"

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_grid_execution(browser):

    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.get("https://www.google.com")

    WebDriverWait(driver, 10).until(
        EC.title_contains("Google")
    )

    assert "Google" in driver.title
    caps = driver.capabilities
    print(f"\nBrowser: {caps.get('browserName')} | Platform: {caps.get('platformName')}")

    driver.quit()
