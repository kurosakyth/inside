import pytest
from selenium import webdriver
#fixture where is set the chrome driver as default, implicit wait to 10, to return the driver and quit.
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()