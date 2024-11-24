from models.person import Person

class Student(Person):
    """
    A student inherits from Person.
    """
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        """
        Enroll the student in a course.
        """
        self.courses.append(course)
        course.add_student(self)

    def list_courses(self):
        """
        List all courses the student is enrolled in.
        """
        return [course.name for course in self.courses]
