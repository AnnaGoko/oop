from typing import List, Dict, TypeVar
from iGetView import iGetView
from iGetModel import iGetModel
from iPersonService import iPersonService
from iPersonController import iPersonController
from Person import Person
from Student import Student
from Teacher import Teacher
from Employee import Employee

T = TypeVar('T', bound=Person)

class PersonComparator:
    @staticmethod
    def get_age(person: Person):
        return person.get_age()

class ViewEng(iGetView):
    def display(self, data):
        print('List of students:')
        for student in data:
            print(f'{student.get_last_name()}, {student.get_first_name()} ({student.get_age()})')

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

class TeacherService(iPersonService[Teacher]):
    def init(self):
        self.teachers = []

    def add(self, teacher: Teacher):
        self.teachers.append(teacher)

    def remove(self, teacher: Teacher):
        self.teachers.remove(teacher)

    def get_all(self) -> List[Teacher]:
        return self.teachers

    def sort(self):
        self.teachers.sort(key=PersonComparator.get_age)

class TeacherController(iPersonController[Teacher]):
    def init(self):
        self.service = TeacherService()

    def add(self, teacher: Teacher):
        self.service.add(teacher)

    def remove(self, teacher: Teacher):
        self.service.remove(teacher)

    def get_all(self) -> List[Teacher]:
        return self.service.get_all()

    def sort(self):
        self.service.sort()

class AverageAge:
    @staticmethod
    def calculate(people: List[T]) -> float:
        total_age = 0
        for person in people:
            total_age += person.get_age()
        return total_age / len(people)

def main():
    model = hachModel()
    view = ViewEng()
    controller = TeacherController(model, view)

    controller.add(Teacher('Bob', 'Smith', 35))
    controller.add(Teacher('Alice', 'Jones', 40))
    controller.add(Student('John', 'Doe', 20))
    controller.add(Student('Jane', 'Doe', 21))

    data = controller.get_all()
    view.display(data)

    print('Average age of teachers:', AverageAge.calculate(controller.get_all()))
    
if __name__ == '__main__':
    main()