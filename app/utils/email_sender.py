import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp(receiver_email, otp):
    if not BREVO_API_KEY:
        raise Exception("BREVO_API_KEY missing")

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "Job Portal",
            "email": "sreelathapachcha225@gmail.com"
        },
        "to": [
            {
                "email": receiver_email
            }
        ],
        "subject": "Password Reset OTP",
        "textContent": f"""Hello,

Your OTP is: {otp}

Use this OTP to reset your password.

Thank You."""
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)

    print("Brevo Response:", response.status_code, response.text)

    if response.status_code not in [200, 201]:
        raise Exception(f"Brevo Error: {response.text}")

    return True