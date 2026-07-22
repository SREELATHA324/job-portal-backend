from app.utils.email_sender import generate_otp, send_otp

otp = generate_otp()

print("Generated OTP:", otp)

send_otp("sreelathapachcha225@gmail.com", otp)