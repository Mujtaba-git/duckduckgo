from selenium.webdriver.common.by import By
from .base_page import BasePage


class SearchPage(BasePage):
    URL = "https://duckduckgo.com/"
    SEARCH_INPUT = (By.ID, "search_form_input_homepage")
    SEARCH_BUTTON = (By.ID, "search_button_homepage")

    def load(self):
        self.driver.get(self.URL)

    def search(self, query):
        self.wait_for_element(self.SEARCH_INPUT)
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(query)
        self.wait_and_click(self.SEARCH_BUTTON)
