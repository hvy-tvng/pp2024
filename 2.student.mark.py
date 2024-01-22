class MarkSheetSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        while True:
            num_students = input("Enter number of students: ")
            if not num_students.isdigit() or int(num_students) < 0:
                print("Invalid input. Please enter a non-negative integer.")
            else:
                break

        for _ in range(int(num_students)):
            student_id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB (DD/MM/YYYY): ")

            self.students.append({'id': student_id, 'name': name, 'dob': dob})

    def input_courses(self):
        if not self.students:
            print("Please enter student information first to use this feature.")
            return

        while True:
            num_courses = input("Enter number of courses: ")
            if not num_courses.isdigit() or int(num_courses) < 0:
                print("Invalid input. Please enter a non-negative integer.")
            else:
                break

        for _ in range(int(num_courses)):
            course_id = input("Enter course id: ")
            name = input("Enter course name: ")
            self.courses.append({'id': course_id, 'name': name})

    def input_marks(self):
        if not self.courses or not self.students:
            print("Courses or students information is missing.")
            return

        course_id = input("Enter course id to input marks: ")
        for student in self.students:
            mark = input(f"Enter mark for student {student['name']} in course {course_id}: ")
            self.marks[(student['id'], course_id)] = mark

    def list_courses(self):
        if not self.courses:
            print("There are 0 courses.")
        else:
            print("-" * 30)
            print("|{:<10}|{:<20}|".format("Course ID", "Course Name"))
            print("-" * 30)

            for course in self.courses:
                print("|{:<10}|{:<20}|".format(course['id'], course['name']))

            print("-" * 30)

    def list_students(self):
        if not self.students:
            print("No students available.")
            return

        print("-" * 50)
        print("|{:<5}|{:<20}|{:<13}|{:<11}|".format("No", "Name", "Date of birth", "Student ID"))
        print("-" * 50)

        for i, student in enumerate(self.students, start=1):
            print("|{:<5}|{:<20}|{:<13}|{:<11}|".format(
                i, student['name'], student['dob'], student['id']))

        print("-" * 50)

    def show_marks(self):
        if not self.courses or not self.students:
            print("Courses or students information is missing.")
            return

        course_id = input("Enter course id to show marks: ")

        print("-" * 40)
        print("|{:<20}|{:<10}|".format("Student Name", "Mark"))
        print("-" * 40)

        for student in self.students:
            student_id = student['id']
            if (student_id, course_id) in self.marks:
                print("|{:<20}|{:<10}|".format(student['name'], self.marks[(student_id, course_id)]))
            else:
                print("|{:<20}|{:<10}|".format(student['name'], "N/A"))

        print("-" * 40)

    def main_menu(self):
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
                self.input_students()
            elif n == '2':
                self.input_courses()
            elif n == '3':
                self.input_marks()
            elif n == '4':
                self.list_courses()
            elif n == '5':
                self.list_students()
            elif n == '6':
                self.show_marks()
            elif n == '7':
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate MarkSheetSystem and run the main menu
mark_sheet_system = MarkSheetSystem()
mark_sheet_system.main_menu()
