from operator import contains
from pages.actions import inside_login_page
import pages.page_object as page_object
import credentials
import time

def test_prueba(browser):

    # Using the fixture configuration run the browser.
    inside = inside_login_page(browser)

    # Open the browser with the page.
    inside.load_page()

    # Check the title of the page is the expected.
    assert 'PortalWeb' == inside.get_title_of_the_page()

    # Click the auth0 button.
    inside.click_btn(page_object.AUTH0_BTN)

    # Check the title of the page is the expected.
    assert 'Sign In with Auth0' == inside.get_title_of_the_page()

    # Click on the Sign with Google button.
    inside.click_btn(page_object.SIGN_IN_WITH_GOOGLE_BTN)

    # Check the title of the browser if contains the title "Cuentas de google" on it.
    assert inside.get_title_of_the_page().__contains__('Cuentas de Google') == True or inside.get_title_of_the_page().__contains__('cuentas de Google') == True

    # Write on the username textbox using the username of the file.
    inside.write_on_textbox(credentials.username,page_object.USERNAME_TEXTBOX)

    # Check that the username on the file is the one wrote.
    assert credentials.username == inside.get_text_from(*page_object.USERNAME_TEXTBOX)

    # Write on the username textbox using the username of the file.
    inside.write_on_textbox(credentials.password,page_object.PASSWORD_TEXTBOX)

    # Click the top left Menu button.
    inside.click_btn(page_object.MENU_BUTTON)

    # Click the Timesheet option of the menu.
    inside.click_btn(page_object.MY_TIMESHEET_DROPDOWN)

    # Click the Timesheet option of the client dropdown.
    inside.click_btn(page_object.CLIENT_DROPDOWN)
    
    # Click the Timesheet option of the project dropdown.
    inside.click_btn(page_object.PROJECT_DROPDOWN)

    # Click the Timesheet option of the module dropdown.
    inside.click_btn(page_object.MODULE_DROPDOWN)

    # Click the Timesheet option of the worktype dropdown.
    inside.click_btn(page_object.TASK_DROPDOWN)

    # Write on Description of the Timesheet textbox.
    inside.write_on_textbox('Description information test.',page_object.DESCRIPTION_TEXTBOX)

    # Check that the username on the file is the one wrote.
    assert "Description information test." == inside.get_text_from(*page_object.DESCRIPTION_TEXTBOX)

    # Write on Description of the Timesheet textbox. writes 04 in this case (example).
    inside.write_on_textbox('4',page_object.TIME_TEXTBOX)

    # Check that the username on the file is the one wrote. 04 in this case (example).
    assert "04" == inside.get_text_from(*page_object.TIME_TEXTBOX)

    # Delete this timer
    #time.sleep(10)

    #agregar asserts nuevos.