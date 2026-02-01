import pytest
from faker import Faker
from configs.config import AUTH_URL, UNIVERSITY_URL
from utils.api_utils import ApiUtils
from helpers.auth_helper import AuthHelper
from helpers.grades_helper import GradesHelper
from services.auth_service import AuthService
from services.grades_service import GradesService
from models.auth_models import RegisterRequest, LoginRequest

fake = Faker()


# ============== API Utils фикстуры ==============

@pytest.fixture
def auth_api_utils() -> ApiUtils:
    """ApiUtils для auth-service без авторизации"""
    return ApiUtils(AUTH_URL)


@pytest.fixture
def university_api_utils_unauthorized() -> ApiUtils:
    """ApiUtils для university-service без авторизации"""
    return ApiUtils(UNIVERSITY_URL)


# ============== Генерация тестовых данных ==============

@pytest.fixture
def random_user_data() -> dict:
    """Генерация случайных данных пользователя"""
    password = f"!Test1{fake.word()}"
    return {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": password,
        "password_repeat": password
    }


# ============== Фикстура для получения токена ==============

@pytest.fixture
def access_token(auth_api_utils: ApiUtils, random_user_data: dict) -> str:
    """
    Регистрирует нового пользователя, логинится и возвращает access_token.
    Используется для авторизованных запросов.
    """
    auth_helper = AuthHelper(auth_api_utils)

    register_response = auth_helper.post_register(random_user_data)
    assert register_response.status_code == 201, f"Registration failed: {register_response.text}"

    login_data = {
        "username": random_user_data["username"],
        "password": random_user_data["password"]
    }
    login_response = auth_helper.post_login(login_data)
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"

    return login_response.json()["access_token"]


# ============== Авторизованные API Utils ==============

@pytest.fixture
def university_api_utils(access_token: str) -> ApiUtils:
    """ApiUtils для university-service с авторизацией"""
    return ApiUtils(
        UNIVERSITY_URL,
        headers={"Authorization": f"Bearer {access_token}"}
    )


# ============== Helpers ==============

@pytest.fixture
def auth_helper(auth_api_utils: ApiUtils) -> AuthHelper:
    """AuthHelper без авторизации"""
    return AuthHelper(auth_api_utils)


@pytest.fixture
def grades_helper(university_api_utils: ApiUtils) -> GradesHelper:
    """GradesHelper с авторизацией"""
    return GradesHelper(university_api_utils)


# ============== Services ==============

@pytest.fixture
def auth_service(auth_api_utils: ApiUtils) -> AuthService:
    """AuthService для высокоуровневых тестов"""
    return AuthService(auth_api_utils)


@pytest.fixture
def grades_service(university_api_utils: ApiUtils) -> GradesService:
    """GradesService для высокоуровневых тестов"""
    return GradesService(university_api_utils)