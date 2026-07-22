import os
import random
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp(receiver_email, otp):

    if not EMAIL or not EMAIL_PASSWORD:
        raise Exception("EMAIL or EMAIL_PASSWORD missing in .env")

    print("Sending mail from:", EMAIL)
    print("Password length:", len(EMAIL_PASSWORD))

    msg = EmailMessage()

    msg["Subject"] = "Password Reset OTP"
    msg["From"] = EMAIL
    msg["To"] = receiver_email

    msg.set_content(
        f"""
Hello,

Your OTP is: {otp}

Use this OTP to reset your password.

Thank You.
"""
    )

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(
            EMAIL.strip(),
            EMAIL_PASSWORD.strip()
        )

        server.send_message(msg)

        server.quit()

        print("OTP Sent Successfully")

        return True

    except Exception as e:
        print("SMTP ERROR:", e)
        raise Exception(str(e))