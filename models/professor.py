from models.person import Person

class Professor(Person):
    """
    A professor inherits from Person.
    """
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def assign_to_course(self, course):
        """
        Assign the professor to a course.
        """
        course.professor = self
