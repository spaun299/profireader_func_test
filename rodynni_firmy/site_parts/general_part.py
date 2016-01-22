class GeneralPart(object):

    def __init__(self, driver):
        self.division_xpath = self.get_division_xpath()
        self.driver = driver

    @staticmethod
    def get_division_xpath():
        return "//div[@class='well']/div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav']/li/a"

    def switch_division(self, division_name):
        path = self.get_division_xpath() + '[@value={division_name}]'.format(division_name=division_name)
