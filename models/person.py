class Person:
    """
    Base class representing a person.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """
        Introduce the person.
        """
        return f"My name is {self.name}, and I am {self.age} years old."
