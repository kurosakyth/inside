import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set browser options to make it headless.
option = Options()
option.headless = True

# fixture where is set the chrome driver as default, implicit wait to 10, to return the driver and quit.
@pytest.fixture
def browser():
    driver = webdriver.Chrome(options= option)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()