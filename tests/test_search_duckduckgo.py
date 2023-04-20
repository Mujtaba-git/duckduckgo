import pytest
from selenium import webdriver
from pages.search_page import SearchPage
from pages.result_page import ResultPage

class TestSearchDuckDuckGo:
    @pytest.fixture(scope="class")
    def driver(self):
        with webdriver.Firefox() as driver:
            yield driver

    @pytest.mark.parametrize("query", ["Python", "Selenium", "Pytest"])
    def test_search_query(self, driver, query):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search(query)

        found_query_in_result = False
        for result in result_page.result_titles():
            if query.lower() in result.text.lower():
                found_query_in_result = True
                break

        assert found_query_in_result

    def test_no_results(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search("asdasdasdqwertyyui")

        assert len(result_page.result_titles()) == 0

    def test_page_navigation(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search("Python")

        for _ in range(3):
            result_page.next_page()
            assert len(result_page.result_titles()) > 0

    def test_search_bar_on_result_page(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search("Python")
        result_page.search("Selenium")

        for result in result_page.link_results():
            assert "selenium" in result.text.lower()

    def test_result_titles(self, driver):
        search_page = SearchPage(driver)
        result_page = ResultPage(driver)

        search_page.load()
        search_page.search("Python")

        for result in result_page.result_titles():
            assert len(result.text.strip()) > 0

