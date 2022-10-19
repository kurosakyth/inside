from operator import contains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class inside_login_page:
    #Links.
    URL = 'https://d36ayf7y0dxdzq.cloudfront.net/login'
    
    #Page objects.
    LOGIN_WITH_AUTHO_BTN = (By.XPATH,'//button')
    SIGN_IN_WITH_GOOGLE_BTN = (By.XPATH, '//a[@data-provider]')
    USERNAME_TEXTBOX = (By.XPATH, '//input[@type="email"]')
    PASSWORD_TEXTBOX = (By.XPATH, '//input[@type="password"]')
    MENU_BUTTON = (By.XPATH, '//button[@type="button"]/span/span')
    MYTIMESHEET = (By.XPATH, '//span[text()="My Timesheet "]')
    CLIENTDROPDOWNTIMETASK = (By.XPATH, '//select/option[text()="Cecropia Solutions"]')
    QAOMBOARDINGTIMETASK = (By.XPATH, '//select/option[text()="QA on Boarding"]')
    DEVELOPMENTTIMTASK = (By.XPATH, '//select/option[text()="Development"]')
    WORKTYPETIMETASK = (By.XPATH, '//select/option[text()="Qa Developer"]')
    DESCRIPTIONTIMETASK = (By.XPATH, '//input[@formcontrolname="description"]')
    TIMEINPUTTIMETASK = (By.XPATH, '//input[@formcontrolname="time"]')

    #Constructor.
    def __init__(self, driver):
        self.driver = driver

    #Open the page with the link.
    def load(self):
        self.driver.get(self.URL)     

    #Get the title of the page and return it.
    def get_title(self):
        return self.driver.title

    #Method to click / select a button / option on the page.
    def btn_method_click(self, selector, timeout = 20):
        wait = WebDriverWait(self.driver,timeout)
        btn = wait.until(ec.visibility_of_element_located(selector))
        btn.click()

    #Click or select a button using a specific selector.
    def click_btn(self, option):
        if option == 'AUTHOBTN':
            self.btn_method_click(self.LOGIN_WITH_AUTHO_BTN)
        elif option == 'GOOGLEBTN':
            self.btn_method_click(self.SIGN_IN_WITH_GOOGLE_BTN)
        elif option == 'MENUBTN':
            self.btn_method_click(self.MENU_BUTTON)
        elif option == 'TIMESHEETSPAN':
            self.btn_method_click(self.MYTIMESHEET)
        elif option == 'CLIENTDROPDOWNTIMETASK':
            self.btn_method_click(self.CLIENTDROPDOWNTIMETASK)
        elif option == 'QAOMBOARDINGTIMETASK':
            self.btn_method_click(self.QAOMBOARDINGTIMETASK)
        elif option == 'DEVELOPMENTTIMTASK':
            self.btn_method_click(self.DEVELOPMENTTIMTASK)
        elif option == 'WORKTYPETIMETASK':
            self.btn_method_click(self.WORKTYPETIMETASK)
        else:
            raise Exception('Is not possible to click/select a btn/option.')

    #Method to write on a textbox on the page.
    def textbox_method_write(self, data_from_user, selector, timeout = 20):
        wait = WebDriverWait(self.driver, timeout)
        textbox = wait.until(ec.visibility_of_element_located(selector))
        textbox.send_keys(data_from_user + Keys.RETURN)

    #Write on a textbox using a specific selector by using a method.
    def write_on_textbox(self, data_from_user, option):
        if option == 'USERNAME':
            self.textbox_method_write(data_from_user,self.USERNAME_TEXTBOX)
        elif option == 'PASSWORD':
            self.textbox_method_write(data_from_user,self.PASSWORD_TEXTBOX)
        elif option == 'DESCRIPTION':
            self.textbox_method_write(data_from_user,self.DESCRIPTIONTIMETASK)
        elif option == 'TIMEINPUTTIMETASK':
            self.textbox_method_write(data_from_user,self.TIMEINPUTTIMETASK)
        else:
            raise Exception('Is not possible to write on the textbox.')

    #Method to find the texbox on the page.
    def textbox_method_get_text(self,*selector):
        textbox = self.driver.find_element(*selector)
        textbox = textbox.get_attribute("value")
        return textbox

    #Check the web object and get the attribute 'value'.
    def get_text_from_textbox(self,option):
        if 'USERNAME' == option:
            textbox_value = self.textbox_method_get_text(*self.USERNAME_TEXTBOX)
            return textbox_value
        elif 'DESCRIPTION' == option:
            textbox_value = self.textbox_method_get_text(*self.DESCRIPTIONTIMETASK)
            return textbox_value
        elif 'TIMEINPUTTIMETASK' == option:
            textbox_value = self.textbox_method_get_text(*self.TIMEINPUTTIMETASK)
            return textbox_value
        else:
            raise Exception('Is not possible to get the text from the textbox.')