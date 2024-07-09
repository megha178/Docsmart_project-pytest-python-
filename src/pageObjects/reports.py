import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Report:
    def __init__(self, driver):
        self.driver = driver

    report_tab = (By.XPATH, "//p[normalize-space()='Reports']")
    report_text = (By.XPATH, "//p[@class='mb-0']")
    upload_button = (By.XPATH,"//button[@class='btn btn-grn-solid fluid-btn v-btn theme--light']")

    def get_report_tab(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.report_tab)
        )

    def get_report_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.report_text)
        )

    def get_upload_button(self):
        return WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(self.upload_button)
        )
