from typing import Optional
from utils.api_utils import ApiUtils
from requests import Response


class GradesHelper:
    """Helper для работы c Grades контроллером"""

    GRADES_ENDPOINT = "/grades/"
    GRADES_STATS_ENDPOINT = "/grades/stats/"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def get_grades(
        self,
        student_id: Optional[int] = None,
        teacher_id: Optional[int] = None,
        group_id: Optional[int] = None
    ) -> Response:
        """Получение списка оценок c опциональными фильтрами"""
        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id

        return self.api_utils.get(self.GRADES_ENDPOINT, params=params if params else None)

    def get_grades_stats(
        self,
        student_id: Optional[int] = None,
        teacher_id: Optional[int] = None,
        group_id: Optional[int] = None
    ) -> Response:
        """Получение статистики оценок c опциональными фильтрами"""
        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id

        return self.api_utils.get(self.GRADES_STATS_ENDPOINT, params=params if params else None)