
class Student:
    def __init__(self, name, study_form, grade, passed_on_time=True):
        self.name = name
        self.study_form = study_form  # "budget" or "paid"
        self.grade = grade
        self.passed_on_time = passed_on_time

    def get_stipend(self):
        if self.study_form != "budget" or not self.passed_on_time or self.grade < 5:
            return 0  # No stipend

        if self.grade >= 8:
            return 1.5  # 50% increase
        elif self.grade >= 6:
            return 1.25  # 25% increase
        else:
            return 1.0 # Minimum stipend


class StipendSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_paid_students(self):
        return [student.name for student in self.students if student.study_form == "paid"]

    def get_average_grade(self):
        grades = [student.grade for student in self.students]
        return sum(grades) / len(grades) if grades else 0

    def get_students_with_25_percent_increase(self):
        return [student.name for student in self.students if student.get_stipend() == 1.25]



# Example usage:
stipend_system = StipendSystem()

# Students who received a 25% increase in stipend (requirement 4)
stipend_system.add_student(Student("Alice", "budget", 7, True))
stipend_system.add_student(Student("Bob", "budget", 6, True))
stipend_system.add_student(Student("Charlie", "budget", 7, True))
stipend_system.add_student(Student("David", "budget", 6, True))
stipend_system.add_student(Student("Eve", "budget", 7, True))
stipend_system.add_student(Student("Jona", "budget", 6, True))
stipend_system.add_student(Student("Frank", "budget", 7, True))
stipend_system.add_student(Student("Grace", "budget", 6, True))
stipend_system.add_student(Student("Heidi", "budget", 7, True))
stipend_system.add_student(Student("Ivan", "budget", 6, True))


# Add other students (requirement 5)
stipend_system.add_student(Student("Mallory", "paid", 9, True))
stipend_system.add_student(Student("Trent", "paid", 8, False))


# Output (requirements 4, 5, 6)
print("Students with 25% stipend increase:", stipend_system.get_students_with_25_percent_increase())
print("Students on paid study form:", stipend_system.get_paid_students())
print("Average grade:", stipend_system.get_average_grade())