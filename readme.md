Curso sobre elementos en web avanzados: Locating web elements Strategies TAU Andrew Knight
Curso sobre AI para seleccion de elementos: AI for Element Selection: Erasing the Pain of Fragile Tests Scripts Jason Arbon

Requirements:
    Python.
    Pipenv:
        pip install pipenv
        pipenv install
        pipenv run python -m pytest (if this displays an error you must..)
            pipenv --python #pythonVersionInstalled
            pipenv update

            pipenv install pytest (if no module of pytest found)
        pipenv install selenium

To print in console a print(something) you should use the command pipenv run python -m pytest -s

Always a file named 'tests' and inside the files.py made must contain the name 'test_'name'.py

tests\conftest.py file must contains the following structure:

    import pytest
    import selenium.webdriver

    @pytest.fixture
        def browser():
            #Initialize the chromeDriver instance
            b = selenium.webdriver.Chrome()
            #Make its calls wait up to 10 seconds for elements to appear
            b.implicitly_wait(10)
            #Return the webdriver instance for the setup
            yield b
            #Quit the webdriver instance for the cleanup
            b. quit()

the test made on tests must contains this following structure (tests\test_name.py):
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
