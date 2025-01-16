class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def input_marks(self, course, mark):
        self.__marks[course] = mark

    def list_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, DOB: {self.__dob}")
        print("Marks:")
        for course, mark in self.__marks.items():
            print(f"  {course}: {mark}")


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def get_info(self):
        return f"Course ID: {self.__course_id}, Name: {self.__name}"


class StudentManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def list_students(self):
        for student in self.__students:
            student.list_info()

    def list_courses(self):
        for course in self.__courses:
            print(course.get_info())


# Example usage
if __name__ == '__main__':
    sm = StudentManagement()
    
    # Adding courses
    course1 = Course('C001', 'Math')
    course2 = Course('C002', 'Physics')
    sm.add_course(course1)
    sm.add_course(course2)
    
    # Adding students
    student1 = Student('S001', 'Alice', '2000-01-01')
    student2 = Student('S002', 'Bob', '2001-02-02')
    sm.add_student(student1)
    sm.add_student(student2)
    
    # Input marks
    student1.input_marks('Math', 85)
    student1.input_marks('Physics', 90)
    student2.input_marks('Math', 78)
    student2.input_marks('Physics', 88)
    
    # List students and courses
    print("Courses:")
    sm.list_courses()
    print("\nStudents:")
    sm.list_students()
