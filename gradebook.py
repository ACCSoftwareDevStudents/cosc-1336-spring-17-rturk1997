
from person import Person
from course import Course
from student import Student
from professor import Professor
from enrollment import Enrollment
from transcript import Transcript

class Gradebook:

    def __init__(self):
        self.students = {}

        #add to student dictionary
        s = Student(1, "Carson", "Alexander", "09012005")
        self.students[s.student_id] = s
        s = Student(2, "Meredith", "Alonso", "09022002")
        self.students[s.student_id] = s
        s = Student(3, "Arturo", "Anand", "09032003")
        self.students[s.student_id] = s
        s = Student(4, "Gytis", "Barzdukas", "09012001")
        self.students[s.student_id] = s
        s = Student(5, "Peggy", "Justice", "09012001")
        self.students[s.student_id] = s
        s = Student(6, "Laura", "Norman", "09012003")
        self.students[s.student_id] = s
        s = Student(7, "Nino", "Olivetto", "09012005")
        self.students[s.student_id] = s

        self.professors = {}

        #professor_id   first_name   last_name  hire_date
        p = Professor(1, "Kim", "Abercrombie", "1995-03-11") 
        self.professors[p.professor_id] = p

        p = Professor(2, "Fadi", "Fakhouri", "2002-07-06") 
        self.professors[p.professor_id] = p

        p = Professor(3, "Roger", "Harui", "1998-07-01") 
        self.professors[p.professor_id] = p

        p = Professor(4, "Candace", "Kapoor", "2001-01-15")
        self.professors[p.professor_id] = p

        p = Professor(5, "Roger", "Zheng", "2004-02-12") 
        self.professors[p.professor_id] = p

        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3, self.professors[1])
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3, self.professors[3])
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3, self.professors[3])
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4, self.professors[4])
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4, self.professors[4])
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3, self.professors[2])
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4, self.professors[5])
        self.courses[c.course_id] = c


        self.enrollments = {}

        #add enrolled students into courses
        enroll_id = 11050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 21045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 23141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[3141])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 22021 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[4041])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 31050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[3], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 41050 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[1050])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 44022 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[4022])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 54041 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[5], self.courses[2021])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 61045 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[6], self.courses[1045])
        self.enrollments[enroll_id] = enrollment

        enroll_id = 73141 #combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[7], self.courses[3141])
        self.enrollments[enroll_id] = enrollment

        


    def main(self):
        GRADE_UPDATE = 1
        PRINT_GPA = 2
        PRINT_ALL = 3
        QUIT_MENU = 4
        TEST = 5
        choice = 0

        print("="*47)
        print("="*10, "Welcome to GPA CALC v0.11", "="*10)
        print('\t'*2, "ACEDEMIC MAIN MENU", '\t'*2)
        while choice != QUIT_MENU:
            self.menu_selections()
            choice = int(input("please select an action: "))

            if choice == GRADE_UPDATE:
                keep_going = 'y'
                while keep_going == 'y':
                    enroll_key = int(input("Enter enroll ID: "))
                    if enroll_key in self.enrollments:
                        enroll = self.enrollments.get(enroll_key)
                        grade = input("Enter grade: ")
                        enroll.grade = grade
                    else:
                        print("Enroll ID not found: ")
                    keep_going = input("continue? y/n: ")
            elif choice == PRINT_GPA:
                input_id = int(input("enter student ID: "))
                s = self.students.get(input_id)
                #print(s)
                for key in self.students.values():
                    if input_id == s.student_id:
                        transcript = Transcript(self.enrollments, self.students)
                        transcript.print_transcript()
                    else:
                        print("ID not found")
            
            elif choice == PRINT_ALL:
                for enrollment in self.enrollments.values():
                    enrollment.print_record()
            elif choice == TEST:#testing weither or not the dictionary is being properly populated. currently returns [none]
                print(self.students.get(1).student_id, '\n',self.courses.values(),'\n', self.professors.values(),'\n',self.enrollments.values())

    def menu_selections(self):
        print("1: update a student's grades",'\n'\
              "2: print a student's transcript", '\n'\
              "3: print full enrollment list", '\n'\
              "4: quit")
gradebook = Gradebook()
gradebook.main()
