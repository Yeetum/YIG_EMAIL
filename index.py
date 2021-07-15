###
# This program is designed for sending FUMaaS reports to YIG Clients and Operaters. Built and managed by Yeetum Technologies. 
###

import sys
import smtplib
from pathlib import Path
import time
#from sendgrid import SendGridAPIClient

# Import config variables
import config

# Import mail prepper & htmlify
import prepEmail
import htmlify

if __name__ == "__main__":
    try:
        # Init variables
        FILEPATH = Path(sys.argv[1])
        USER_SMTP = config.USER_SMTP
        PASSWORD_SMTP = config.PASSWORD_SMTP
        SENDER = config.SENDER
        SENDERNAME = config.SENDERNAME

        RECEPIENT_FILE = sys.argv[2]
        SUBJECT = sys.argv[3]

        SMTP_SERVER = config.SMTP_SERVER
        SMTP_PORT = config.SMTP_PORT

        print('SUBJECT: ', SUBJECT)
        print('RECEPIENTS: ', RECEPIENT_FILE)
        print('FILETYPE:', FILEPATH.suffix)

        if not FILEPATH.exists():
            print("Oops, file doesn't exist!")
            raise ValueError('Filepath does not exist...')
        else:
            print("File located...")

        if FILEPATH.suffix == ".csv":
            print('CSV filepath, htmlify executing...')
            html = htmlify.htmlify_csv(FILEPATH, SUBJECT)
            message = prepEmail.prep_SMTPemail_body(FILEPATH, SENDER, SUBJECT, html)
        else:
            print('filepath not htmlified')
            FILEPATH = FILEPATH
            message = prepEmail.prep_SMTPemail_body(FILEPATH, SENDER, SUBJECT)

        
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

        # TODO: Adjust SendGrid email capabilities
        #sg = SendGridAPIClient(config.SG_API_KEY)
        #response = sg.send(sg_message)
        #print(response.status_code, response.body, response.headers)

    except Exception as e:
        print("Error", e)
    finally:
        print("Email job finished...")