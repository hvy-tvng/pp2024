students = []
courses = []
marks = {}

def main_menu():
    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Exit")
        n = input("Enter your choice: ")

        if n == '1':
            input_students()
        elif n == '2':
            input_courses()
        elif n == '3':
            input_marks()
        elif n == '4':
            list_courses()
        elif n == '5':
            list_students()
        elif n == '6':
            show_marks()
        elif n == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def input_students():
    # Ensure num_students is a non-negative integer
    while True:
        num_students = input("Enter number of students: ")
        if not num_students.isdigit() or int(num_students) < 0:
            print("Invalid input. Please enter a non-negative integer.")
        else:
            break

    for _ in range(int(num_students)):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")

        # Validate DoB as a number
        while True:
            dob = input("Enter student DoB (DD/MM/YYYY): ")
            if not dob.isdigit():
                print("Invalid DoB. Please enter a valid number.")
            else:
                break

        students.append((student_id, name, dob))

def input_courses():
    if len(students) == 0:
        print("Please enter student information first to use this feature.")
        return

    # Ensure num_courses is a non-negative integer
    while True:
        num_courses = input("Enter number of courses: ")
        if not num_courses.isdigit() or int(num_courses) < 0:
            print("Invalid input. Please enter a non-negative integer.")
        else:
            break

    for _ in range(int(num_courses)):
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append((course_id, name))

def input_marks():
    if len(courses) == 0 or len(students) == 0:
        print("Courses or students information is missing.")
        return

    course_id = input("Enter course id to input marks: ")
    for student in students:
        mark = input(f"Enter mark for student {student[1]} in course {course_id}: ")
        marks[(student[0], course_id)] = mark

def list_courses():
    if len(courses) == 0:
        print("There are 0 courses.")
    else:
        print("-" * 30)
        print("|{:<10}|{:<20}|".format("Course ID", "Course Name"))
        print("-" * 30)
        
        for course in courses:
            print("|{:<10}|{:<20}|".format(course[0], course[1]))
        
        print("-" * 30)

def list_students():
    if len(students) == 0:
        print("No students available.")
        return

    print("-" * 50)
    print("|{:<5}|{:<20}|{:<13}|{:<11}|".format("No", "Name", "Date of birth", "Student ID"))
    print("-" * 50)
    
    for i, student in enumerate(students, start=1):
        print("|{:<5}|{:<20}|{:<13}|{:<11}|".format(
            i, student[1], student[2], student[0]))
    
    print("-" * 50)

def show_marks():
    if len(courses) == 0 or len(students) == 0:
        print("Courses or students information is missing.")
        return

    course_id = input("Enter course id to show marks: ")
    
    print("-" * 40)
    print("|{:<20}|{:<10}|".format("Student Name", "Mark"))
    print("-" * 40)
    
    for student in students:
        student_id = student[0]
        if (student_id, course_id) in marks:
            print("|{:<20}|{:<10}|".format(student[1], marks[(student_id, course_id)]))
        else:
            print("|{:<20}|{:<10}|".format(student[1], "N/A"))
    
    print("-" * 40)

# Run the main menu
main_menu()
