import smtplib
import datetime
from datetime import datetime
import sensitive

def sendmail():
    try:
        logfile = open("stocklog.txt", "a")
    except:
        logfile = open("stocklog.txt", "w")

    now = datetime.now()
    current_datetime = now.strftime("%d/%m/%Y %H:%M:%S")

    action = "Buy"
    money = "1000"

    try:
        mail = smtplib.SMTP(host="smtp.gmail.com",port=587)

        mail.ehlo()

        mail.starttls()

        mail.login(user=sensitive.sender, password=sensitive.password)

        for i in range(len(sensitive.recievers)):
            content = """From: """+sensitive.sender+""" <"""+sensitive.sender+"""@gmail.com>
            To: """+sensitive.recievers[i]+""" <"""+sensitive.recievers[i]+"""@gmail.com>
            Subject: Tesla Stock Alert
            Alert: """+action+"""
            Current Portfolio: $"""+money+"""
            Time: """+current_datetime+"""
            """
            mail.sendmail(sensitive.sender, sensitive.recievers[i], content)

        mail.quit()

        print("Successful Alert at "+current_datetime)
        logfile.write("Sent "+action+" Alert at "+current_datetime+"\n")

    except:
        print("Unsuccessful Alert at "+current_datetime)
        logfile.write("Failed to send "+action+" Alert at "+current_datetime+"\n")

    logfile.close()
