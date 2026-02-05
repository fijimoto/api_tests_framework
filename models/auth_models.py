from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    """Модель запроса на регистрацию"""
    username: str
    password: str
    password_repeat: str
    email: EmailStr


class LoginRequest(BaseModel):
    """Модель запроса на авторизацию"""
    username: str
    password: str


class LoginResponse(BaseModel):
    """Модель ответа при успешной авторизации"""
    access_token: str
    token_type: str
