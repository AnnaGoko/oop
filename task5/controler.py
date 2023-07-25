def run(self):
    while True:
        command = input('Enter command (ADD, REMOVE, GET_ALL, SORT, EXIT): ')
        if command == 'ADD':
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            age = int(input('Enter age: '))
            student = Student(first_name, last_name, age)
            self.add(student)
        elif command == 'REMOVE':
            student_id = int(input('Enter student id: '))
            success = self.model.remove(student_id)
            if success:
                print(f'Student with id {student_id} has been removed.')
            else:
                print(f'Student with id {student_id} does not exist.')
        elif command == 'GET_ALL':
            data = self.get_all()
            self.view.display(data)
        elif command == 'SORT':
            self.sort()
        elif command == 'EXIT':
            break
        else:
            print('Invalid command.')