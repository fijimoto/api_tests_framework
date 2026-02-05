from utils.api_utils import ApiUtils
from requests import Response


class AuthHelper:
    """Helper для работы с Authentication контроллером"""

    REGISTER_ENDPOINT = "/auth/register/"
    LOGIN_ENDPOINT = "/auth/login/"
    ME_ENDPOINT = "/users/me/"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_register(self, data: dict) -> Response:
        """Регистрация пользователя"""
        return self.api_utils.post(self.REGISTER_ENDPOINT, data=data)

    def post_login(self, data: dict) -> Response:
        """Авторизация пользователя"""
        return self.api_utils.post(self.LOGIN_ENDPOINT, data=data)

    def get_me(self) -> Response:
        """Получение информации о текущем пользователе"""
        return self.api_utils.get(self.ME_ENDPOINT)
