from ast import Pass
from selenium.webdriver.common.by import By

class inside_login_page:
    #Links.
    URL = 'https://d36ayf7y0dxdzq.cloudfront.net/login'
    
    #Page objects.
    LOGIN_WITH_AUTHO_BTN = (By.XPATH,'/html/body/app-root/div/ui-view/app-login/div/div/div[1]/div[2]/button')
    SIGN_IN_WITH_GOOGLE_BTN = (By.XPATH, '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div/div[1]/a')
    
    #Constructor.
    def __init__(self, driver):
        self.driver = driver
    #Open the page with the link.
    def load(self):
        self.driver.get(self.URL)      
    #Get the title of the page and return it.
    def get_title(self):
        return self.driver.title
    #Click on Auth0 button.
    def click_autho_button(self):
        btn = self.driver.find_element(*self.LOGIN_WITH_AUTHO_BTN)
        btn.click()
    #Click on Sign in with google button.
    def click_sign_with_google_btn(self):
        btn = self.driver.find_element(*self.SIGN_IN_WITH_GOOGLE_BTN)
        btn.click()
    
    #se puede crear un file nuevo donde mantenga los métodos repetidos
    #y más usados del driver para solo importarlos y pasarles el selector.