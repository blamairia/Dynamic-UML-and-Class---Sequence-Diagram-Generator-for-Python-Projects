import trace
import sys

def main():
    """
    The main function where the program to be analyzed runs.
    """
    from models.student import Student
    from models.professor import Professor
    from models.course import Course

    # Example interactions
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

if __name__ == "__main__":
    # Create a trace object
    tracer = trace.Trace(
        trace=True,
        count=False,
        outfile="trace_log.txt"  # File to save the logs
    )

    # Redirect standard output to a file AND run the trace
    with open("trace_log.txt", "w") as f:
        sys.stdout = f  # Redirect stdout to the file
        tracer.run('main()')  # Run the main function under the tracer
        sys.stdout = sys.__stdout__  # Restore stdout back to the terminal
