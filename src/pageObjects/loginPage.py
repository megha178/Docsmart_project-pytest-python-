import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login_button_Hp = (By.XPATH, "//li[@id='loginRegister']")
    select_role = (By.XPATH, "//div[@role='button']")
    patient_role = (By.XPATH, "//div[contains(text(),'User/ Patient')]")
    username = (By.XPATH, "//label[text()='Enter your mobile number here.']/following-sibling::input")
    password = (By.XPATH, "//div[@class='v-text-field__slot']/input[@type='password']")
    login_button = (By.XPATH, "//span[normalize-space()='Login']")
    error_msg = (By.CSS_SELECTOR, "div[role='status']")

    def get_login_button_hp(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_Hp))

    def get_select_role(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.select_role))

    def get_patient_role(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.patient_role))

    def get_username(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username))

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_error_msg(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_msg))

    def login_patient(self, user, pwd):
        self.get_login_button_hp().click()
        self.get_select_role().click()
        self.get_patient_role().click()
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_login_button().click()
        time.sleep(3)
