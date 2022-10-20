from selenium.webdriver.common.by import By
#Links.
URL = 'https://d36ayf7y0dxdzq.cloudfront.net/login'
    
#Page objects.

#Login.
LOGIN_WITH_AUTHO_BTN = (By.XPATH,'//button')

#Sign in google btn.
SIGN_IN_WITH_GOOGLE_BTN = (By.XPATH, '//a[@data-provider]')

#Inputs of the account.
USERNAME_TEXTBOX = (By.XPATH, '//input[@type="email"]')
PASSWORD_TEXTBOX = (By.XPATH, '//input[@type="password"]')

#Inside menu options.
MENU_BUTTON = (By.XPATH, '//button[@type="button"]/span/span')
MYTIMESHEET = (By.XPATH, '//span[text()="My Timesheet "]')

#Timesheet options.
CLIENTDROPDOWNTIMETASK = (By.XPATH, '//select/option[text()="Cecropia Solutions"]')
QAOMBOARDINGTIMETASK = (By.XPATH, '//select/option[text()="QA on Boarding"]')
DEVELOPMENTTIMTASK = (By.XPATH, '//select/option[text()="Development"]')
WORKTYPETIMETASK = (By.XPATH, '//select/option[text()="Qa Developer"]')
DESCRIPTIONTIMETASK = (By.XPATH, '//input[@formcontrolname="description"]')
TIMEINPUTTIMETASK = (By.XPATH, '//input[@formcontrolname="time"]')