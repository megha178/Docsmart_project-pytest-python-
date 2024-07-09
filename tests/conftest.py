import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
from src.pageObjects.loginPage import LoginPage

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='session')
def driver_init(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"unsupported browser:{browser_name}")
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def login(driver_init):
    driver = driver_init
    driver.get("https://www.docsmart.in/")
    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    loginPage = LoginPage(driver)
    loginPage.login_patient(user=username, pwd=password)
    return driver

    ''''
    #print("NAME:", username)
    #print("PASSWORD:", password)

        request.cls.driver = driver

        request.cls.username = username
        request.cls.password = password

        yield driver
        driver.quit()
        
        '''
