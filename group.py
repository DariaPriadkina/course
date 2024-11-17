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
