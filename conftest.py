
import pytest
import logging
from my_project.gui.webdriver.setup import BaseDriver

LOGGER = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge", help="Browser to use for the UI tests")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    browser = BaseDriver()
    driver = browser.initiate_browser(browser_name)
    yield driver
    driver.quit()
