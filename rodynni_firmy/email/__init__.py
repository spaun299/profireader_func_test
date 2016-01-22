import config
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    def __init__(self, username=config.MAIL_GMAIL, password=config.MAIL_PWD, text=None, subject='Test Error',
                 send_to=None):
        self.username = username
        self.password = password
        self.text = text
        self.subject = subject
        self.send_to = send_to or [username]

    def send_email(self):
        msg = MIMEText(self.text)

        msg['Subject'] = self.subject
        msg['From'] = self.username
        msg['To'] = self.send_to
        s = smtplib.SMTP('localhost')
        s.sendmail(self.username, self.send_to, msg.as_string())
        s.quit()

