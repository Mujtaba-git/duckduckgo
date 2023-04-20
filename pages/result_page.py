from selenium.webdriver.common.by import By
from .base_page import BasePage


class ResultPage(BasePage):
    #RESULT_LINKS = (By.CSS_SELECTOR, "div#links a.result__url")
    RESULT_LINKS = (By.ID, "links_wrapper")

    def link_results(self):
        self.wait_for_element(self.RESULT_LINKS)
        return self.driver.find_elements(*self.RESULT_LINKS)

    def navigate_to_next_page(self):
        next_button = self.driver.find_element_by_css_selector("a.pagination__button--next")
        next_button.click()
