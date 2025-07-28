import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("GMAIL_ADDRESS")
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def send_email(to_address, subject, body, attachment_path=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_address
    msg.set_content(body)
    if attachment_path:
        with open(attachment_path, 'rb') as f:
            data = f.read()
            msg.add_attachment(data, maintype='application', subtype='pdf', filename='CV.pdf')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
