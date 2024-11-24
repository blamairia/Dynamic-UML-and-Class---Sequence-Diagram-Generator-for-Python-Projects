# test_example.py


class B:
    """
    Class B: A standalone class.
    """
    pass


class A:
    """
    Class A: Has an association with B.
    """
    def __init__(self, b: B):
        self.b: B = b  # Explicitly associate A with B

class B:
    def action(self):
        return "Action in B executed"


class A:
    def __init__(self, b: B):
        self.b: B = b  # Aggregation or association

    def use_b(self):
        return self.b.action()  # Explicit interaction with B

class A:
    b: B  # Explicit relationship at the class level

    def __init__(self, b: B):
        self.b = b

    def get_b(self) -> B:
        return self.b



a = A(b=B())
