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
    #assert 'Inicia sesión: Cuentas de Google' == inside.get_title()
                    #Check the title of the page is the expected for windows Headless browser.
    assert 'Acceso: cuentas de Google' == inside.get_title()
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

    #Click the Timesheet option of the client dropdown.
    inside.click_btn('CLIENTDROPDOWNTIMETASK')
    
    #Click the Timesheet option of the project dropdown.
    inside.click_btn('QAOMBOARDINGTIMETASK')

    #Click the Timesheet option of the module dropdown.
    inside.click_btn('DEVELOPMENTTIMTASK')

    #Click the Timesheet option of the worktype dropdown.
    inside.click_btn('WORKTYPETIMETASK')

    #Write on Description of the Timesheet textbox.
    inside.write_on_textbox('Description information test.','DESCRIPTION')

    #Check that the username on the file is the one wrote.
    assert "Description information test." == inside.get_text_from_textbox('DESCRIPTION')

    #Write on Description of the Timesheet textbox. writes 04 in this case (example).
    inside.write_on_textbox('4','TIMEINPUTTIMETASK')

    #Check that the username on the file is the one wrote. 04 in this case (example).
    assert "04" == inside.get_text_from_textbox('TIMEINPUTTIMETASK')

    #Delete this timer
    time.sleep(10)

    #headless browser.