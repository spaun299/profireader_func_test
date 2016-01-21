from .pages.index import IndexPage
from config import RODYNNIFIRMY_URL, WINDOW_SIZE


def start_test(driver, device):
    window_size = WINDOW_SIZE[device]
    driver.set_window_size(*window_size)
    driver.get(RODYNNIFIRMY_URL)
    driver.implicitly_wait(3)
