import smtplib
import base64

sender = 'scorpioncarr1@gmail.com'
receivers = 'scorpioncarr1@gmail.com'

filename = "/Users/nathanael/Google Drive/ProgramDatabase/Python_SignIn/StudentCheckin_2017-07-16.txt"

fileopen = open(filename, "r")

message = """From: Nathanael Carr <scorpioncarr1@gmail.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: e-mail test

Nathanael,

<br>This is an e-mail message to be sent in HTML format

<br>This is HTML message.
<h1>This is headline.</h1>
<br><br>
%s
""" % (fileopen.read())

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587, 'localhost')
    smtpObj.starttls()
    smtpObj.login(sender, "gcoolguye")

    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")

except smtplib.SMTPAuthenticationError:
    print("Error: unable to send email")
