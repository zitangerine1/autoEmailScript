import smtplib
import ssl
import time, random

from email.message import EmailMessage
from readUtils import getSponsorList
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# TODO - HTML emails.

emailSender = 'sponsor.cloudhacks@gmail.com'
emailPassword = 'wnkvooxnmavgofav'
emailReceiver = 'zitangr@gmail.com'

sponsorList = getSponsorList("./assets/CloudHacks Dummy Test Data.csv")

for sponsor in sponsorList:
    subject = 'Test Email'

    msg = EmailMessage()
    msg['From'] = emailSender
    msg['To'] = sponsor[1]
    msg['Subject'] = subject

    msg.set_content(f'Hello {sponsor[0]},\n\nThis is a test text email.\n\nBest,\nCloudHacks Team')
    msg.add_alternative(f"""\
    <!DOCTYPE html>
        <html>
            <body>
                <p>Hello {sponsor[0]},</p>
                <p>This is a test email.</p>
                <p>Best,</p>
                <p>CloudHacks Team</p>
            </body>
        </html>
                                                """, subtype='html')

    with open('./assets/cloudhacks_prospectus.pdf', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='cloudhacks_prospectus.pdf')
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, msg.as_string())