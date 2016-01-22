class GeneralPart(object):

    def __init__(self, driver):
        self.division_xpath = self.get_division_xpath()
        self.driver = driver

    @staticmethod
    def get_division_xpath():
        return "//div[@class='well']/div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav']/li/a"

    def switch_division(self, division_name):
        link = self.driver.find_element_by_xpath(
            self.get_division_xpath() + '[@value={division_name}]'.format(division_name=division_name))
        link.click()
        assert division_name in self.driver.current_url

    def get_number_of_current_page(self):
        return int(self.driver.find_element_by_xpath("//ul[@class='pager']/li[@class='current-page']/a").text)

    def get_current_division_name(self):
        return self.driver.find_element_by_xpath("//div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav']"
                                                 "/li/a[@id='navigation_selected_division']").text
