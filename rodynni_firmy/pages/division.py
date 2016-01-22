from ..site_parts.footer import Footer


class Division(Footer):
    def __init__(self, driver):
        super(Footer, self).__init__(driver)
        self.driver = driver
