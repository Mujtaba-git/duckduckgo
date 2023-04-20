from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class SearchPage(BasePage):
    URL = "https://duckduckgo.com/"
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="searchbox_homepage"]/div/div/button')

    def load(self):
        self.driver.get(self.URL)

    def search(self, query):
        search_input = self.wait_for_element(self.SEARCH_INPUT)
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

