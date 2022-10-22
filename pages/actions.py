from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import pages.page_object as page_object

class inside_login_page:

    # Constructor.
    def __init__(self, driver):
        self.driver = driver

    # Open the page with the link.
    def load_page(self):
        self.driver.get(page_object.URL)   

    # Get the title of the page and return it.
    def get_title_of_the_page(self):
        return self.driver.title

    # Method to click / select a button / option on the page.
    def click_btn(self, selector, timeout = 30):
        wait = WebDriverWait(self.driver,timeout)
        btn = wait.until(ec.visibility_of_element_located(selector))
        btn.click()

    # Method to write on a textbox on the page.
    def write_on_textbox(self, data_from_user, selector, timeout = 30):
        wait = WebDriverWait(self.driver, timeout)
        textbox = wait.until(ec.visibility_of_element_located(selector))
        textbox.send_keys(data_from_user + Keys.RETURN)

    # Method to find the texbox on the page.
    def get_text_from_textbox(self,selector, timeout = 30):
        wait = WebDriverWait(self.driver, timeout)
        textbox = wait.until(ec.visibility_of_element_located(selector))
        textbox = textbox.get_attribute('value')
        return textbox

    # Method to get text. Used to get the alert on the timesheet.
    def get_text(self,*selector, timeout = 30):
        wait = WebDriverWait(self.driver, timeout)
        obj = wait.until(ec.visibility_of_element_located(*selector))
        obj = obj.text
        return obj