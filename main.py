class Student:
    def __init__(self, name, surname, gender):
        self._name = name
        self._surname = surname
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
        avg = 0
        for grade in self.grades.values():
            avg += sum(grade)
        return avg / len(self.grades)

    def __str__(self):
        res = f'Имя: {self._name}\n' \
              f'Фамилия: {self._surname}\n' \
              f'Средняя оценка за домашние задания: {self.get_average_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
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
        avg = 0
        for grade in self.lecture_grades.values():
            avg += sum(grade)
        return avg / len(self.lecture_grades)

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