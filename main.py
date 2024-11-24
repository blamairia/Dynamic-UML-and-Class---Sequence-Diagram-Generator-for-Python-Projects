from models.student import Student
from models.professor import Professor
from models.course import Course

def main():
    # Create a professor
    prof = Professor(name="Dr. Smith", age=45, department="Computer Science")

    # Create a course and assign the professor
    course = Course(name="Advanced Python", professor=prof)

    # Create students
    student1 = Student(name="Alice", age=20, student_id="S1001")
    student2 = Student(name="Bob", age=22, student_id="S1002")

    # Enroll students in the course
    student1.enroll(course)
    student2.enroll(course)

    # Test class interactions
    print(prof.introduce())
    print(f"{prof.name} teaches {course.name}")
    print(f"Students in {course.name}: {', '.join(course.list_students())}")

    # Dynamic interactions for sequence diagrams
    print(f"{student1.name} introduces themselves: {student1.introduce()}")
    print(f"{student1.name} is enrolled in: {', '.join(student1.list_courses())}")

if __name__ == "__main__":
    main()
