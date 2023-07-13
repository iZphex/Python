from email.message import EmailMessage
import ssl
import smtplib

# go over to our gmail account setup 2 step authentication
# generate app password
# creat a function to send the mail

email_sender = 'FILL IN YOUR OWN EMAIL HERE'
email_password = 'EMAIL APP PASSWORD HERE'

email_receiver = 'WHOEVER YOU WANT TO SEND THE EMAIL TO HERE'

subject = "Sent from a python script"
body = """"
Hello PERSON, I was able to send this by using a python script that accesses my email via app password.
Thought it would be a good mini project to learn.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

