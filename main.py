import mysql.connector


# Function to connect to MySQL database
def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="EduSchema"
        )
        if db_connection.is_connected():
            print("Connected to MySQL database")
            return db_connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None


# Function to add a new course
def add_course(course_name, course_type, credits, instructor_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to insert a new course
        add_course_query = "INSERT INTO Course (CName, CType, Credits, IID) VALUES (%s, %s, %s, %s)"
        course_data = (course_name, course_type, credits, instructor_id)

        cursor.execute(add_course_query, course_data)
        db_connection.commit()
        print("Course added successfully")

    except mysql.connector.Error as e:
        print(f"Error adding course: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function to update an existing course
def update_course(course_id, course_name, course_type, credits, instructor_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to update an existing course
        update_course_query = "UPDATE Course SET CName = %s, CType = %s, Credits = %s, IID = %s WHERE CID = %s"
        course_data = (course_name, course_type, credits, instructor_id, course_id)

        cursor.execute(update_course_query, course_data)
        db_connection.commit()
        print("Course updated successfully")

    except mysql.connector.Error as e:
        print(f"Error updating course: {e}")

    finally:
        cursor.close()
        db_connection.close()

def view_deleted_courses():
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to view all deleted courses
        view_deleted_courses_query = "SELECT * FROM DeletedCourses"
        cursor.execute(view_deleted_courses_query)
        deleted_courses = cursor.fetchall()

        # Display deleted courses
        if deleted_courses:
            print("Deleted Courses:")
            for course in deleted_courses:
                print(course)
        else:
            print("No deleted courses found")

    except mysql.connector.Error as e:
        print(f"Error viewing deleted courses: {e}")

    finally:
        cursor.close()
        db_connection.close()

# Function to remove a course
def remove_course(course_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Retrieve course details before deletion
        select_course_query = "SELECT * FROM Course WHERE CID = %s"
        cursor.execute(select_course_query, (course_id,))
        course_data = cursor.fetchone()

        # SQL query to delete a course
        delete_course_query = "DELETE FROM Course WHERE CID = %s"
        course_data_tuple = (course_id,)
        cursor.execute(delete_course_query, course_data_tuple)
        db_connection.commit()

        # Insert into DeletedCourses table
        add_deleted_course_query = "INSERT INTO DeletedCourses (CID, CName, CType, Credits, IID) VALUES (%s, %s, %s, %s, %s)"
        deleted_course_data = (course_data[0], course_data[1], course_data[2], course_data[3], course_data[4])
        cursor.execute(add_deleted_course_query, deleted_course_data)
        db_connection.commit()

        print("Course removed")

    except mysql.connector.Error as e:
        print(f"Error removing course: {e}")

    finally:
        cursor.close()
        db_connection.close()



# Function to search for courses by keyword
def search_courses(keyword):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to search for courses
        search_course_query = "SELECT * FROM Course WHERE CName LIKE %s"
        search_data = ('%' + keyword + '%',)

        cursor.execute(search_course_query, search_data)
        courses = cursor.fetchall()

        # Display search results
        if courses:
            print("Search results:")
            for course in courses:
                print(course)
        else:
            print("No courses found with the given keyword")

    except mysql.connector.Error as e:
        print(f"Error searching courses: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function to sort courses by name
def sort_courses():
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to sort courses by name
        sort_course_query = "SELECT * FROM Course ORDER BY CName"

        cursor.execute(sort_course_query)
        courses = cursor.fetchall()

        # Display sorted courses
        if courses:
            print("Sorted courses:")
            for course in courses:
                print(course)
        else:
            print("No courses found")

    except mysql.connector.Error as e:
        print(f"Error sorting courses: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function to add a new instructor
def add_instructor(instructor_name, email, hire_date, department):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to insert a new instructor
        add_instructor_query = "INSERT INTO Instructor (IName, Email, HireDate, Department) VALUES (%s, %s, %s, %s)"
        instructor_data = (instructor_name, email, hire_date, department)

        cursor.execute(add_instructor_query, instructor_data)
        db_connection.commit()
        print("Instructor added successfully")

    except mysql.connector.Error as e:
        print(f"Error adding instructor: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function to update an existing instructor
def update_instructor(instructor_id, instructor_name, email, hire_date, department):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to update an existing instructor
        update_instructor_query = "UPDATE Instructor SET IName = %s, Email = %s, HireDate = %s, Department = %s WHERE IID = %s"
        instructor_data = (instructor_name, email, hire_date, department, instructor_id)

        cursor.execute(update_instructor_query, instructor_data)
        db_connection.commit()
        print("Instructor updated successfully")

    except mysql.connector.Error as e:
        print(f"Error updating instructor: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function to enroll a student in a course
def enroll_student(student_id, course_id, enrollment_date):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to enroll a student in a course
        enroll_student_query = "INSERT INTO Student_Course (SID, CID, EnrollmentDate) VALUES (%s, %s, %s)"
        enrollment_data = (student_id, course_id, enrollment_date)

        cursor.execute(enroll_student_query, enrollment_data)
        db_connection.commit()
        print("Student enrolled successfully")

    except mysql.connector.Error as e:
        print(f"Error enrolling student: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function to add a grade for a student's assignment
def add_grade(student_id, assignment_id, marks_obtained, grade):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to add a grade for a student's assignment
        add_grade_query = "INSERT INTO Grades (SID, AID, MarksObtained, Grade) VALUES (%s, %s, %s, %s)"
        grade_data = (student_id, assignment_id, marks_obtained, grade)

        cursor.execute(add_grade_query, grade_data)
        db_connection.commit()
        print("Grade added successfully")

    except mysql.connector.Error as e:
        print(f"Error adding grade: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function to view grades of a student
def view_grades(student_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # SQL query to view grades of a student
        view_grades_query = "SELECT A.AID, A.AName, G.MarksObtained, G.Grade FROM Assignment A INNER JOIN Grades G ON A.AID = G.AID WHERE G.SID = %s"

        cursor.execute(view_grades_query, (student_id,))
        grades = cursor.fetchall()

        # Display grades
        if grades:
            print(f"Grades for Student ID {student_id}:")
            for grade in grades:
                print(grade)
        else:
            print(f"No grades found for Student ID {student_id}")

    except mysql.connector.Error as e:
        print(f"Error viewing grades: {e}")

    finally:
        cursor.close()
        db_connection.close()


# Function for the main menu and user interaction
def main():
    db_connection = connect_to_database()
    if not db_connection:
        return

    cursor = db_connection.cursor()

    while True:
        print("\nMain Menu:")
        print("1. Course Management")
        print("2. Instructor Management")
        print("3. Student Enrollment")
        print("4. Assignments & Grades")
        print("5. Exit")
        print("6. View Deleted")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Course Management Menu
            while True:
                print("\nCourse Management:")
                print("1. Add Course")
                print("2. Update Course")
                print("3. Remove Course")
                print("4. Search Course")
                print("5. Sort Courses")
                print("6. Back to Main Menu")

                course_choice = input("Enter your choice (1-6): ")

                if course_choice == '1':
                    # Add Course
                    course_name = input("Enter course name: ")
                    course_type = input("Enter course type: ")
                    credits = int(input("Enter credits: "))
                    instructor_id = int(input("Enter instructor ID: "))
                    add_course(course_name, course_type, credits, instructor_id)

                elif course_choice == '2':
                    # Update Course
                    course_id = int(input("Enter course ID to update: "))
                    course_name = input("Enter new course name: ")
                    course_type = input("Enter new course type: ")
                    credits = int(input("Enter new credits: "))
                    instructor_id = int(input("Enter new instructor ID: "))
                    update_course(course_id, course_name, course_type, credits, instructor_id)

                elif course_choice == '3':
                    # Remove Course
                    course_id = int(input("Enter course ID to remove: "))
                    remove_course(course_id)

                elif course_choice == '4':
                    # Search Course
                    keyword = input("Enter keyword to search: ")
                    search_courses(keyword)

                elif course_choice == '5':
                    # Sort Courses
                    sort_courses()

                elif course_choice == '6':
                    # Back to Main Menu
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 6.")

        elif choice == '2':
            # Instructor Management Menu
            while True:
                print("\nInstructor Management:")
                print("1. Add Instructor")
                print("2. Update Instructor")
                print("3. Back to Main Menu")

                instructor_choice = input("Enter your choice (1-3): ")

                if instructor_choice == '1':
                    # Add Instructor
                    instructor_name = input("Enter instructor name: ")
                    email = input("Enter email: ")
                    hire_date = input("Enter hire date (YYYY-MM-DD): ")
                    department = input("Enter department: ")
                    add_instructor(instructor_name, email, hire_date, department)

                elif instructor_choice == '2':
                    # Update Instructor
                    instructor_id = int(input("Enter instructor ID to update: "))
                    instructor_name = input("Enter new instructor name: ")
                    email = input("Enter new email: ")
                    hire_date = input("Enter new hire date (YYYY-MM-DD): ")
                    department = input("Enter new department: ")
                    update_instructor(instructor_id, instructor_name, email, hire_date, department)

                elif instructor_choice == '3':
                    # Back to Main Menu
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 3.")

        elif choice == '3':
            # Student Enrollment Menu
            while True:
                print("\nStudent Enrollment:")
                print("1. Enroll Student in Course")
                print("2. Back to Main Menu")

                enrollment_choice = input("Enter your choice (1-2): ")

                if enrollment_choice == '1':
                    # Enroll Student
                    student_id = int(input("Enter student ID: "))
                    course_id = int(input("Enter course ID to enroll in: "))
                    enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                    enroll_student(student_id, course_id, enrollment_date)

                elif enrollment_choice == '2':
                    # Back to Main Menu
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 2.")

        elif choice == '4':
            # Assignments & Grades Menu
            while True:
                print("\nAssignments & Grades:")
                print("1. Add Grade for Student")
                print("2. View Grades for Student")
                print("3. Back to Main Menu")

                grade_choice = input("Enter your choice (1-3): ")

                if grade_choice == '1':
                    # Add Grade
                    student_id = int(input("Enter student ID: "))
                    assignment_id = int(input("Enter assignment ID: "))
                    marks_obtained = int(input("Enter marks obtained: "))
                    grade = input("Enter grade: ")
                    add_grade(student_id, assignment_id, marks_obtained, grade)

                elif grade_choice == '2':
                    # View Grades
                    student_id = int(input("Enter student ID to view grades: "))
                    view_grades(student_id)

                elif grade_choice == '3':
                    # Back to Main Menu
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 3.")

        elif choice == '5':
            # Exit
            print("Exiting program...")
            break


        elif choice == '6':
            view_deleted_courses()


        else:

            print("Invalid choice. Please enter a number from 1 to 6.")

    # Close cursor and database connection
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
