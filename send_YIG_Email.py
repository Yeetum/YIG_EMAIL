import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

USER_SMTP = 'ocid1.user.oc1..aaaaaaaagf754hzzk23iy4awx4adk6js4uyjokrrhffkiagshocbkfuuhjha@ocid1.tenancy.oc1..aaaaaaaa5p3y7xokpuoj4vyuv4545wxu3ir5v4ltc26r7n7egpnqcssy6lha.if.com'
PASSWORD_SMTP = 'P!i0OR;g1a3kA9<}++Ps'
SENDER = 'info@yeetum.com'
SENDERNAME = 'Yeetum LLC'
# TODO: Add customer emails as recepients
RECEPIENT = ['tobalotv@gmail.com', 'ariesvtb@gmail.com', 'traderdave2112@gmail.com', 'ardito.bryan@gmail.com']
SMTP_SERVER = 'smtp.us-phoenix-1.oraclecloud.com'
SMTP_PORT = 587

FILEPATH = sys.argv[1]
SUBJECT_DATA = 'YIG Report - '+ str(FILEPATH)
SUBJECT = SUBJECT_DATA
FILENAME = SUBJECT_DATA

msg = MIMEMultipart()
msg['From'] = SENDER
msg['To'] = COMMASPACE.join(RECEPIENT)
msg['Subject'] = SUBJECT

part = MIMEBase('application', "octet-stream")
part.set_payload(open(FILEPATH, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=FILENAME)
msg.attach(part)

smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(USER_SMTP, PASSWORD_SMTP)
smtpObj.sendmail(SENDER, RECEPIENT, msg.as_string())
smtpObj.quit()