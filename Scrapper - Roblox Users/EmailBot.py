from email.message import EmailMessage
import ssl
import smtplib

receiver = ['dota2pakitan@gmail.com', 'animesoul824@gmail.com','yougeshdhomeja307@gmail.com','k191048@nu.edu.pk','k191120@nu.edu.pk','k191042@nu.edu.pk','k191090@nu.edu.pk','k191112@nu.edu.pk','k191107@nu.edu.pk']
sender = 'anonymousghost2007@gmail.com'
password = 'xickiralvljrxyta'

subject = input("Enter Subject: ")
message = input("Enter Message: ")

for i in receiver:
    print("Sending Email to: ", i)
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = i
    msg.set_content(message)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())     