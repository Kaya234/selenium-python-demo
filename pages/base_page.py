from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def click_on(self, element):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(element)).click()

    def type(self, element, text):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(element)).send_keys(text)

    def assert_true_text(self, element, text):
        actual_string = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(element))
        assert actual_string.text == text

    def click_contain_text(self, text):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[text()="' + text + '"]'))).click()

    def click_contain_text_dropdown(self, option):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[span[text()="' + option + '"]]'))).click()

    def assert_true_toast(self, message):
        actual_string = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//p[text()="' + message + '"]')))
        assert actual_string.text == message

    def assert_true_search_result(self, message):
        actual_string = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[span[text()="' + message + '"]]')))
        assert actual_string.text == message

    def assert_true_list(self, table, element, text):
        rows = self.driver.find_elements(By.CSS_SELECTOR, table)
        for row in rows:
            assert row.find_element(By.XPATH, element).text == text

    def autocomplete(self, element):
        time.sleep(5)
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(element)).click()
