from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'joshuazicofowler@gmail.com'
email_password = 'ricu zbfq hioz rscx'
email_receiver = 'joshuazicofowler@gmail.com'

subject = 'Your plant needs watering'
body = """
Your plant low on water my dude
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_sender
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail,com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

