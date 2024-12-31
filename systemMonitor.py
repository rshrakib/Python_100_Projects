import psutil
import smtplib
from email.mime.text import MIMEText

sender_email = ""
receiver_email = ""
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = ""
smtp_password = ""

def send_alert(subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(smtp_username,smtp_password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        server.quit()
        print("Alert email send successfully")

    except Exception as e:
        print(f"Failed to send email alart: {e}")


def monitor_system():
    try:
        cpu_threshold = 80
        memory_threshold = 80

        cpu_usage = psutil.cpu_percent(interval=1)
        print(cpu_usage)
        memory_usage = psutil.virtual_memory().percent
        print(memory_usage)

        if cpu_usage > cpu_threshold:
            send_alert("High CPU usages", f"CPU usages is {cpu_usage}")
        if memory_usage > memory_threshold:
            send_alert("High Memory usages", f"Memory usages is {memory_usage}")

    except Exception as e:
        print(f"An error occurred. The error: {e}")


while True:
    monitor_system()
