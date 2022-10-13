from selenium.webdriver.common.by import By
class inside_login_page:
    URL = 'https://d36ayf7y0dxdzq.cloudfront.net/login'
    LOGIN_WITH_AUTHO_BTN = (By.XPATH,'/html/body/app-root/div/ui-view/app-login/div/div/div[1]/div[2]/button')
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)      

    def get_title(self):
        return self.driver.title

    def click_autho_button(self):
        btn = self.driver.find_element(*self.LOGIN_WITH_AUTHO_BTN)
        btn.click()