# -*- coding: utf-8 -*-

import pandas as pd


# function to calculate average score and letter grade
def calculate_grade(scores):
    avg_score = sum(scores) / len(scores)
    if avg_score >= 90:
        letter_grade = "A"
    elif avg_score >= 80:
        letter_grade = "B"
    elif avg_score >= 70:
        letter_grade = "C"
    elif avg_score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return avg_score, letter_grade


# Define the student data
student_first_names = ["Marjan", "Khaleed", "Alireza", "Karen", "Shairylle"]
student_last_names = ["Jafari", "Opeloyeru", "Shirazi", "Dela Cruz", "Patio"]
student_ids = ["301321020", "301286462", "301307134", "301296127", "301270129"]
students_password = [student_last_names[0] + "2023", student_last_names[1] + "2023", student_last_names[2] + "2023", student_last_names[3] + "2023", student_last_names[4] + "2023"]
student_email_address = ["mjafari7@my.centennialcollege.ca", "kopeloye@my.centennialcollege.ca", "ahiraz6@my.centennialcollege.ca", "kdelac14@my.centennialcollege.ca", "spatio@my.centennialcollege.ca"]

# Define the educator data
educator_id = "professor"
educator_password = "comp120"

# Define error message
error_message = "Invalid entry, please try again."

# Initialize flags
is_not_educator_or_student = True
is_educator_login_correct = True
is_student_login_correct = True
is_educator_action = True

#question
questions = [
    {
        "question": "which of the following is dedined as a tangible realization of project plans\nthat can be easily refernced by stakeholder when trying to describe desired change",
        "options": ["A Table", "A map", "A prototype", "An estimate"],
        "answer": "A prototype"
    },
    {
        "question": "According to the principle that assesses risks that guide the software process,\nwhat is required to mitigate the risks?",
        "options": ["Presenting organized support plans", "Stating the basic requirements", "Capturing attention", "Establishing contingency plans"],
        "answer": "Establishing contingency plans"
    },
    {
        "question": "The first task in the creation of the first prototype is to ________",
        "options": ["engineer the algorithms", "test the prototype", "identify the features and functions that are important to the stakeholders", "decide how much time will be allocated to creating the first prototype"],
        "answer": "identify the features and functions that are important to the stakeholders"
    },
    {
        "question": "Identify the goal of the spiral model.",
        "options": ["To make communication easier between stakeholders", "To create extensible prototypes each time a process is iterated", "To make use of heuristics to solve complex problems", "To improve actions within each framework activity"],
        "answer": "To create extensible prototypes each time a process is iterated"
    },
    {
        "question": "Many misunderstandings between developers and stakeholders can be alleviated by beginning with",
        "options": ["adding input and output to the user interface prototype", "testing a prototype", "a paper prototype of the user interface", "engineering the algorithms"],
        "answer": "testing a prototype"
    }
]
print("hi")
import os
os.system('cls')

# Print welcome message
print("Welcome to our grade and academic management app! Keep track of your\ngrades, attendance, and assignments all in one place. Whether you are\na student or an educator, our app is designed to make managing your \nacademic life easier :).")

# Ask if user is a student or educator
while is_not_educator_or_student:
    student_or_educator = input("Are you an educator or a student?: ").lower()

    # Check if user entered a valid response
    if student_or_educator == "student" or student_or_educator == "educator":
        is_not_educator_or_student = False
    else:
        print(error_message)
        input("press enter to clear the screen")
        import os
        os.system('cls')
import os
os.system('cls')


# Ask for user ID
if student_or_educator == "educator":
    print("Hi there educator! Please log in below.")
    while is_educator_login_correct:
        user_educator_id = input("Educator ID: ").lower()
        user_educator_password = input("Password: ").lower()
        if user_educator_id == educator_id and user_educator_password == educator_password:
            is_educator_login_correct = False
        else:
            print(error_message)
            input("press enter to clear the screen")
        import os
        os.system('cls')

    # Clears the screen after selection
    import os
    os.system('cls')

        # Loops until educator enters a valid entry
        
    student_grades = {}  # initialize the dictionary outside of the while loop
    while is_educator_action:
        # Ask for user action
        print("What would you like to do today?")
        print("1. Enter student grades")
        print("2. View student grades")
        educator_action = input("Enter your choice: ")
        
        if educator_action == "1":
            # Prompt for number of students and assignments
            num_students = int(input("Enter the number of students: "))
            num_assignments = int(input("Enter the number of assignments: "))

            # Prompt for each student's name and grades
            for i in range(num_students):
                name = input(f"Enter the name of student {i+1}: ")
                grades = []
                for j in range(num_assignments):
                    grade = float(input(f"Enter the grade for assignment {j+1}: "))
                    grades.append(grade)
                student_grades[name] = grades
                os.system('cls')


            # Clear the screen
            os.system('cls')
            
        elif educator_action == "2":
            # Display each student's name, average score, and letter grade in a table
            table = []
            for name, grades in student_grades.items():
                avg_score, letter_grade = calculate_grade(grades)
                table.append([name, avg_score, letter_grade])
            
            df = pd.DataFrame(table, columns=["Student Name", "Average Score", "Letter Grade"])
            print(df.to_string(index=False))
            
            # Prompt to continue or exit
            while True:
                continue_choice = input("Enter 'c' to continue or 'e' to exit: ")
                if continue_choice == "c":
                    os.system('cls')
                    break
                elif continue_choice == "e":
                    is_educator_action = False
                    break
                else:
                    print("Invalid choice. Please try again.")
            
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")
                

