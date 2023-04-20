from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base_page import BasePage

class ResultPage(BasePage):
    RESULT_TITLES = (By.CSS_SELECTOR, "a.result__a")
    NEXT_BUTTON = (By.CSS_SELECTOR, "a.result--more__btn")
    SEARCH_INPUT_RESULT = (By.ID, "search_form_input")

    def result_titles(self):
        return self.wait_for_elements(self.RESULT_TITLES)

    def next_page(self):
        self.wait_for_element(self.NEXT_BUTTON).click()

    def search(self, query):
        search_input = self.wait_for_element(self.SEARCH_INPUT_RESULT)
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def link_results(self):
        return self.wait_for_elements(self.RESULT_TITLES)
