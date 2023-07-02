import smtplib
import ssl
import random, time
from email.message import EmailMessage

# TODO - Integrate get from spreadsheet and send email.

pwdInput = input('Enter password: ')

emailSender = 'sponsor.cloudhacks@gmail.com'
emailPassword = pwdInput
emailReceiver = 'zitangr@gmail.com'

subject = 'Test Email'
body = open('./assets/emailbody.txt', 'r').read()

msg = EmailMessage()
msg['From'] = emailSender
msg['To'] = emailReceiver
msg['Subject'] = subject
msg.set_content(body)

with open('./assets/cloudhacks_prospectus.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='cloudhacks_prospectus.pdf')

context = ssl.create_default_context()

for i in range(1):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, msg.as_string())

    print(f'Email sent to {emailReceiver} successfully.')