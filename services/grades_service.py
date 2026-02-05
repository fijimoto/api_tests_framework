from typing import Optional, List
from helpers.grades_helper import GradesHelper
from models.grades_models import GradeResponse, GradeStatisticResponse
from utils.api_utils import ApiUtils


class GradesService:
    """Сервис для работы c оценками (высокоуровневый)"""

    def __init__(self, api_utils: ApiUtils):
        self.helper = GradesHelper(api_utils)

    def get_grades(
        self,
        student_id: Optional[int] = None,
        teacher_id: Optional[int] = None,
        group_id: Optional[int] = None
    ) -> List[GradeResponse]:
        """Получение списка оценок"""
        response = self.helper.get_grades(
            student_id=student_id,
            teacher_id=teacher_id,
            group_id=group_id
        )
        response.raise_for_status()
        return [GradeResponse.model_validate(item) for item in response.json()]

    def get_grades_stats(
        self,
        student_id: Optional[int] = None,
        teacher_id: Optional[int] = None,
        group_id: Optional[int] = None
    ) -> GradeStatisticResponse:
        """Получение статистики оценок"""
        response = self.helper.get_grades_stats(
            student_id=student_id,
            teacher_id=teacher_id,
            group_id=group_id
        )
        response.raise_for_status()
        return GradeStatisticResponse.model_validate(response.json())
