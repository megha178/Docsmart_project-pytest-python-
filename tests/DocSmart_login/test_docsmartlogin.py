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
    @pytest.mark.usefixtures("setup")
    def test_invalid_login(self, setup):
        driver = setup
        loginPage = LoginPage(driver)
        loginPage.login_patient(user="2333222222", pwd=self.password)
        assert loginPage.get_error_msg().is_displayed()
        allure.attach(driver.get_screenshot_as_png(), name="invalid_login", attachment_type=AttachmentType.PNG)

    @pytest.mark.smoke
    @pytest.mark.usefixtures("setup")
    def test_valid_login(self, setup):
        driver = setup
        loginPage = LoginPage(driver)
        loginPage.login_patient(user=self.username, pwd=self.password)
        time.sleep(5)
        print(self.username)
        print(self.password)
        assert "https://app.docsmart.in/patient/dashboard" in driver.current_url
