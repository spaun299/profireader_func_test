from .pages.index import IndexPage
from .email import SendEmail


def start_test(device):
    send_email = SendEmail().send_email
    try:
        IndexPage(device=device)
    except AssertionError as e:
        send_email(exception=e)
