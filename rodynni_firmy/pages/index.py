from ..site_parts.footer import Footer
from selenium.webdriver.common.keys import Keys
from .general import General
import config


class IndexPage(General):
    testing_page = config.RODYNNIFIRMY_URL

    def __init__(self, device='PC'):
        self.device = device
        self.set_config()
        super().__init__(device=self.device, testing_page=self.testing_page)
