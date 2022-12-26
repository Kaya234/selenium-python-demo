from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# search function
SEARCH_USERNAME_TEXTBOX = (By.CSS_SELECTOR, ':nth-child(2) > .oxd-input')
SEARCH_NAME_TEXTBOX = (By.CSS_SELECTOR, '.oxd-autocomplete-text-input > input')
SEARCH_NAME_AUTOCOMPLETE = (By.CSS_SELECTOR, '.oxd-autocomplete-dropdown')
SEARCH_BUTTON = (By.CSS_SELECTOR, '.oxd-form-actions > .oxd-button--secondary')
SEARCH_RESULT = (By.CSS_SELECTOR, '.orangehrm-horizontal-padding > .oxd-text')

# user role dropdown
SEARCH_ROLE_DROPDOWN = \
    (By.CSS_SELECTOR, ':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper > .oxd-select-text')
SEARCH_ROLE_OPTION = (By.CSS_SELECTOR, '.oxd-select-option')
SEARCH_ROLE_TEXT = '//div[2]/div[3]/div/div[2]/div/div/div[3]/div'

# status dropdown
SEARCH_STATUS_DROPDOWN = \
    (By.CSS_SELECTOR, ':nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper > .oxd-select-text')
SEARCH_STATUS_OPTION = (By.CSS_SELECTOR, '.oxd-select-option')
SEARCH_STATUS_TEXT = '//div[2]/div[3]/div/div[2]/div/div/div[5]/div'
SEARCH_TABLE = ".oxd-table-body"

# error
INFO_TOAST_MESSAGE = '.oxd-toast'


class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def change_page_to_admin(self):
        self.click_contain_text('Admin')

    def check_default_input_values(self):
        self.assert_true_text(SEARCH_USERNAME_TEXTBOX, '')
        self.assert_true_text(SEARCH_ROLE_DROPDOWN, '-- Select --')
        self.assert_true_text(SEARCH_NAME_TEXTBOX, '')
        self.assert_true_text(SEARCH_STATUS_DROPDOWN, '-- Select --')

    def name_autocomplete(self):
        self.autocomplete(SEARCH_NAME_AUTOCOMPLETE)

    def search_result(self, message):
        self.assert_true_search_result(message)

    def select_option_role(self, option):
        self.click_on(SEARCH_ROLE_DROPDOWN)
        self.click_contain_text_dropdown(option)

    def check_search_result_role(self, role):
        self.assert_true_list(SEARCH_TABLE, SEARCH_ROLE_TEXT, role)

    def select_option_status(self, option):
        self.click_on(SEARCH_STATUS_DROPDOWN)
        self.click_contain_text_dropdown(option)

    def check_search_result_status(self, status):
        self.assert_true_list(SEARCH_TABLE, SEARCH_STATUS_TEXT, status)

    def check_search_toast_message(self, message):
        self.assert_true_toast(message)

    def search_username(self, username):
        self.type(SEARCH_USERNAME_TEXTBOX, username)

    def search_name(self, name):
        self.type(SEARCH_NAME_TEXTBOX, name)

    def click_search(self):
        self.click_on(SEARCH_BUTTON)
