from helpers.auth_helper import AuthHelper
from models.auth_models import RegisterRequest, LoginRequest, LoginResponse
from utils.api_utils import ApiUtils


class AuthService:
    """Сервис для работы c авторизацией (высокоуровневый)"""

    def __init__(self, api_utils: ApiUtils):
        self.helper = AuthHelper(api_utils)

    def register(self, request: RegisterRequest) -> int:
        """Регистрация пользователя"""
        response = self.helper.post_register(request.model_dump())
        return response.status_code

    def login(self, request: LoginRequest) -> LoginResponse:
        """Авторизация пользователя"""
        response = self.helper.post_login(request.model_dump())
        response.raise_for_status()
        return LoginResponse.model_validate(response.json())