class inside_login_page:
    URL = 'https://d36ayf7y0dxdzq.cloudfront.net/login'
    #LOGIN_WITH_AUTHO_BTN = "//*[contains(text(), ' Login with Auth0 ')]"
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)      

    def get_title(self):
        return self.driver.title