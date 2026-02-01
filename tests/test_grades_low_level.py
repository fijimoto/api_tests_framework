"""
Низкоуровневые тесты для /grades/ и /grades/stats/
Тесты работают напрямую с Helper, проверяют сырой Response.
"""


class TestGetGradesLowLevel:
    """Низкоуровневые тесты для GET /grades/"""

    def test_get_grades_returns_200(self, grades_helper):
        """Проверка что endpoint возвращает 200 OK"""
        response = grades_helper.get_grades()

        assert response.status_code == 200

    def test_get_grades_returns_list(self, grades_helper):
        """Проверка что endpoint возвращает список"""
        response = grades_helper.get_grades()

        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_grades_without_auth_returns_403(self, university_api_utils_unauthorized):
        """Проверка что без авторизации возвращается 403"""
        from helpers.grades_helper import GradesHelper

        helper = GradesHelper(university_api_utils_unauthorized)
        response = helper.get_grades()

        assert response.status_code == 403


class TestGetGradesStatsLowLevel:
    """Низкоуровневые тесты для GET /grades/stats/"""

    def test_get_grades_stats_returns_200(self, grades_helper):
        """Проверка что endpoint возвращает 200 OK"""
        response = grades_helper.get_grades_stats()

        assert response.status_code == 200

    def test_get_grades_stats_response_structure(self, grades_helper):
        """Проверка структуры ответа статистики"""
        response = grades_helper.get_grades_stats()

        assert response.status_code == 200

        data = response.json()
        assert "count" in data
        assert "min" in data
        assert "max" in data
        assert "avg" in data

    def test_get_grades_stats_count_is_non_negative(self, grades_helper):
        """Проверка что count >= 0"""
        response = grades_helper.get_grades_stats()

        assert response.status_code == 200
        assert response.json()["count"] >= 0

    def test_get_grades_stats_without_auth_returns_403(self, university_api_utils_unauthorized):
        """Проверка что без авторизации возвращается 403"""
        from helpers.grades_helper import GradesHelper

        helper = GradesHelper(university_api_utils_unauthorized)
        response = helper.get_grades_stats()

        assert response.status_code == 403