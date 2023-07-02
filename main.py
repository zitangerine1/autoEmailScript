import smtplib
import ssl
from email.message import EmailMessage
from readUtils import getSponsorList

# TODO - Hide the email password, ideally by using environment variables.
# TODO - Integrate get from spreadsheet and send email.
# TODO - Attach PDF prospectus to email.

#emailSender = 'sponsor.cloudhacks@gmail.com'
#emailPassword = 'wnkvooxnmavgofav'
#emailReceiver = 'zitangr@gmail.com'

sponsorList = getSponsorList("assets\CloudHacks Dummy Test Data.csv")

for sponsor in sponsorList:
    subject = 'Test Email'
    body = 'This is a test email'

    msg = EmailMessage()
    msg['From'] = emailSender
    msg['To'] = sponsor[1]
    msg['Subject'] = subject
    msg.set_content(body)

    # sponsor[0] is sponsor name

    with open('./assets/cloudhacks_prospectus.pdf', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='cloudhacks_prospectus.pdf')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, msg.as_string())