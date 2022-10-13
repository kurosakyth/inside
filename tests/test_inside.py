from pages.login import inside_login_page

def test_prueba(browser):

    #Using the fixture configuration run the browser.
    inside = inside_login_page(browser)

    #Open the browser with the page.
    inside.load()

    #Check the title of the page is the expected.
    assert 'PortalWeb' == inside.get_title()

    #Click the auth0 button.
    inside.click_autho_button()

    #Check the title of the page is the expected.
    assert 'Sign In with Auth0' == inside.get_title()

    #Click on the Sign with Google button.
    inside.click_sign_with_google_btn()

    #Check the title of the page is the expected.
    assert 'Inicia sesión: Cuentas de Google' == inside.get_title()