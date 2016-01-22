from ..site_parts.footer import Footer
from ..site_parts.header import Header
from selenium.webdriver import Firefox
from config import RODYNNIFIRMY_URL, WINDOW_SIZE
from ..email import SendEmail


class General(object):
    
    driver = Firefox()
    dependences = ('header', 'footer')

    def __init__(self, dependences=dependences, driver=driver, device='PC', testing_page=RODYNNIFIRMY_URL):
        self.device = device
        self.driver = driver
        self.testing_page = testing_page
        self.send_email = SendEmail().send_email
        self.call_dependences(dependences)

    def set_config(self):
        window_size = WINDOW_SIZE[self.device]
        self.driver.set_window_size(*window_size)
        self.driver.get(self.testing_page)
        self.driver.implicitly_wait(3)

    def call_dependences(self, dependences):
        classes = (Header, Footer)
        [a() for a in map(lambda cls: cls(driver=self.driver),
                          filter(lambda cls: cls.__repr__() in dependences, classes))]
