from selenium.webdriver.common.by import By
from .base_page import BasePage


class ResultPage(BasePage):
    RESULT_LINKS = (By.CSS_SELECTOR, "div#links a.result__url")

    def link_results(self):
        self.wait_for_element(self.RESULT_LINKS)
        return self.driver.find_elements(*self.RESULT_LINKS)
