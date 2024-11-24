from models.student import Student
from models.professor import Professor
from models.course import Course

# Dummy interactions
prof = Professor(name="Dr. Smith", age=45, department="Computer Science")
course = Course(name="Advanced Python", professor=prof)
prof.assign_to_course(course)

student1 = Student(name="Alice", age=20, student_id="S1001")
student2 = Student(name="Bob", age=22, student_id="S1002")
student1.enroll(course)
student2.enroll(course)

print(f"{prof.name} teaches {course.name}")
print(f"Students in {course.name}: {', '.join(course.list_students())}")
print(f"{student1.name} is enrolled in: {', '.join(student1.list_courses())}")
