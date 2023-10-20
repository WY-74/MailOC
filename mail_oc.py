from typing import Dict, List
from email.header import Header
from email.mime.text import MIMEText


class MailOC:
    def __init__(self, mime, stp):
        self.mime = mime
        self.stp = stp

    def get_mime_from(self, sender: Dict[str, str]):
        # sender: {"name": "xxx", "email": "xxx@xxx.com"}

        return f"{sender['name']}<{sender['email']}>"

    def get_mime_to(self, receivers: List[Dict[str, str]]):
        # receivers: [{"name": "xxx1", "email": xxx@xxx.com}, {"name": "xxx2", "email": xxx@xxx.com}]

        mm_to = ""
        for receiver in receivers:
            mm_to += f"{receiver['name']}<{receiver['email']}>,"
        return mm_to

    def set_from_to(self, sender: Dict[str, str], receivers: List[Dict[str, str]]):
        self.mime["From"] = self.get_mime_from(sender)
        self.mime["To"] = self.get_mime_to(receivers)

    def set_subject(self, subject):
        if self.mime["Subject"]:
            del self.mime["Subject"]  # Create a new topic instead of appending
        self.mime["Subject"] = Header(subject, 'utf-8')

    def set_plain_body(self, body):
        if self.mime.get_payload():
            self.mime.set_payload([])
        self.mime.attach(MIMEText(body, "plain", "utf-8"))

    def send_email(self, sender: str, receivers: List[str]):
        # sender: "xxx@xxx.com"
        # receivers: ["xxx@xxx.com", "xxx@xxx.com"]

        self.stp.sendmail(sender, receivers, self.mime.as_string())

    def disconnect(self):
        self.stp.quit()
