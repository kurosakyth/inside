from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class inside_login_page:
    #Links.
    URL = 'https://d36ayf7y0dxdzq.cloudfront.net/login'
    
    #Page objects.
    LOGIN_WITH_AUTHO_BTN = (By.XPATH,'/html/body/app-root/div/ui-view/app-login/div/div/div[1]/div[2]/button')
    SIGN_IN_WITH_GOOGLE_BTN = (By.XPATH, '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div/div[1]/a')
    USERNAME_TEXTBOX = (By.XPATH, '//*[@id="identifierId"]')
    PASSWORD_TEXTBOX = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    MENU_BUTTON = (By.XPATH, '/html/body/app-root/div/ui-view/app-main/div/ng-sidebar-container/div/div/div/app-header/div/div[1]/button')
    MYTIMESHEET = (By.XPATH, '/html/body/app-root/div/ui-view/app-main/div/ng-sidebar-container/ng-sidebar/aside/app-navbar/div/div[2]/div/app-navbar-item[10]/a/div/div[1]')
    CLIENTDROPDOWNTIMETASK = (By.XPATH, '/html/body/app-root/div/ui-view/app-main/div/ng-sidebar-container/div/div/div/div/ui-view/app-timesheet-personal-time/app-timesheet-personal-add/div/div[1]/form/select[1]/option[2]')

    #Constructor.
    def __init__(self, driver):
        self.driver = driver

    #Open the page with the link.
    def load(self):
        self.driver.get(self.URL)     

    #Get the title of the page and return it.
    def get_title(self):
        return self.driver.title

    #Method to click / select a button option.
    def btn_method(self, selector, timeout = 20):
        wait = WebDriverWait(self.driver,timeout)
        btn = wait.until(ec.visibility_of_element_located(selector))
        btn.click()

    #Click or select a button using a specific selector.
    def click_btn(self, option):
        if option == 'AUTHOBTN':
            self.btn_method(self.LOGIN_WITH_AUTHO_BTN)
        elif option == 'GOOGLEBTN':
            self.btn_method(self.SIGN_IN_WITH_GOOGLE_BTN)
        elif option == 'MENUBTN':
            self.btn_method(self.MENU_BUTTON)
        elif option == 'TIMESHEETSPAN':
            self.btn_method(self.MYTIMESHEET)
        elif option == 'CLIENTDROPDOWNTIMETASK':
            self.btn_method(self.CLIENTDROPDOWNTIMETASK)

    #Method to write on a textbox.
    def textbotx_method(self, data_from_user, selector, timeout = 20):
        wait = WebDriverWait(self.driver, timeout)
        textbox = wait.until(ec.visibility_of_element_located(selector))
        textbox.send_keys(data_from_user + Keys.RETURN)
        pass

    #Write on a textbox using a specific selector by using a method.
    def write_on_textbox(self, data_from_user, option):
        if option == 'USERNAME':
            self.write_on_textbox_method(data_from_user,self.USERNAME_TEXTBOX)
        elif option == 'PASSWORD':
            self.write_on_textbox_method(data_from_user,self.PASSWORD_TEXTBOX)

    #Check the web object and get the attribute 'value'.
    def get_text_from_textbox(self,option):
        if 'USERNAME' == option:
            textbox = self.driver.find_element(*self.USERNAME_TEXTBOX)
            textbox = textbox.get_attribute("value")
            return textbox
