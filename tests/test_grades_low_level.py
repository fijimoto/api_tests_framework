class TestGetGradesLowLevel:
    """Низкоуровневые тесты для GET /grades/"""

    def test_get_grades_returns_200(self, grades_helper):
        """Проверка что endpoint возвращает 200 OK"""
        response = grades_helper.get_grades()

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}. Body: {response.text}"
        )

    def test_get_grades_returns_list(self, grades_helper):
        """Проверка что endpoint возвращает список"""
        response = grades_helper.get_grades()

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}. Body: {response.text}"
        )
        assert isinstance(response.json(), list), (
            f"Expected list, got {type(response.json())}"
        )

    def test_get_grades_without_auth_returns_403(self, university_api_utils_unauthorized):
        """Проверка что без авторизации возвращается 403"""
        from helpers.grades_helper import GradesHelper

        helper = GradesHelper(university_api_utils_unauthorized)
        response = helper.get_grades()

        assert response.status_code == 403, (
            f"Expected 403, got {response.status_code}. Body: {response.text}"
        )


class TestGetGradesStatsLowLevel:
    """Низкоуровневые тесты для GET /grades/stats/"""

    def test_get_grades_stats_returns_200(self, grades_helper):
        """Проверка что endpoint возвращает 200 OK"""
        response = grades_helper.get_grades_stats()

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}. Body: {response.text}"
        )

    def test_get_grades_stats_response_structure(self, grades_helper):
        """Проверка структуры ответа статистики"""
        response = grades_helper.get_grades_stats()

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}. Body: {response.text}"
        )

        data = response.json()
        assert "count" in data, f"Missing 'count' in response: {data}"
        assert "min" in data, f"Missing 'min' in response: {data}"
        assert "max" in data, f"Missing 'max' in response: {data}"
        assert "avg" in data, f"Missing 'avg' in response: {data}"

    def test_get_grades_stats_count_is_non_negative(self, grades_helper):
        """Проверка что count >= 0"""
        response = grades_helper.get_grades_stats()

        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}. Body: {response.text}"
        )

        count = response.json()["count"]
        assert count >= 0, f"Expected count >= 0, got {count}"

    def test_get_grades_stats_without_auth_returns_403(self, university_api_utils_unauthorized):
        """Проверка что без авторизации возвращается 403"""
        from helpers.grades_helper import GradesHelper

        helper = GradesHelper(university_api_utils_unauthorized)
        response = helper.get_grades_stats()

        assert response.status_code == 403, (
            f"Expected 403, got {response.status_code}. Body: {response.text}"
        )
