from __future__ import annotations
from models.person import Person

class Student(Person):
    """
    A student inherits from Person and has a relationship with Course.
    """
    courses: list[Course]  # Forward reference to avoid circular import

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course: Course):
        """
        Enroll in a course.
        """
        from models.course import Course  # Local import to avoid circular dependency
        self.courses.append(course)
        course.add_student(self)

    def list_courses(self) -> list[str]:
        """
        List all courses the student is enrolled in.
        """
        return [course.name for course in self.courses]
