from selenium.webdriver.common.keys import Keys
import random as rand
from .general_part import GeneralPart


class Header(GeneralPart):
    def __init__(self, driver=None):
        super().__init__(driver=driver)
        self.driver = driver

    def __call__(self, *args, **kwargs):
        self.test_top_navbar(random=True)

    @classmethod
    def __repr__(cls):
        return 'header'

    def test_top_navbar(self, random=False):
        xpath = self.division_xpath
        hrefs = self.driver.find_elements_by_xpath(xpath)
        if random:
            rand.choice(hrefs).click()
            assert 'Not Found' in self.driver.page_source, \
                'Page {page} Not Found'.format(page=self.driver.current_url)
