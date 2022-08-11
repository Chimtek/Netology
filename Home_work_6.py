# ================== Объекты и классы. Инкапсуляция, наследование и полиморфизм ===================================
class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        all_grades_list = sum(list(self.grades.values()), [])
        if all_grades_list:
            average_grade = round(sum(all_grades_list) / len(all_grades_list), 1)
            return average_grade
        return 0

    def get_average_grade_course(self, course):
        if course in self.grades:
            average_grade_course = round(sum(self.grades[course]) / len(self.grades[course]), 1)
            return average_grade_course
        return 0

    def __str__(self):
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.get_average_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''

    def __eq__(self, other):
        if not isinstance(other, Student):
            return f'Справа должен быть Студент'
        return self.get_average_grade() == other.get_average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'Справа должен быть Студент'
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return f'Справа должен быть Студент'
        return self.get_average_grade() > other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lectureres = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.lectureres.append(self)

    def get_average_grade(self):
        all_grades_list = sum(list(self.grades.values()), [])
        if all_grades_list:
            average_grade = round(sum(all_grades_list) / len(all_grades_list), 1)
            return average_grade
        return 0

    def get_average_grade_course(self, course):
        if course in self.grades:
            average_grade_course = round(sum(self.grades[course]) / len(self.grades[course]), 1)
            return average_grade_course
        return 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}\nЧитает курсы: {", ".join(self.courses_attached)}'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return f'Справа должен быть Лектор'
        return self.get_average_grade() == other.get_average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'Справа должен быть Лектор'
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return f'Справа должен быть Лектор'
        return self.get_average_grade() > other.get_average_grade()


class Reviewer(Mentor):
    revieweres = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        Reviewer.revieweres.append(self)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nПроверяет курсы: {", ".join(self.courses_attached)}'


def get_avarage_grade_course(persons_lst, course):
    average_grade_list = []
    type_lst = ''

    for person in persons_lst:
        if course in person.grades:
            average_grade_list.append(person.get_average_grade_course(course))
    average_grade = round(sum(average_grade_list) / len(average_grade_list), 2)

    if isinstance(persons_lst[0], Student):
        type_lst = 'студентов'
    elif isinstance(persons_lst[0], Lecturer):
        type_lst = 'лекторов'

    print(f"Средняя оценка у {type_lst} за курс {course}: {average_grade}")


# лекторы --------------------------------
lec1 = Lecturer('Дмитрий', 'Менделеев')
lec1.courses_attached += ['Химия'] + ['Технология дистилляции'] + ['Базы данных']

lec2 = Lecturer('Satoshi', 'Nakamoto')
lec2.courses_attached += ['Python'] + ['JS'] + ['Базы данных'] + ['Blockchain']

lec3 = Lecturer('Иван', 'Бездомный')
lec3.courses_attached += ['Python'] + ['Web'] + ['Базы данных']

# студенты ------------------------------
stud1 = Student('Omar', 'Tupak', 'муж')
stud1.courses_in_progress += ['Python'] + ['JS'] + ['Базы данных'] + ['Blockchain'] + ['Web']
stud1.add_courses('Технология дистилляции')
stud1.add_courses('Химия')
stud1.rate_hw(lec1, 'Базы данных', 10)
stud1.rate_hw(lec2, 'Blockchain', 10)
stud1.rate_hw(lec2, 'Python', 2)
stud1.rate_hw(lec3, 'Python', 8)
stud1.rate_hw(lec3, 'Базы данных', 8)
stud1.rate_hw(lec3, 'Web', 3)

stud2 = Student('Незнайка', 'Носов', 'муж')
stud2.courses_in_progress += ['Химия'] + ['Базы данных'] + ['Python'] + ['JS'] + ['Web']
stud2.add_courses('Технология дистилляции')
stud2.add_courses('Blockchain')
stud2.rate_hw(lec1, 'Химия', 10)
stud2.rate_hw(lec1, 'Базы данных', 10)
stud2.rate_hw(lec2, 'Python', 3)
stud2.rate_hw(lec2, 'JS', 9)
stud2.rate_hw(lec3, 'Python', 8)
stud2.rate_hw(lec3, 'Базы данных', 8)

stud3 = Student('Лиса', 'Алиса', 'жен')
stud3.courses_in_progress += ['Химия'] + ['Технология дистилляции'] + ['Базы данных'] + ['Python'] + ['JS'] + ['Web']
stud3.add_courses('Blockchain')
stud3.rate_hw(lec1, 'Химия', 10)
stud3.rate_hw(lec1, 'Базы данных', 10)
stud3.rate_hw(lec2, 'Python', 2)
stud3.rate_hw(lec2, 'JS', 10)
stud3.rate_hw(lec2, 'Базы данных', 9)
stud3.rate_hw(lec3, 'Python', 9)
stud3.rate_hw(lec3, 'Базы данных', 6)
stud3.rate_hw(lec3, 'Web', 4)

