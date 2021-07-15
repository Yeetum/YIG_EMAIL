import sys
from pathlib import Path
import argparse


# Import config variables
import config

def init_atlas_email_services():

    parser = argparse.ArgumentParser()

    # Add positional args
    parser.add_argument("filepath", help="default filepath", type=Path)
    parser.add_argument("recepients", help="email recepients file")
    parser.add_argument("subject", help="email subject")

    # Add optional args
    parser.add_argument("-stocks", "--stock-report", nargs="+", help="Stock Report Files", type=Path)

    args = parser.parse_args()
    print(args)

    # Return init variables
    DEFAULT_FILEPATH = args.filepath
    USER_SMTP = config.USER_SMTP
    PASSWORD_SMTP = config.PASSWORD_SMTP
    SENDER = config.SENDER
    SENDERNAME = config.SENDERNAME

    RECEPIENT_FILE = args.recepients
    SUBJECT = args.subject

    SMTP_SERVER = config.SMTP_SERVER
    SMTP_PORT = config.SMTP_PORT

    
    FILEPATH = DEFAULT_FILEPATH

    print('SUBJECT: ', SUBJECT)
    print('RECEPIENTS: ', RECEPIENT_FILE)
    print('FILETYPE:', FILEPATH.suffix)

    if not FILEPATH.exists():
        print("Oops, file doesn't exist!")
        raise ValueError('Filepath does not exist...')
    else:
        print("File located...")

    

    return FILEPATH, USER_SMTP, PASSWORD_SMTP, SENDER, SENDERNAME, RECEPIENT_FILE, SUBJECT, SMTP_SERVER, SMTP_PORT