
import smtplib
from sendgrid import SendGridAPIClient
import config

def send_smtp_email(SMTP_SERVER, SMTP_PORT, USER_SMTP, PASSWORD_SMTP,RECEPIENT_FILE, SENDER, message):    
    try:
        #TODO: SendGrid email needs work on FileType/Attachment of csv
        #sg_message = prepEmail.prep_SendGrid_email(FILEPATH, SENDER, RECEPIENT, SUBJECT)

        # Send SMTP email
        smtpObj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(USER_SMTP, PASSWORD_SMTP)

        with open(RECEPIENT_FILE, "r") as rfile:
            for recepient in rfile:
                print("Sending SMTP email to:", recepient)
                smtpObj.sendmail(SENDER, recepient, message.as_string())
        smtpObj.quit()
        
    except Exception as e:
        print("Error,", e)
    finally:
        print("send_smtp_email completed...")

def send_sg_email(sg_message):
    try:
        # TODO: Adjust SendGrid email capabilities
        sg = SendGridAPIClient(config.SG_API_KEY)
        response = sg.send(sg_message)
        print(response.status_code, response.body, response.headers)
    except Exception as e:
        print("Error", e)
    finally:
        print("send_sg_email completed...")