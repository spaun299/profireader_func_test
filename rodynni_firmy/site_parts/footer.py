from ..site_parts.header import Header


class Footer:
    def __init__(self, driver=None):
        self.driver = driver

    def __call__(self, *args, **kwargs):
        print('call footer')

    @classmethod
    def __repr__(cls):
        return 'footer'
