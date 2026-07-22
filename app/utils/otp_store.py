otp_storage = {}

def save_otp(email, otp):
    otp_storage[email] = otp


def verify_otp(email, otp):
    if email in otp_storage and otp_storage[email] == otp:
        return True
    return False