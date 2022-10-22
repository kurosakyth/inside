Curso sobre elementos en web avanzados: Locating web elements Strategies TAU Andrew Knight
Curso sobre AI para seleccion de elementos: AI for Element Selection: Erasing the Pain of Fragile Tests Scripts Jason Arbon

Requirements:
    Set as environment variable the path of the webdriver:
        path: C:\Selenium
        With the driver inside named as chromedriver
    Python.
    Pipenv:
        pip install pipenv
        pipenv install
        pipenv install selenium
        pipenv install pytest
        pipenv install pytest-xdist (is to run tests on parallel)
        pipenv run python -m pytest (if this displays an error you must..)
            pipenv --python #pythonVersionInstalled
            pipenv update
        

To print in console a print(something) you should use the command: pipenv run python -m pytest -s
To run tests in parallel you should use, the # is to run specific number of test: pipenv run python -m pytest -n #

Always set the file name as 'tests' and inside the 'test_name'.py files format with the 'test_name():' methods.

tests\conftest.py file must contains the following structure:

    import pytest
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    # Set browser options to make it headless.  
    option = Options()
    option.headless = False

    # fixture where is set the chrome driver as default, implicit wait to 10, to return the driver and quit.
    @pytest.fixture
    def browser():
        driver = webdriver.Chrome(options= option)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()

The test made on tests must contains this following structure (tests\test_name.py):
    #This function uses browser from the conftest.py file as a fixture
    def test_basic_duckduckgo_Search(browser):
        #code
        #code
    raise Exception('Incomplete Test')

/pages/__init__.py
the __init__ means that this folder is a python package.

/pages/result.py
search_input = self.browser.find_element(*self.SEARCH_INPUT) ('*self....' el * significa que le está pasando un tuple '(By.ID, 'search_form_input')')
/pages/search.py

#Prueba correcta, no tocar.
# from selenium import webdriver
# def test_prueba2():
#     driver = webdriver.Chrome()
#     driver.get("http://www.python.org")
#     assert "Python" in driver.title
#     driver.quit()