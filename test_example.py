class B:
    """
    Class B: A standalone class.
    """
    def action(self):
        return "Action in B executed"

class A:
    """
    Class A: Has an association with B.
    """
    b: B  # Explicit relationship at the class level

    def __init__(self, b: B):
        self.b = b  # Aggregation or association

    def use_b(self):
        return self.b.action()  # Explicit interaction with B

    def get_b(self) -> B:
        return self.b

# Usage
a = A(b=B())
