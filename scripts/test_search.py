from base.base_driver import init_driver
from page.page import Page


class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.page.setting.click_search()
        self.page.search.input_key_word("hello")
        self.page.search.click_back()