Класс ViewEng:

python
from iGetView import iGetView

class ViewEng(iGetView):
    def display(self, data):
        print('List of students:')
        for student in data:
            print(f'{student.get_last_name()}, {student.get_first_name()} ({student.get_age()})')