#student


# Student Login Section
elif student_or_educator == "student":
    print("Hi there student! Please log in below.")
    while is_student_login_correct:
        user_student_id = input("Student ID: ").strip()
        user_student_password = input("Password: ").strip()

        # Verify student credentials
        if user_student_id in student_ids and user_student_password == students_password[student_ids.index(user_student_id)]:
            is_student_login_correct = False
            print("You are now logged in as a student.")
        else:
            print(error_message)
            input("Press enter to clear the screen")
            import os
            os.system('cls')
    # Clears the screen after selection
    import os
    os.system('cls')


    schedule = {}

# Function to display student menu and handle user choice
def student_menu():
    print("Welcome to the Student Menu")
    while True:
        print("\nPlease select an option:")
        print("1. Schedule Class")
        print("2. Change Password")
        print("3. Take Self-Assessment Test")
        choice = input("Enter option number: ")
        if choice == "1":
            schedule_class()
            print("You have selected to schedule a class.")
        elif choice == "2":
            change_password_menu()
            print("You have selected to change your password.")
        elif choice == "3":
            take_assessment()
            print("You have selected to take the self-assessment test.")
        else:
            print("Invalid choice. Please try again.")

# function to take self-assessment test
def take_assessment():
    print("Welcome to the self-assessment test!")
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, opt in enumerate(q["options"]):
            print(f"{chr(97+i)}. {opt}")
        user_answer = input("Your answer (a, b, c, d): ").lower()
        if user_answer in ["a", "b", "c", "d"]:
            if q["options"][ord(user_answer) - ord('a')] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        else:
            print("Invalid input.")
    print(f"\nYour score is {score} out of {len(questions)}")


# Function to add a class to the schedule
def add_class():
    course_name = input("Enter the course name: ")
    instructor_name = input("Enter the instructor name: ")
    course_time = input("Enter the course time: ")
    course_location = input("Enter the course location: ")
    schedule[course_name] = [instructor_name, course_time, course_location]
    print("Class added successfully!")

# Function to remove a class from the schedule
def remove_class():
    course_name = input("Enter the course name to remove: ")
    if course_name in schedule:
        del schedule[course_name]
        print("Class removed successfully!")
    else:
        print("Class not found in schedule.")

# Function to display the class schedule
def display_schedule():
    if not schedule:
        print("Schedule is empty.")
    else:
        df = pd.DataFrame.from_dict(schedule, orient='index', columns=["Instructor Name", "Course Time", "Course Location"])
        df.index.name = "Course Name"
        print(df)

# Function to schedule a class
def schedule_class():
    print("Schedule Class Menu")
    print("-------------------")
    print("1. Add Class")
    print("2. Remove Class")
    print("3. Display Schedule")
    print("4. Return to Main Menu")

    choice = input("Enter your choice: ").strip()
    os.system('cls')

    if choice == "1":
        add_class()
        input("Press Enter to continue...")
    elif choice == "2":
        remove_class()
        input("Press Enter to continue...")
    elif choice == "3":
        display_schedule()
        input("Press Enter to continue...")
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        os.system('cls')

# Function to change password
def change_password_menu():
    print("Change Password Menu")
    print("--------------------")
    print("1. Proceed to Change Password")
    print("2. Return to Main Menu")

    choice = input("Enter your choice: ").strip()
    os.system('cls')

    if choice == "1":
        change_password()
        input("Press Enter to continue...")
    elif choice == "2":
        return
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        os.system('cls')

# Function to change password
def change_password():
    # Get current password
    current_password = input("Enter your current password: ").strip()

    # Verify current password
    if current_password == students_password[student_ids.index(user_student_id)]:
        # Get new password
        new_password = input("Enter your new password: ").strip()

        # Verify new password
        if new_password == current_password:
            print("New password cannot be the same as the current password.")
        else:
            # Get new password again
            new_password2 = input("Enter your new password again: ").strip()

            # Verify new password again
            if new_password == new_password2:
                # Change password
                students_password[student_ids.index(user_student_id)] = new_password
                print("Password changed successfully!")
            else:
                print("Passwords do not match.")
    else:
        print("Incorrect password.")

# Main program loop
while True:
    # Clear the screen
    os.system('cls')
    student_menu()