from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    #Click on Auth0 or Google button.
    def click_btn(self, option):
        if option == 'AUTHOBTN':
            btn = self.driver.find_element(*self.LOGIN_WITH_AUTHO_BTN)
            btn.click()
        elif option == 'GOOGLEBTN':
            btn = self.driver.find_element(*self.SIGN_IN_WITH_GOOGLE_BTN)
            btn.click()
        elif option == 'MENUBTN':
            btn = self.driver.find_element(*self.MENU_BUTTON)
            btn.click()
        elif option == 'TIMESHEETSPAN':
            btn = self.driver.find_element(*self.MYTIMESHEET)
            btn.click()
        elif option == 'CLIENTDROPDOWNTIMETASK':
            btn = self.driver.find_element(*self.CLIENTDROPDOWNTIMETASK)
            btn.click()


    #Write on the textbox if the option is USERNAME, write the uername, else the password.
    def write_on_textbox(self, data_from_user, option):
        if option == 'USERNAME':
            textbox = self.driver.find_element(*self.USERNAME_TEXTBOX)
            textbox.send_keys(data_from_user + Keys.RETURN)
        elif option == 'PASSWORD':
            textbox = self.driver.find_element(*self.PASSWORD_TEXTBOX)
            textbox.send_keys(data_from_user + Keys.RETURN)

    #Check the web object and get the attribute 'value'.
    def get_text_from_textbox(self,option):
            textbox = self.driver.find_element(*self.USERNAME_TEXTBOX)
            textbox = textbox.get_attribute("value")
            return textbox
