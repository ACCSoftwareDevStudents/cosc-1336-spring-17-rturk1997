from model.person import Person
from model.course import Course
from model.student import Student
from model.professor import Professor
from model.enrollment import Enrollment
from model.transcript import Transcript
from data.school_initializer import SchoolInitializer
from data.school_db import SchoolDB

class Gradebook:

    def __init__(self, school_db):
        init_db = SchoolInitializer()
        self.students = init_db.students
        self.courses = init_db.courses
        self.professors = init_db.professors
        self.enrollments = init_db.enrollments
        self.school_db = SchoolDB(self)

    def main(self):
        GRADE_UPDATE = 1
        PRINT_GPA = 2
        PRINT_ALL = 3
        SAVE_DATA = 4
        QUIT_MENU = 5

        choice = 0

        print("="*47)
        print("="*10, "Welcome to GPA CALC v0.12", "="*10)
        print('\t'*2, "ACEDEMIC MAIN MENU", '\t'*2)
        while choice != QUIT_MENU:
            self.menu_selections()
            choice = int(input("please select an action: "))

            if choice == GRADE_UPDATE:
                    enroll_key = int(input("Enter enroll ID: "))
                    if enroll_key in self.enrollments:
                        enroll = self.enrollments.get(enroll_key)
                        grade = input("Enter grade: ")
                        enroll.grade = grade
                    else:
                        print("Enroll ID not found: ")
                    keep_going = input("continue? y/n: ")
            elif choice == PRINT_GPA:
                student_id = int(input("enter student ID: "))

                if student_id in self.students:
                    student = self.students.get(student_id)
                    transcript = Transcript(self.enrollments)
                    transcript.print_transcript(student)
                else:
                    print("Student ID not found")
            elif choice == PRINT_ALL:
                for enrollment in self.enrollments.values():
                    enrollment.print_record()
            elif choice == SAVE_DATA:
                self.school_db.save_data()
            

    def menu_selections(self):
        print("1: update a student's grades",'\n'\
              "2: print a student's transcript", '\n'\
              "3: print full enrollment list", '\n'\
              "4: Save enrollments to database", '\n'\
              "5: Quit")
school_db = SchoolDB(SchoolInitializer())
gradebook = Gradebook(school_db)
gradebook.main()
