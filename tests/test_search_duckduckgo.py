import pytest
from pages.search_page import SearchPage
from pages.result_page import ResultPage

class TestSearchDuckDuckGo:
    @pytest.mark.parametrize("query", ["Python", "Selenium", "Pytest"])
    def test_search_query(self, driver, query):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search(query)

        for result in result_page.link_results():
            assert query.lower() in result.text.lower()

    def test_no_results(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search("asdasdasdqwertyyui")

        assert len(result_page.link_results()) == 0

    def test_page_navigation(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search("Python")

        for _ in range(3):
            result_page.navigate_to_next_page()
            assert len(result_page.link_results()) > 0
