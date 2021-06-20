###
# This program is designed for sending FUMaaS reports to YIG Clients and Operaters. Built and managed by Yeetum Technologies. 
###

import sys
import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
from typing import Mapping
from pathlib import Path
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

# Import config variables
import config

def prep_SMTPemail_body(FILEPATH, SENDER, RECEPIENT, SUBJECT):

    print(" Prepping SMTP email body")

    subject = SUBJECT
    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['To'] = COMMASPACE.join(RECEPIENT)
    msg['Subject'] = subject

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(FILEPATH, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=str(FILEPATH))
    msg.attach(part)
    msg.attach(MIMEText('OCI SMTP Email', 'plain'))
    return msg

def prep_SendGrid_email(FILEPATH, SENDER, RECEPIENT, SUBJECT):

    print(" Prepping SendGrid email")

    message = Mail(
        from_email=SENDER,
        to_emails=RECEPIENT,
        subject=SUBJECT,
        html_content='<strong>YIG SendGrid Dev email</strong>'
    )

    with open(FILEPATH, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('text/csv'),
        Disposition('attachment')
    )
    message.attachment = attachedFile

    return message

if __name__ == "__main__":
    try:
        # Init variables
        FILEPATH = Path(sys.argv[1])
        USER_SMTP = config.USER_SMTP
        PASSWORD_SMTP = config.PASSWORD_SMTP
        SENDER = config.SENDER
        SENDERNAME = config.SENDERNAME
        SUBJECT = 'YIG Report - '+ str(FILEPATH.stem)

        # TODO: Add customer emails as recepients
        RECEPIENT = config.RECEPIENT

        SMTP_SERVER = config.SMTP_SERVER
        SMTP_PORT = config.SMTP_PORT

        # Prep email
        message = prep_SMTPemail_body(FILEPATH, SENDER, RECEPIENT, SUBJECT)
        sg_message = prep_SendGrid_email(FILEPATH, SENDER, RECEPIENT, SUBJECT)

        # Send SMTP email
        smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(USER_SMTP, PASSWORD_SMTP)
        smtpObj.sendmail(SENDER, RECEPIENT, message.as_string())
        smtpObj.quit()

        # Send SendGrid email
        sg = SendGridAPIClient(config.SG_API_KEY)
        response = sg.send(sg_message)
        print(response.status_code, response.body, response.headers)

    except Exception as e:
        print(e)
    finally:
        print("Email job finished...")