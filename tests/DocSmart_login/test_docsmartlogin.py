import pytest
from allure_commons.types import AttachmentType

from src.pageObjects.loginPage import LoginPage
import time
import allure


class TestDocSmart:

    #  @allure.feature("App_login")
    #   @allure.story("positive test case in docsmartlogin")
    #   @allure.description("valid username and password")
    #   @pytest.mark.positive

    @pytest.mark.qa
    @pytest.mark.usefixtures("driver_init")
    @pytest.mark.usefixtures("login")

   # @pytest.mark.usefixtures("setup")
   # @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_invalid_login(self,login):
       # driver = driver_init
        driver = login
        loginPage = LoginPage(driver)
        loginPage.login_patient(user="2333222222", pwd="Admin@123")
        assert loginPage.get_error_msg().is_displayed()
        allure.attach(driver.get_screenshot_as_png(), name="invalid_login", attachment_type=AttachmentType.PNG)

    @pytest.mark.smoke
   # @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("driver_init")
    @pytest.mark.usefixtures("login")

 #   @pytest.mark.parametrize("browser_name", ["chrome"])
    def test_valid_login(self,login):
       # driver = driver_init
        driver = login
        loginPage = LoginPage(driver)
        loginPage.login_patient(user="7021656297", pwd="Admin@123")
        time.sleep(5)
        print(self.username)
        print(self.password)
        assert "https://app.docsmart.in/patient/dashboard" in driver.current_url
        driver.save_screenshot('dashboard.png')
