class Person:
    """
    Base class representing a person.
    """
    name: str  # Class-level attributes
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """
        Introduce the person.
        """
        return f"My name is {self.name}, and I am {self.age} years old."
