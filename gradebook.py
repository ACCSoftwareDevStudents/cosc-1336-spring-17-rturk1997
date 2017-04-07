from enrollment import Enrollment
from course import Course
from student import Student
class Gradebook():
    def __init__(self):
        
        self.students = {}

        #add to student dictionary
        s = Student(1, "Carson", "Alexande#r", "09012005")
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


        self.courses = {}

        #add to course dictionary
        c = Course(1050, "Chemistry", 3)
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 3)
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3)
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 4)
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 4)
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 3)
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 4)
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
        keep_going = "y"
        while keep_going == "y":
            enroll_id = input("please enter enroll_id: ")
            grade_update = input("Enter a grade: ")
            if enroll_id in self.enrollments:
                self.enrollment[key].append(grade_update)
            else:
                print("error: enrollment ID not found...")
            keep_going = input("Keep going? y/n: ")
                
        for key in self.enrollments:
            print(key, self.enrollments[key])
        
        
gradebook = Gradebook()
gradebook.main()














        
