from pages.actions import action_class
import pages.page_object as page_object
import credentials

def test_login(browser):
    # Using the fixture configuration run the browser.
    inside = action_class(browser)

    # Open the browser with the page.
    inside.load_page(page_object.URL)

    # Check the title of the page is the expected.
    assert inside.get_title_of_the_page().__contains__('PortalWeb') == True

    # Click the auth0 button.
    inside.click_btn(page_object.AUTH0_BTN)

    # Check the title of the page is the expected.
    assert inside.get_title_of_the_page().__contains__('Sign In with Auth0') == True

    # Click on the Sign with Google button.
    inside.click_btn(page_object.SIGN_IN_WITH_GOOGLE_BTN)

    # Check the title of the browser if contains the title "Cuentas de google" on it.
    assert inside.get_title_of_the_page().__contains__('Cuentas de Google') == True or inside.get_title_of_the_page().__contains__('cuentas de Google') == True

    # Write on the username textbox using the username of the file.
    inside.write_on_textbox(credentials.username,page_object.USERNAME_TEXTBOX)

    # Write on the username textbox using the username of the file.
    inside.write_on_textbox(credentials.password,page_object.PASSWORD_TEXTBOX)

    # Check the welcome message on the home inside page.
    assert inside.get_text(page_object.WELCOME_MSG).__contains__('Welcome') == True