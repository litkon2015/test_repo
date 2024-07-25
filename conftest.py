import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():

    selenoid_options = {
            "enableVNC": True,
            "enableVideo": False,
            "name": "TestProject",
            "sessionTimeout": "2m",
        }

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "126.0")

    options.set_capability("selenoid:options", selenoid_options)

    driver = webdriver.Remote(
        command_executor=f"http://localhost:4444/wd/hub",
        options=options)

    yield driver

    driver.close()
    driver.quit()
