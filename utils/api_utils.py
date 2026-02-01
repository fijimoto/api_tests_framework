import requests
import curlify
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class ApiUtils:
    """Базовый класс для работы c API. Управляет сессией и централизованными настройками запросов"""

    def __init__(self, base_url: str, headers: Optional[dict] = None):
        self.base_url = base_url
        self.session = requests.Session()

        if headers:
            self.session.headers.update(headers)

    def get(self, endpoint: str, params: Optional[dict] = None) -> requests.Response:
        """GET-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        self._log_request_response(response)
        return response

    def post(self, endpoint: str, data: Optional[dict] = None) -> requests.Response:
        """POST-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data)
        self._log_request_response(response)
        return response

    def put(self, endpoint: str, data: Optional[dict] = None) -> requests.Response:
        """PUT-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data)
        self._log_request_response(response)
        return response

    def delete(self, endpoint: str) -> requests.Response:
        """DELETE-запрос"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url)
        self._log_request_response(response)
        return response

    def _log_request_response(self, response: requests.Response) -> None:
        """Логирование запроса и ответа"""
        curl_command = curlify.to_curl(response.request)
        logger.info(f"Request: {curl_command}")

        logger.info(f"Status: {response.status_code} | Time: {response.elapsed.total_seconds()}s")

        try:
            logger.info(f"Response body:\n{response.json()}")
        except requests.exceptions.JSONDecodeError:
            logger.info(f"Response body:\n{response.text}")