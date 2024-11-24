from models.student import Student
from models.professor import Professor

class Course:
    """
    Represents a course that students can enroll in.
    """
    def __init__(self, name, professor: Professor):
        self.name = name
        self.professor = professor  # Association with Professor
        self.students: list[Student] = []  # Aggregation: List of students

    def add_student(self, student: Student):
        """
        Add a student to the course.
        """
        self.students.append(student)

    def list_students(self):
        """
        List all students in the course.
        """
        return [student.name for student in self.students]
