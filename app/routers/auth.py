from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google.oauth2 import id_token
from google.auth.transport import requests

from app.schemas.user import (
    UserRegister,
    LoginRequest,
    ForgotPasswordRequest,
    VerifyOTPRequest,
    ResetPasswordRequest
)

from app.auth.jwt_handler import create_access_token
from app.utils.email_sender import generate_otp, send_otp

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

users = []
otp_store = {}
class GoogleLoginRequest(BaseModel):
    token: str


@router.post("/register")
def register(user: UserRegister):

    users.append(user)

    token = create_access_token({
        "sub": user.email
    })

    return {
        "message": "User Registered Successfully",
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/google-login")
def google_login(data: GoogleLoginRequest):

    try:
        google_user = id_token.verify_oauth2_token(
            data.token,
            requests.Request(),
            "536124478145-pjfn02pnl37peve988396botj8sogqkr.apps.googleusercontent.com"
        )

        email = google_user.get("email")
        name = google_user.get("name")

        # Existing user check
        existing_user = None

        for u in users:
            if u.email.lower() == email.lower():
                existing_user = u
                break

        # New Google user create
        if not existing_user:
            from app.schemas.user import UserRegister

            new_user = UserRegister(
                name=name,
                email=email,
                password="google_login"
            )

            users.append(new_user)

        token = create_access_token({
            "sub": email
        })

        return {
            "message": "Google Login Successful",
            "access_token": token,
            "token_type": "bearer",
            "user": {
                "name": name,
                "email": email,
                "role": "user"
            }
        }

    except Exception as e:
        print("GOOGLE ERROR:", e)
        raise HTTPException(
            status_code=400,
            detail="Invalid Google Token"
        )


@router.post("/login")
def login(user: LoginRequest):

    for u in users:
        if u.email.lower() == user.email.lower() and u.password == user.password:

            token = create_access_token({
                "sub": user.email
            })

            return {
                "message": "Login Successful",
                "access_token": token,
                "token_type": "bearer"
            }

    raise HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )

@router.post("/forgot-password")
def forgot_password(payload: ForgotPasswordRequest):
    print("FORGOT PASSWORD API HIT")

    email = payload.email

    user_found = False

    for u in users:
        if u.email.lower() == email.lower():
            user_found = True
            break

    if not user_found:
        raise HTTPException(
            status_code=404,
            detail="Email not found"
        )

    otp = generate_otp()

    print("Email:", email)
    print("Users:", users)
    print("OTP:", otp)

    otp_store[email] = otp

    try:
        send_otp(email, otp)
    except Exception as e:
        print("EMAIL ERROR:", e)
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    return {
        "message": "OTP sent successfully to your Gmail"
    }

@router.post("/verify-otp")
def verify_otp(payload: VerifyOTPRequest):

    email = payload.email
    otp = payload.otp

    if email not in otp_store:
        raise HTTPException(
            status_code=400,
            detail="OTP not found"
        )

    if otp_store[email] != otp:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP"
        )

    return {
        "message": "OTP verified successfully"
    }

@router.post("/reset-password")
def reset_password(payload: ResetPasswordRequest):

    email = payload.email
    new_password = payload.new_password

    for u in users:
        if u.email.lower() == email.lower():
            u.password = new_password

            if email in otp_store:
                del otp_store[email]

            return {
                "message": "Password reset successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )