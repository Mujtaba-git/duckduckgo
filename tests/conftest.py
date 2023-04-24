import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")

# Parameterize the driver fixture with both browsers
@pytest.fixture(scope="session", params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={"browserName": "chrome"},
            options=options,
        )
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={"browserName": "firefox"},
            options=options,
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
