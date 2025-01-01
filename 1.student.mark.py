
students = []  
courses = []   
marks = {}     


def input_students():
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student Name: ")
        student_dob = input("Enter student Date of Birth: ")
        students.append({'id': student_id, 'name': student_name, 'dob': student_dob})


def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course Name: ")
        courses.append({'id': course_id, 'name': course_name})


def input_marks():
    course_id = input("Enter Course ID to input marks: ")
    if course_id not in [course['id'] for course in courses]:
        print("Invalid Course ID!")
        return
    
    if course_id not in marks:
        marks[course_id] = {}
    
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark


def list_students():
    print("\n--- List of Students ---")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")


def list_courses():
    print("\n--- List of Courses ---")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")


def show_marks():
    course_id = input("Enter Course ID to view marks: ")
    if course_id not in marks:
        print("No marks available for this course.")
        return
    
    print(f"\n--- Marks for Course {course_id} ---")
    for student in students:
        mark = marks[course_id].get(student['id'], "No mark")
        print(f"Student: {student['name']} (ID: {student['id']}), Mark: {mark}")


def main():
    input_students()
    input_courses()
    
    while True:
        print("\n--- Student Mark Management ---")
        print("1. List Students")
        print("2. List Courses")
        print("3. Input Marks")
        print("4. Show Marks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            list_students()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            show_marks()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
