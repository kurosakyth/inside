from pages.login import inside_login_page
import user
import time

def test_prueba(browser):

    #Using the fixture configuration run the browser.
    inside = inside_login_page(browser)

    #Open the browser with the page.
    inside.load()

    #Check the title of the page is the expected.
    assert 'PortalWeb' == inside.get_title()

    #Click the auth0 button.
    inside.click_btn('AUTHOBTN')

    #Check the title of the page is the expected.
    assert 'Sign In with Auth0' == inside.get_title()

    #Click on the Sign with Google button.
    inside.click_btn('GOOGLEBTN')

                    #Check the title of the page is the expected for WINDOWS.
    assert 'Inicia sesión: Cuentas de Google' == inside.get_title()
                    #Check the title of the page is the expected for MAC.
    #assert 'Acceso: Cuentas de Google' == inside.get_title()

    #Write on the username textbox using the username of the file.
    inside.write_on_textbox(user.username,'USERNAME')

    #Check that the username on the file is the one wrote.
    assert user.username == inside.get_text_from_textbox('USERNAME')

    #Write on the username textbox using the username of the file.
    inside.write_on_textbox(user.password,'PASSWORD')

    #Click the top left Menu button.
    inside.click_btn('MENUBTN')

    #Click the Timesheet option of the menu.
    inside.click_btn('TIMESHEETSPAN')
    #validar que entro al timetask
    
    #Delete this timer
    time.sleep(10)