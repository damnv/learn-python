from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name: str
    class_room: str
    description: Optional[str]
    maths: float = 0
    literature: float = 0
    english: float = 0


class Student_GPA(BaseModel):
    class_room: Optional[str]
