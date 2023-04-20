import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")

    # Replace the existing driver setup in conftest.py with the following
    if browser == "chrome":
        options = ChromeOptions()
        #options.headless = True
        options.add_argument('--headless')
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={"browserName": "chrome"},
            options=options,
        )
    elif browser == "firefox":
        options = FirefoxOptions()
        #options.headless = True
        options.add_argument('--headless')
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
