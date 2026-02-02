from models.grades_models import GradeResponse, GradeStatisticResponse, MIN_GRADE, MAX_GRADE


class TestGetGradesHighLevel:
    """Высокоуровневые тесты для GET /grades/"""

    def test_get_grades_returns_list_of_grade_models(self, grades_service):
        """Проверка что сервис возвращает список GradeResponse моделей"""
        grades = grades_service.get_grades()

        assert isinstance(grades, list), f"Expected list, got {type(grades)}"
        for grade in grades:
            assert isinstance(grade, GradeResponse), f"Expected GradeResponse, got {type(grade)}"

    def test_grade_values_within_valid_range(self, grades_service):
        """Проверка что все оценки в допустимом диапазоне"""
        grades = grades_service.get_grades()

        for grade in grades:
            assert MIN_GRADE <= grade.grade <= MAX_GRADE, (
                f"Grade {grade.grade} is out of range [{MIN_GRADE}, {MAX_GRADE}]"
            )


class TestGetGradesStatsHighLevel:
    """Высокоуровневые тесты для GET /grades/stats/"""

    def test_get_grades_stats_returns_statistic_model(self, grades_service):
        """Проверка что сервис возвращает GradeStatisticResponse модель"""
        stats = grades_service.get_grades_stats()

        assert isinstance(stats, GradeStatisticResponse), (
            f"Expected GradeStatisticResponse, got {type(stats)}"
        )

    def test_stats_min_max_avg_are_none_when_no_grades(self, grades_service):
        """Проверка что при count=0 статистика содержит None"""
        stats = grades_service.get_grades_stats()

        if stats.count == 0:
            assert stats.min is None, f"Expected min=None when count=0, got {stats.min}"
            assert stats.max is None, f"Expected max=None when count=0, got {stats.max}"
            assert stats.avg is None, f"Expected avg=None when count=0, got {stats.avg}"

    def test_stats_values_are_valid_when_grades_exist(self, grades_service):
        """Проверка корректности статистики при наличии оценок"""
        stats = grades_service.get_grades_stats()

        if stats.count > 0:
            assert stats.min is not None, "min should not be None when count > 0"
            assert stats.max is not None, "max should not be None when count > 0"
            assert stats.avg is not None, "avg should not be None when count > 0"

            assert stats.min <= stats.avg <= stats.max, (
                f"Invalid stats: min={stats.min}, avg={stats.avg}, max={stats.max}"
            )

            assert MIN_GRADE <= stats.min <= MAX_GRADE, (
                f"min={stats.min} is out of range [{MIN_GRADE}, {MAX_GRADE}]"
            )
            assert MIN_GRADE <= stats.max <= MAX_GRADE, (
                f"max={stats.max} is out of range [{MIN_GRADE}, {MAX_GRADE}]"
            )

    def test_stats_calculation_matches_actual_grades(self, grades_service):
        """Проверка что статистика соответствует реальным данным"""
        grades = grades_service.get_grades()
        stats = grades_service.get_grades_stats()

        assert stats.count == len(grades), (
            f"stats.count={stats.count} != len(grades)={len(grades)}"
        )

        if len(grades) > 0:
            grade_values = [g.grade for g in grades]
            expected_min = min(grade_values)
            expected_max = max(grade_values)
            expected_avg = sum(grade_values) / len(grade_values)

            assert stats.min == expected_min, (
                f"stats.min={stats.min} != expected={expected_min}"
            )
            assert stats.max == expected_max, (
                f"stats.max={stats.max} != expected={expected_max}"
            )
            assert abs(stats.avg - expected_avg) < 0.01, (
                f"stats.avg={stats.avg} != expected={expected_avg}"
            )