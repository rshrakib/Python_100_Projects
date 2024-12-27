import smtplib
import schedule
import time

def send_mail():
    sender = ""
    receiver = ""
    password = ""

    subject = ""
    body = ""

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,message)
        print("Email Sent!")
# schedule.every(1).minute.do(send_mail())
schedule.every().day.at("08.00").do(send_mail())

while True:
    schedule.run_pending()
    time.sleep(10)