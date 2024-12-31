import csv, smtplib, ssl
from datetime import  date

from pyexpat.errors import messages


def send_email(form_address, password, to_address, message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as server:
        server.login(form_address,password)
        server.sendmail(form_address, to_address, message)

def main():
    today = date.today().strftime("%B %d %Y")
    message = "'Subject: Your Evaluation Hi {name}, the date your Q1 evaluation is {date} Your Score is {score}'"
    from_address = ""
    password = ""
    with open("Student.csv") as file:
        reader = csv.reader(file)
        for name, email, score in reader:
            send_email(from_address,password,email,message.format(name = name, date = today, score = score))
            if send_email:
                print("Email send for " + name)
            else:
                print("Email not sent for : " + name )

if __name__ == "__main__":
    main()

