import unittest

from selenium import webdriver
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

VALID_S_USERNAME = "David.Morris"
VALID_S_NAME = "David Morris"


class AdminSearchTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login = LoginPage(self.driver)
        self.admin = AdminPage(self.driver)
        self.login.go_to_url()
        self.login.login()
        self.admin.change_page_to_admin()

    def tearDown(self):
        super().tearDown()
        self.driver.close()
        self.driver.quit()

    def test_default_state(self):
        self.admin.check_default_input_values()

    # Username field
    def test_invalid_username(self):
        self.admin.search_username("David")
        self.admin.click_search()
        self.admin.check_search_toast_message("No Records Found")
        self.admin.search_result("No Records Found")

    def test_valid_username_no_capitals(self):
        self.admin.search_username("david.morris")
        self.admin.click_search()
        self.admin.search_result("(1) Record Found")

    def test_valid_username_capitals(self):
        self.admin.search_username(VALID_S_USERNAME)
        self.admin.click_search()
        self.admin.search_result("(1) Record Found")

    # User Role Dropdown
    def test_select_option_ess(self):
        self.admin.select_option_role("ESS")
        self.admin.click_search()
        self.admin.check_search_result_role("ESS")

    def test_select_option_admin(self):
        self.admin.select_option_role("Admin")
        self.admin.click_search()
        self.admin.check_search_result_role("Admin")

    # Employee Name autocomplete Field
    def test_not_use_autocomplete(self):
        self.admin.search_name(VALID_S_NAME)
        self.admin.click_search()

    def test_use_autocomplete(self):
        self.admin.search_name(VALID_S_NAME)
        self.admin.name_autocomplete()
        self.admin.click_search()
        self.admin.search_result("(1) Record Found")

    # Status Dropdown
    def test_select_option_enabled(self):
        self.admin.select_option_status("Enabled")
        self.admin.click_search()
        self.admin.check_search_result_status("Enabled")

    def test_select_option_disabled(self):
        self.admin.select_option_status("Disabled")
        self.admin.click_search()
        self.admin.check_search_toast_message("Invalid Parameter")

    # Valid Search Combinations
    def test_username_role(self):
        self.admin.search_username(VALID_S_USERNAME)
        self.admin.select_option_role("ESS")
        self.admin.click_search()
        self.admin.search_result("(1) Record Found")

    def test_username_role_name(self):
        self.admin.search_username(VALID_S_USERNAME)
        self.admin.select_option_role("ESS")
        self.admin.search_name(VALID_S_NAME)
        self.admin.name_autocomplete()
        self.admin.click_search()
        self.admin.search_result("(1) Record Found")

    def test_username_role_name_status(self):
        self.admin.search_username(VALID_S_USERNAME)
        self.admin.select_option_role("ESS")
        self.admin.search_name(VALID_S_NAME)
        self.admin.name_autocomplete()
        self.admin.select_option_status("Enabled")
        self.admin.click_search()
        self.admin.search_result("(1) Record Found")

    # Invalid Search Combinations
    def test_ok_username_nok_role(self):
        self.admin.search_username(VALID_S_USERNAME)
        self.admin.select_option_role("Admin")
        self.admin.click_search()
        self.admin.search_result("No Records Found")
        self.admin.check_search_toast_message("No Records Found")

    def test_ok_username_ok_role_nok_name(self):
        self.admin.search_username(VALID_S_USERNAME)
        self.admin.select_option_role("ESS")
        self.admin.search_name("d")
        self.admin.name_autocomplete()
        self.admin.select_option_status("Enabled")
        self.admin.click_search()
        self.admin.search_result("No Records Found")
        self.admin.check_search_toast_message("No Records Found")

    def test_ok_username_ok_role_ok_name_nok_status(self):
        self.admin.search_username(VALID_S_USERNAME)
        self.admin.select_option_role("ESS")
        self.admin.search_name(VALID_S_NAME)
        self.admin.name_autocomplete()
        self.admin.select_option_status("Disabled")
        self.admin.click_search()
        self.admin.check_search_toast_message("Invalid Parameter")


if __name__ == "__main__":
    unittest.main()
