#task handling file(Email Bot)

import smtplib
from email.message import EmailMessage


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ajay.pediredla.1818@gmail.com', '8143232797')
    email = EmailMessage()
    email['From'] = 'ajay.pediredla.1818@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

