from typing import Optional
from pydantic import BaseModel, Field


class GradeResponse(BaseModel):
    """Модель одной оценки"""
    id: int
    teacher_id: int
    student_id: int
    grade: int = Field(ge=0, le=5)


class GradeStatisticResponse(BaseModel):
    """Модель статистики оценок"""
    count: int = Field(ge=0)
    min: Optional[int] = None
    max: Optional[int] = None
    avg: Optional[float] = None