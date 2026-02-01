from models.grades_models import GradeResponse, GradeStatisticResponse


class TestGetGradesHighLevel:
    """Высокоуровневые тесты для GET /grades/"""

    def test_get_grades_returns_list_of_grade_models(self, grades_service):
        """Проверка что сервис возвращает список GradeResponse моделей"""
        grades = grades_service.get_grades()

        assert isinstance(grades, list)
        for grade in grades:
            assert isinstance(grade, GradeResponse)

    def test_get_grades_model_has_required_fields(self, grades_service):
        """Проверка что модель оценки содержит все обязательные поля"""
        grades = grades_service.get_grades()

        for grade in grades:
            assert hasattr(grade, "id")
            assert hasattr(grade, "teacher_id")
            assert hasattr(grade, "student_id")
            assert hasattr(grade, "grade")


class TestGetGradesStatsHighLevel:
    """Высокоуровневые тесты для GET /grades/stats/"""

    def test_get_grades_stats_returns_statistic_model(self, grades_service):
        """Проверка что сервис возвращает GradeStatisticResponse модель"""
        stats = grades_service.get_grades_stats()

        assert isinstance(stats, GradeStatisticResponse)

    def test_get_grades_stats_count_is_integer(self, grades_service):
        """Проверка что count это целое число"""
        stats = grades_service.get_grades_stats()

        assert isinstance(stats.count, int)
        assert stats.count >= 0

    def test_get_grades_stats_empty_database_returns_nulls(self, grades_service):
        """
        Проверка что при пустой базе min/max/avg = None.
        Примечание: тест может не пройти если в базе есть данные.
        """
        stats = grades_service.get_grades_stats()

        if stats.count == 0:
            assert stats.min is None
            assert stats.max is None
            assert stats.avg is None

    def test_get_grades_stats_with_data_returns_valid_statistics(self, grades_service):
        """Проверка что при наличии данных статистика валидна"""
        stats = grades_service.get_grades_stats()

        if stats.count > 0:
            assert stats.min is not None
            assert stats.max is not None
            assert stats.avg is not None
            assert stats.min <= stats.max
            assert stats.min <= stats.avg <= stats.max