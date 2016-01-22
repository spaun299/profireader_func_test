from ..site_parts.footer import Footer
from ..site_parts.header import Header
from selenium.webdriver import Firefox
from config import RODYNNIFIRMY_URL, WINDOW_SIZE


class General(object):
    driver = Firefox()

    dependences = ('footer', 'header')

    def __init__(self, dependences=dependences, driver=driver, device='PC'):
        self.set_config()
        self.call_dependences(dependences)
        self.device = device
        self.driver = driver

    def set_config(self):
        window_size = WINDOW_SIZE[self.device]
        self.driver.set_window_size(*window_size)
        self.driver.get(RODYNNIFIRMY_URL)
        self.driver.implicitly_wait(3)

    def call_dependences(self, dependences):
        classes = (Footer, Header)
        [a() for a in map(lambda cls: cls(driver=self.driver),
                          filter(lambda cls: cls.__repr__() in dependences, classes))]
