import base64, sys
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from email.utils import COMMASPACE
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

def prep_SMTPemail_body(FILEPATH, SENDER, SUBJECT):

    print(" Prepping SMTP email body")

    subject = SUBJECT
    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['Subject'] = subject

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(FILEPATH, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=str(FILEPATH))
    msg.attach(part)
    msg.attach(MIMEText('OCI SMTP Email: ' +  subject, 'plain'))
    return msg

## Bugged
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
        FileType(file_type=MIMEBase('application, "octet-stream')),
        Disposition('attachment')
    )
    message.attachment = attachedFile

    return message