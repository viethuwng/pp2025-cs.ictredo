import math
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__credits = {}

    def input_marks(self, course, mark, credit):
        self.__marks[course] = math.floor(mark * 10) / 10  # Round down to 1 decimal place
        self.__credits[course] = credit

    def calculate_gpa(self):
        if not self.__marks:
            return 0
        total_weighted_score = sum(self.__marks[course] * self.__credits[course] for course in self.__marks)
        total_credits = sum(self.__credits.values())
        return total_weighted_score / total_credits if total_credits > 0 else 0

    def list_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, DOB: {self.__dob}")
        print("Marks:")
        for course, mark in self.__marks.items():
            print(f"  {course}: {mark}")
        print(f"GPA: {self.calculate_gpa():.1f}")

    def get_gpa(self):
        return self.calculate_gpa()


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
        sorted_students = sorted(self.__students, key=lambda s: s.get_gpa(), reverse=True)
        for student in sorted_students:
            student.list_info()

    def list_courses(self):
        for course in self.__courses:
            print(course.get_info())

    def curses_ui(self):
        def draw_ui(stdscr):
            stdscr.clear()
            stdscr.addstr(0, 0, "Student Management System", curses.A_BOLD)
            stdscr.addstr(2, 0, "1. List Courses")
            stdscr.addstr(3, 0, "2. List Students")
            stdscr.addstr(4, 0, "3. Exit")
            stdscr.refresh()
            
            while True:
                choice = stdscr.getch()
                if choice == ord('1'):
                    stdscr.clear()
                    for i, course in enumerate(self.__courses):
                        stdscr.addstr(i, 0, course.get_info())
                    stdscr.refresh()
                elif choice == ord('2'):
                    stdscr.clear()
                    sorted_students = sorted(self.__students, key=lambda s: s.get_gpa(), reverse=True)
                    for i, student in enumerate(sorted_students):
                        stdscr.addstr(i, 0, f"{student.get_gpa():.1f} - {student._Student__name}")
                    stdscr.refresh()
                elif choice == ord('3'):
                    break

        curses.wrapper(draw_ui)


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
    student1.input_marks('Math', 85.67, 3)
    student1.input_marks('Physics', 90.45, 4)
    student2.input_marks('Math', 78.34, 3)
    student2.input_marks('Physics', 88.12, 4)
    
    # Curses UI
    sm.curses_ui()
