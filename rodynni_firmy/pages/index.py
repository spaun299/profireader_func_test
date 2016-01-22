from ..site_parts.footer import Footer
from selenium.webdriver.common.keys import Keys
from .general import General


class IndexPage(General):
    def __init__(self, device='PHONE'):
        self.device = device
        super().__init__(device=self.device)
