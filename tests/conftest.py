import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()

    driver.get("https://www.docsmart.in/")
    username = os.getenv("NAME")
    password = os.getenv("PASSWORD")

    print("NAME:", username)
    print("PASSWORD:", password)

    request.cls.driver = driver

    request.cls.username = username
    request.cls.password = password

    yield driver
    driver.quit()
