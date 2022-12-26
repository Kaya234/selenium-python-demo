from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# login
URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
LOGIN_PAGE_TITLE = (By.CSS_SELECTOR, '.oxd-text--h5')
USERNAME_TEXTBOX = (By.CSS_SELECTOR, ':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input')
PASSWORD_TEXTBOX = (By.CSS_SELECTOR, ':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input')
LOGIN_BUTTON = (By.CSS_SELECTOR, '.oxd-button')

# login errors
PAGE_TITLE = (By.CSS_SELECTOR, '.oxd-topbar-header-breadcrumb > .oxd-text')
ERROR_LOGIN = (By.CSS_SELECTOR, '.oxd-alert-content > .oxd-text')
ERROR_USERNAME_INPUT = (By.CSS_SELECTOR, ':nth-child(2) > .oxd-input-group > .oxd-text')
ERROR_PASSWORD_INPUT = (By.CSS_SELECTOR, ':nth-child(3) > .oxd-input-group > .oxd-text')

# reset password
RESET_BUTTON = (By.CSS_SELECTOR, '.orangehrm-login-forgot > .oxd-text')
RESET_P_TEXTBOX = (By.CSS_SELECTOR, '.oxd-input')
RESET_BUTTON_SUBMIT = (By.CSS_SELECTOR, '.oxd-button--secondary')
RESET_BUTTON_CANCEL = (By.CSS_SELECTOR, '.oxd-button--ghost')
RESET_ER_USERNAME_INPUT = (By.CSS_SELECTOR, '.oxd-input-group > .oxd-text')
RESET_SUCCESS_INFO = (By.CSS_SELECTOR, '.oxd-text--h6')

# log out
PROFILE_DROPDOWN = (By.CSS_SELECTOR, '.oxd-userdropdown-tab')
LOGOUT_BUTTON = (By.CSS_SELECTOR, ':nth-child(4) > .oxd-userdropdown-link')


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_url(self):
        self.visit(URL)

    def click_login(self):
        self.click_on(LOGIN_BUTTON)

    def login(self):
        self.type(USERNAME_TEXTBOX, "Admin")
        self.type(PASSWORD_TEXTBOX, "admin123")
        self.click_on(LOGIN_BUTTON)

    def enter_username(self, username):
        self.type(USERNAME_TEXTBOX, username)

    def enter_password(self, password):
        self.type(PASSWORD_TEXTBOX, password)

    # Login errors
    def check_valid_login(self):
        self.assert_true_text(PAGE_TITLE, "Dashboard")

    def check_invalid_login_error(self):
        self.assert_true_text(ERROR_LOGIN, "Invalid credentials")

    def check_input_error_username(self):
        self.assert_true_text(ERROR_USERNAME_INPUT, "Required")

    def check_input_error_password(self):
        self.assert_true_text(ERROR_PASSWORD_INPUT, "Required")

    def reset_enter_username(self, username):
        self.type(RESET_P_TEXTBOX, username)

    def click_reset(self):
        self.click_on(RESET_BUTTON)

    def click_reset_submit(self):
        self.click_on(RESET_BUTTON_SUBMIT)

    def click_reset_cancel(self):
        self.click_on(RESET_BUTTON_CANCEL)

    def check_reset_input_error(self):
        self.assert_true_text(RESET_ER_USERNAME_INPUT, "Required")

    def check_reset_success_info(self):
        self.assert_true_text(RESET_SUCCESS_INFO, "Reset Password link sent successfully")

    def check_return_to_login_page(self):
        self.assert_true_text(LOGIN_PAGE_TITLE, "Login")

    def logout(self):
        self.click_on(PROFILE_DROPDOWN)
        self.click_on(LOGOUT_BUTTON)

    def check_empty_inputs(self):
        self.assert_true_text(USERNAME_TEXTBOX, "")
        self.assert_true_text(PASSWORD_TEXTBOX, "")