# ревьюеры ------------------------------------------
rev1 = Reviewer('Феликс', 'Джержинский')
rev1.courses_attached += ['Химия'] + ['Технология дистилляции'] + ['Базы данных'] + ['Python'] + ['JS'] + ['Web']
rev1.rate_hw(stud1, 'Web', 3)
rev1.rate_hw(stud1, 'Web', 5)
rev1.rate_hw(stud1, 'Web', 2)
rev1.rate_hw(stud1, 'Базы данных', 4)
rev1.rate_hw(stud1, 'Базы данных', 3)
rev1.rate_hw(stud1, 'Python', 5)
rev1.rate_hw(stud1, 'Python', 5)
rev1.rate_hw(stud1, 'JS', 2)
rev1.rate_hw(stud1, 'JS', 4)

rev1.rate_hw(stud2, 'Web', 2)
rev1.rate_hw(stud2, 'Web', 3)
rev1.rate_hw(stud2, 'Базы данных', 4)
rev1.rate_hw(stud2, 'Базы данных', 5)
rev1.rate_hw(stud2, 'Python', 4)
rev1.rate_hw(stud2, 'Python', 4)
rev1.rate_hw(stud2, 'JS', 3)
rev1.rate_hw(stud2, 'Химия', 5)

rev1.rate_hw(stud3, 'Web', 5)
rev1.rate_hw(stud3, 'Web', 5)
rev1.rate_hw(stud3, 'Базы данных', 4)
rev1.rate_hw(stud3, 'Базы данных', 5)
rev1.rate_hw(stud3, 'Python', 5)
rev1.rate_hw(stud3, 'Python', 4)
rev1.rate_hw(stud3, 'JS', 5)
rev1.rate_hw(stud3, 'Технология дистилляции', 2)
rev1.rate_hw(stud3, 'Технология дистилляции', 2)

rev2 = Reviewer('Olga', 'Petrova')
rev2.courses_attached += ['Blockchain'] + ['Web'] + ['Базы данных'] + ['Python'] + ['JS'] + ['Web']
rev2.rate_hw(stud1, 'Blockchain', 5)
rev2.rate_hw(stud1, 'Blockchain', 3)
rev2.rate_hw(stud1, 'Web', 4)
rev2.rate_hw(stud1, 'Базы данных', 2)
rev2.rate_hw(stud1, 'Базы данных', 3)
rev2.rate_hw(stud1, 'Python', 4)
rev2.rate_hw(stud1, 'Python', 4)
rev2.rate_hw(stud1, 'JS', 4)
rev2.rate_hw(stud1, 'JS', 4)

rev2.rate_hw(stud2, 'Базы данных', 3)
rev2.rate_hw(stud2, 'Базы данных', 3)
rev2.rate_hw(stud2, 'Python', 3)
rev2.rate_hw(stud2, 'Python', 4)
rev2.rate_hw(stud2, 'JS', 4)
rev2.rate_hw(stud2, 'Web', 5)

rev1.rate_hw(stud3, 'Web', 5)
rev1.rate_hw(stud3, 'Web', 4)
rev1.rate_hw(stud3, 'Базы данных', 3)
rev1.rate_hw(stud3, 'Базы данных', 4)
rev1.rate_hw(stud3, 'Python', 5)
rev1.rate_hw(stud3, 'Python', 5)
rev1.rate_hw(stud3, 'JS', 4)

# Вывод списка всех студентов
print(f"{'-' * 30} Студенты {'-' * 30}")
for student in Student.students:
    print(student)

# Вывод списка всех лекторов
print(f"{'-' * 30} Лекторы {'-' * 30}")
for lecturer in Lecturer.lectureres:
    print(lecturer, '\n')

# Вывод списка всех ревьюеры
print(f"{'-' * 30} Проверяющие {'-' * 30}")
for reviewer in Reviewer.revieweres:
    print(reviewer, '\n')


# Сравнение студентов по средним оценкам
print(f"{'-' * 30} Сравнение студентов по средним оценкам {'-' * 30}")
print(f'{stud1.surname} {stud1.get_average_grade()} == {stud2.surname} {stud2.get_average_grade()}', stud1 == stud2)
print(f'{stud2.surname} {stud2.get_average_grade()} > {stud3.surname} {stud3.get_average_grade()}', stud2 > stud3)

# Сравнение лекторов по средним оценкам
print(f"{'-' * 30} Сравнение лекторов по средним оценкам {'-' * 30}")
print(f'{lec1.surname} {lec1.get_average_grade()} == {lec2.surname} {lec2.get_average_grade()}', lec1 == lec2)
print(f'{lec2.surname} {lec2.get_average_grade()} < {lec3.surname} {lec3.get_average_grade()}', lec2 < lec3)


# Вывод средних оценок за курс у студентов
print(f"{'-' * 30} Вывод средних оценок за курс {'-' * 30}")
get_avarage_grade_course(Student.students, 'Базы данных')
get_avarage_grade_course(Student.students, 'Python')
print()

# Вывод средних оценок за курс у лекторов
get_avarage_grade_course(Lecturer.lectureres, 'Базы данных')
get_avarage_grade_course(Lecturer.lectureres, 'Web')
print()

