from selenium.webdriver.common.keys import Keys


class Header:
    def __init__(self, driver=None):
        self.driver = driver

    def __call__(self, *args, **kwargs):
        print('call header')

    @classmethod
    def __repr__(cls):
        return 'header'
