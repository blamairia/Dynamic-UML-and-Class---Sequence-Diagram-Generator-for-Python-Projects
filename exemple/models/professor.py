from __future__ import annotations  # Enables forward references
from models.person import Person

class Professor(Person):
    """
    A professor inherits from Person and is associated with courses.
    """
    course: Course  # Forward reference to avoid circular import

    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self.department = department

    def assign_to_course(self, course: Course):
        """
        Assign the professor to a course.
        """
        from models.course import Course  # Local import to avoid circular dependency
        self.course = course
        course.professor = self
