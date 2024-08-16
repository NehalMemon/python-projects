import random
import smtplib
import pandas as pd
from datetime import datetime
from pathlib import Path

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "nehalmemon73@gmail.com"
GMAIL_PASSWORD = "ouaa uwtg jgpn nnay"

def send_email(to_address, subject, message):

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(GMAIL_USER, to_address, email_message)
        print(f"Successfully sent email to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

def check_and_send_quotes():
    today = datetime.today()
    day = today.strftime("%A")

    gmails = pd.read_csv(Path("gmails.csv"))
    quotes = pd.read_csv(Path("quotes.csv"))

    if day == "Monday":
        for index, row in gmails.iterrows():
            email = row["gmails"]
            subject = "Motivated week is a strong week"
            random_quote = random.choice(quotes['quote'])
            message = f"Dear User,\n\n{random_quote}"
            send_email(email, subject, message)

if __name__ == "__main__":
    check_and_send_quotes()
