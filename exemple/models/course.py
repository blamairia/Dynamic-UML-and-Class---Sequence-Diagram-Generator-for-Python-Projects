from __future__ import annotations  # Enables forward references

class Course:
    """
    Represents a course that students can enroll in and is taught by a professor.
    """
    professor: Professor  # Forward reference
    students: list[Student]  # Forward reference

    def __init__(self, name: str, professor: Professor):
        from models.professor import Professor  # Local import to avoid circular dependency
        self.name = name
        self.professor = professor
        self.students = []

    def add_student(self, student: Student):
        """
        Add a student to the course.
        """
        from models.student import Student  # Local import to avoid circular dependency
        self.students.append(student)

    def list_students(self):
        """
        List all students in the course.
        """
        return [student.name for student in self.students]
