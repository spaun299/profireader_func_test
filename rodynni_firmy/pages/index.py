from ..site_parts.header import Header
from ..site_parts.footer import Footer
from selenium.webdriver.common.keys import Keys


class IndexPage(object):
    def __init__(self, driver):
        self.driver = driver
