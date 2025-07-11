#!/usr/bin/env python3
# Author ID: 118541234

class Student:

    # This runs when you create a new student.
    # It saves the student's name and number, and sets up an empty list for their courses.
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Make sure student number is always stored as text (string)
        self.courses = {}  # Empty dictionary to store course names and grades

    # This shows the student's name and number in a nice format
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # This adds a new course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # This calculates and shows the GPA (average grade) of the student
    def displayGPA(self):
        try:
            if len(self.courses) == 0:
                raise ZeroDivisionError  # Handle case where no grades were added
            gpa = sum(self.courses.values()) / len(self.courses)  # Average of all grades
        except ZeroDivisionError:
            gpa = 0.0  # If no courses added, GPA is 0
        return 'GPA of student ' + self.name + ' is ' + str(gpa)

    # This returns a list of only the passed courses (grade must be more than 0.0)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return sorted(passed_courses)  # Sort alphabetically just to make it neat

# This part runs only if the file is being run directly (not imported)
if __name__ == '__main__':
    # Creating first student and adding some course grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Creating second student and adding some course grades
    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)  # Failed course

    # Show student1's details, GPA, and passed courses
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Show student2's details, GPA, and passed courses
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
