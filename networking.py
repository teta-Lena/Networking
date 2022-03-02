import smtplib
sender = "tetalenaa@gmail.com"
receiver = "tetalenaa@gmail.com"

message = """From: From Person <tetalenaa@gmail.com>
To:To Person <tetalenaa@gmail.com"
Subject: Networking Assignment
This is my assignment.My name is Ishimwe Teta Lena
 You can view my code on Github at https://github.com/teta-Lena/Networking.git
 
"""
try:
    smtpObj = smtplib.SMTP("smtp.gmail.com",587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.sendmail(sender,receiver,message)
    print("Successfully sent mail")
except smtplib.SMTPException:
    print("Error unable to send mail")
