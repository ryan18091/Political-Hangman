import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from os import environ
# from boto.s3.connection import S3Connection
# import os
#
# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])


# from gitignore import *



def PH_Email():
    print('PH_EMAIL')

    # email_user = 'ryanerickson74@gmail.com'
    # email_password = 'erickson74'
    # email_send = 'ryanerickson74@gmail.com'
    # subject = '-PH REPORT-.'
    user = (environ.get('EMAIL_USER'))
    password = (environ.get('EMAIL_PASSWORD'))
    send = (environ.get('EMAIL_SEND'))

    email_user = user
    email_password = password
    email_send = send
    subject = '-PH REPORT-.'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Daily Test Report'
    msg.attach(MIMEText(body,'plain'))

    filename='ReportSpreadsheet.xlsx'
    attachment = open(filename, 'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()

    #initializes a secure connection to the gmail server
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

