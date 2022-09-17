from email.message import EmailMessage
import ssl
import smtplib

receiver = 'k191264@nu.edu.pk'
sender = 'anonymousghost2007@gmail.com'
password = 'xickiralvljrxyta'

subject = input("Enter Subject: ")
message = input("Enter Message: ")

msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver
msg.set_content(message)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())     