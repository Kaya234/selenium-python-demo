import unittest
from selenium import webdriver

from pages.login_page import LoginPage

VALID_NAME = "Admin"
VALID_PASSWORD = "admin123"


class LoginTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login = LoginPage(self.driver)
        self.login.go_to_url()

    def tearDown(self):
        super().tearDown()
        self.driver.close()
        self.driver.quit()

    # Login
    def test_without_credentials(self):
        self.login.click_login()
        self.login.check_input_error_username()
        self.login.check_input_error_password()

    def test_withoutUsername(self):
        self.login.enter_username(VALID_NAME)
        self.login.click_login()
        self.login.check_input_error_password()

    def test_withoutPassword(self):
        self.login.enter_password(VALID_PASSWORD)
        self.login.click_login()
        self.login.check_input_error_username()

    def test_validCredentials(self):
        self.login.enter_username(VALID_NAME)
        self.login.enter_password(VALID_PASSWORD)
        self.login.click_login()
        self.login.check_valid_login()

    def test_invalidUsername(self):
        self.login.enter_username("admi")
        self.login.enter_password(VALID_PASSWORD)
        self.login.click_login()
        self.login.check_invalid_login_error()

    def test_invalidPassword(self):
        self.login.enter_username(VALID_NAME)
        self.login.enter_password("Admin123")
        self.login.click_login()
        self.login.check_invalid_login_error()

    # Forgotten Password
    def test_clickResetWithoutUsername(self):
        self.login.click_reset()
        self.login.click_reset_submit()
        self.login.check_reset_input_error()

    def test_clickResetWithUsername(self):
        self.login.click_reset()
        self.login.reset_enter_username(VALID_NAME)
        self.login.click_reset_submit()
        self.login.check_reset_success_info()

    def test_clickCancel(self):
        self.login.click_reset()
        self.login.click_reset_cancel()
        self.login.check_return_to_login_page()

    # Logout
    def test_logoutLoginInputsEmpty(self):
        self.login.login()
        self.login.logout()
        self.login.check_empty_inputs()


if __name__ == "__main__":
    unittest.main()
