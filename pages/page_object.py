from selenium.webdriver.common.by import By
# Links.
URL = 'https://d36ayf7y0dxdzq.cloudfront.net/login'
    
# Page objects.

# Login.
AUTH0_BTN = (By.XPATH,'//button')

# Sign in google btn.
SIGN_IN_WITH_GOOGLE_BTN = (By.XPATH, '//a[@data-provider]')

# Inputs of the account.
USERNAME_TEXTBOX = (By.XPATH, '//input[@type="email"]')
PASSWORD_TEXTBOX = (By.XPATH, '//input[@type="password"]')

# Inside menu options.
MENU_BUTTON = (By.XPATH, '//button[@type="button"]/span/span')
MY_TIMESHEET_DROPDOWN = (By.XPATH, '//span[text()="My Timesheet "]')

# Timesheet / Timetask options.
CLIENT_DROPDOWN = (By.XPATH, '//select/option[text()="Cecropia Solutions"]')
PROJECT_DROPDOWN = (By.XPATH, '//select/option[text()="QA on Boarding"]')
MODULE_DROPDOWN = (By.XPATH, '//select/option[text()="Development"]')
TASK_DROPDOWN = (By.XPATH, '//select/option[text()="Qa Developer"]')
DESCRIPTION_TEXTBOX = (By.XPATH, '//input[@formcontrolname="description"]')
TIME_TEXTBOX = (By.XPATH, '//input[@formcontrolname="time"]')
ADD_BTN = (By.XPATH, '//button[text()="ADD"]')
DONE_BTN = (By.XPATH, '//button/span[text()="DONE"]')