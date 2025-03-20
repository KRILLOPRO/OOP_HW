class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        return f'{super().__str__()}\nСредняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def rate_lecturer(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


def average_student_grade(students, course):
    grades = [sum(st.grades.get(course, [])) / len(st.grades.get(course, [1])) for st in students if
              course in st.grades]
    return round(sum(grades) / len(grades), 1) if grades else 0


def average_lecturer_grade(lecturers, course):
    grades = [sum(lec.grades.get(course, [])) / len(lec.grades.get(course, [1])) for lec in lecturers if
              course in lec.grades]
    return round(sum(grades) / len(grades), 1) if grades else 0


student1 = Student('Ruoy', 'Eman', 'Male')
student2 = Student('Alice', 'Wonder', 'Female')
lecturer1 = Lecturer('John', 'Smith')
lecturer2 = Lecturer('Mary', 'Poppins')
reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Another', 'Person')


student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python', 'Git']
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Git']


reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 10)

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Git', 8)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)


print(f'Средняя оценка за Python среди студентов: {average_student_grade([student1, student2], "Python")}')
print(f'Средняя оценка за Git среди студентов: {average_student_grade([student1, student2], "Git")}')
print(f'Средняя оценка за Python среди лекторов: {average_lecturer_grade([lecturer1, lecturer2], "Python")}')
print(f'Средняя оценка за Git среди лекторов: {average_lecturer_grade([lecturer1, lecturer2], "Git")}')
