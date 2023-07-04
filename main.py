import smtplib
import ssl
import time, random
import mimetypes

from getpass import getpass
from email.message import EmailMessage
from email.utils import make_msgid
from readUtils import getSponsorList

password = getpass('Enter access key: ')
batchSize = int(input('Enter email batch size: '))

emailSender = 'sponsor.cloudhacks@gmail.com'
emailPassword = password

sponsorList = getSponsorList("./assets/dummy_data.csv")
image_cid = make_msgid()

for sponsor in sponsorList:
    emailReceiver = f'{sponsor[1]}'
    subject = (f'CloudHacks 2023 and {sponsor[0]} Partnership')

    msg = EmailMessage()
    msg['From'] = emailSender
    msg['To'] = sponsor[1]
    msg['Subject'] = subject

    msg.set_content(f"""\
<html>
    <body>
        <p>To whom this may regard, </p>
        <p>
            I'm reaching out on behalf of <strong>CloudHacks</strong>, a student-led hackathon based in Singapore, and we’d like your help. A hackathon is a weekend-long invention marathon where high school and college students from all over Singapore will spend the weekend building awesome projects. CloudHacks will be held on the 5th and 6th of August 2023, in partnership with Google Cloud. 
        </p>
        <p>
            <strong>Our mission</strong>
                    <br>
            We believe that the best way for us to learn and develop skills is by doing things together - when we bond together and share our ideas, the things that we can achieve are much greater than what we can do alone. Thus, we created CloudHacks: a groundbreaking 24h+ hackathon where people of different backgrounds, ages, and skills can come to work together to create amazing new things: to innovate.        
        </p>
        <p>
            <strong>Why you should sponsor us</strong>
                    <br>
            To fully realize the goal of our hackathon, we need resources. This is what we’d like to ask of you: by sponsoring us, you'll not only have the opportunity to interact with bright young minds and make a lasting impression on the people of our future but also possibly see a problem you or the world faces solved. 
        </p>
        <p>
            More information is in the sponsorship package attached below! If you are interested or have any further questions, we’ll be happy to meet and connect with you to further discuss the opportunities available and benefit mutually.
        </p>
        <p>Best, CloudHacks Team.</p>
        <img src="cid:{image_cid[1:-1]}" alt="logo" height="150px">
    </body>
</html>

                                                """, subtype='html')

    with open('./assets/cloudhacks_prospectus.pdf', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='cloudhacks_prospectus.pdf')
    context = ssl.create_default_context()

    with open('./assets/images/postscript.png', 'rb') as img:
        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
        msg.get_payload()[1].add_related(img.read(), maintype=maintype,subtype=subtype, cid=image_cid)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)

        batchCount = 0
        batchNum = 0

        if batchCount < batchSize:
            print(f'Sending email to {sponsor[0]}...')
            time.sleep(random.randint(3, 10))
            smtp.sendmail(emailSender, emailReceiver, msg.as_string())
            batchCount += 1
        else:
            print(f'Batch {batchNum} sent. Waiting for cooldown...')
            time.sleep(random.randint(30, 60))
            batchNum += 1

        