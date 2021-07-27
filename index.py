###
# This program is designed for sending emails to YIG Clients and Operaters. Built and managed by Yeetum Technologies. 
###

import initservice
import prepEmail
import htmlify
import sendEmail
import schedule

from pathlib import Path
import schedule
import time


if __name__ == "__main__":
    try:
        
        FILEPATH, USER_SMTP, PASSWORD_SMTP, SENDER, SENDERNAME, RECEPIENT_FILE, SUBJECT, SMTP_SERVER, SMTP_PORT = initservice.init_atlas_email_services()

        MARKET_STRENGTH_FILEPATH = Path('./stock_reports/csvfiles_market-strength-stocks.2021-07-14.csv')
        SECTOR_REPORT_FILEPATH = Path('./stock_reports/csvfiles_sector-strength-stocks.2021-07-14.csv')
        STOCK_SIGNAL_FILEPATH = Path('./stock_reports/csvfiles_stocks.2021-07-14.signals.csv')
        #schedule.every().day.at("17:00").do(job)

        if FILEPATH.suffix == ".csv":
            print('CSV filepath, htmlify executing...')

            #html = htmlify.standard_csv(FILEPATH, SUBJECT)
            html = htmlify.stock_reports(MARKET_STRENGTH_FILEPATH, SECTOR_REPORT_FILEPATH, STOCK_SIGNAL_FILEPATH, SUBJECT)

            message = prepEmail.prep_SMTPemail_body(FILEPATH, SENDER, SUBJECT, html)
            sendEmail.send_smtp_email(SMTP_SERVER, SMTP_PORT, USER_SMTP, PASSWORD_SMTP,RECEPIENT_FILE, SENDER, message)
            

            ### SendGrid prep + send
            #sg_message = prepEmail.prep_sg_email(FILEPATH, SENDER, RECEPIENT_FILE, SUBJECT, html)
            #sendEmail.send_sg_email(sg_message)

        else:
            print('filepath not htmlified')
            FILEPATH = FILEPATH
            message = prepEmail.prep_SMTPemail_body(FILEPATH, SENDER, SUBJECT)
            sendEmail.send_smtp_email(SMTP_SERVER, SMTP_PORT, USER_SMTP, PASSWORD_SMTP,RECEPIENT_FILE, SENDER, message)


        #while True:
        #    schedule.run_pending()
        #    time.sleep(1)

    


    except Exception as e:
        print("Error", e)
    finally:
        print("Email job finished...")