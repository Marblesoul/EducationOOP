class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_someone(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        if self.grades.values():
            return sum(list(self.grades.values())[0]) / len(list(self.grades.values())[0])
        else:
            return "Нет оценок"

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.get_average_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def get_average_grade(self):
        if self.lecture_grades.values():
            return sum(list(self.lecture_grades.values())[0]) / len(list(self.lecture_grades.values())[0])
        else:
            return "Нет оценок"

    def __eq__(self, student):
        return self.get_average_grade() == student.get_average_grade()

    def __str__(self):
        res = f'Имя: {self._name}\n' \
              f'Фамилия: {self._surname}\n' \
              f'Средняя оценка за лекции: {self.get_average_grade()}\n'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_someone(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self._name}\n' \
              f'Фамилия: {self._surname}'
        return res

student_1 = Student('Tom', 'Hanks', 'Male')
student_2 = Student('Salma', 'Hayek', 'Female')

student_1.courses_in_progress += ['Python', 'C++']
student_1.finished_courses += ['Java']
student_2.courses_in_progress += ['Python']

lecturer_1 = Lecturer('Vin', 'Diesel')
lecturer_2 = Lecturer('Benny', 'Black')

lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Python']

reviewer_1 = Reviewer('Martin', 'Stevenson')
reviewer_2 = Reviewer('Garry', 'Kasparov')

reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_someone(student_1, 'Python', 9)
reviewer_1.rate_someone(student_1, 'Python', 10)
reviewer_1.rate_someone(student_2, 'Python', 8)
reviewer_2.rate_someone(student_2, 'Python', 7)

student_1.rate_someone(lecturer_1, 'Python', 10)
student_1.rate_someone(lecturer_1, 'Python', 9)
student_2.rate_someone(lecturer_2, 'Python', 8)
student_2.rate_someone(lecturer_2, 'Python', 9)

def average_students_grade(students, course) -> float:
    average_value = [student.get_average_grade() for student in students if course in student.grades]
    return sum(average_value) / len(students)

def average_lecturers_grade(lecturers, course) -> float:
    average_value = [lecturer.get_average_grade() for lecturer in lecturers if course in lecturer.lecture_grades]
    return sum(average_value) / len(lecturers)

# Вывод всех экземпляров классов
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

# Вывод средней оценки по студентам и курсу
print(average_students_grade([student_1, student_2], 'Python'))

#Вывод средней оценки по лекторам и курсу
print(average_lecturers_grade([lecturer_1, lecturer_2], 'Python'))