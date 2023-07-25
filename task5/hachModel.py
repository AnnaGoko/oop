from typing import Dict
from iGetModel import iGetModel
from Student import Student

class hachModel(iGetModel):
    def __init__(self):
        self.students = {}

    def add(self, student: Student):
        self.students[student.get_id()] = student

    def remove(self, student_id: int):
        if student_id in self.students:
            del self.students[student_id]
            return True
        else:
            return False

    def get_all(self) -> Dict[int, Student]:
        return self.students