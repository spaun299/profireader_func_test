from ..site_parts.header import Header
from .general_part import GeneralPart


class Footer(GeneralPart):
    def __init__(self, driver=None):
        super().__init__(driver=driver)
        self.driver = driver

    def __call__(self, *args, **kwargs):
        print('footer')

    @classmethod
    def __repr__(cls):
        return 'footer'
