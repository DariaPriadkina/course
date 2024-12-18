class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Human:{self.first_name} {self.last_name}\nAge:{self.age}\nGender:{self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f'\nRecord book:{self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise ValueError("The group already has 10 students!")

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.discard(student)

    def find_student(self, last_name):
        res = None
        for student in self.group:
            if student.last_name == last_name:
                res = student
                break
        return res

    def __str__(self):
        all_students = '\n'.join(student.first_name for student in self.group)

        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

st3 = Student('Female', 21, 'Angela', 'Wilson', 'F456')
st4 = Student('Male', 25, 'Roman', 'Taylor', 'A348')
st5 = Student('Female', 22, 'Sophia', 'Richie', 'D789')
st6 = Student('Male', 23, 'Luke', 'More', 'B123')
st7 = Student('Female', 24, 'Hailey', 'Smith', 'C345')
st8 = Student('Male', 26, 'Lucas', 'Brown', 'H321')
st9 = Student('Female', 28, 'Olivia', 'Jackson', 'K593')
st10 = Student('Male', 29, 'Mark', 'Hemsworth', 'J675')
st11 = Student('Female', 27, 'Demi', 'Moore', 'L907')
st12 = Student('Male', 23, 'John', 'Johnson', 'L654')
list_st = (st3, st4, st5, st6, st7, st8, st9, st10, st11)

for st in list_st:
    gr.add_student(st)

try:
    gr.add_student(st12)
except ValueError as e:
    print(e)