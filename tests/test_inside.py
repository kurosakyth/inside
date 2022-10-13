from pages.login import inside_login_page

def test_prueba(browser):
    inside = inside_login_page(browser)
    inside.load()
    assert 'PortalWeb' == inside.get_title()
    inside.click_autho_button()
    assert 'Sign In with Auth0' == inside.get_title()

#Prueba correcta, no tocar
# from selenium import webdriver
# def test_prueba2():
#     driver = webdriver.Chrome()
#     driver.get("http://www.python.org")
#     assert "Python" in driver.title
#     driver.quit()