import pytest
from allure_commons.types import AttachmentType

from src.pageObjects.reports import Report
from src.pageObjects.loginPage import LoginPage

import time
import allure


class TestReport:
    @pytest.mark.usefixtures("login")
    def test_report_text(self, login):
        driver = login
        report = Report(driver)
        time.sleep(5)
        report.get_report_tab().click()
        report_text = report.get_report_text().text
        assert report_text == "This automatically displays all your Laboratory Reports. You may also upload a report from a laboratory not in our system."
        print(report_text)

    @pytest.mark.usefixtures("login")
    def test_upload_button(self,login):
        driver = login
        report = Report(driver)
        time.sleep(5)
        report.get_report_tab().click()
        report.get_upload_button().is_displayed()


