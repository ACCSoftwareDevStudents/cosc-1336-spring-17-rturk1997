
from model.student import Student
from model.course import Course
from model.enrollment import Enrollment
class Transcript:
    def __init__(self, enrollments):
        self.enrollments = enrollments

    def print_transcript(self, student):
            
        print("Student: ", student.first_name," ",student.last_name)
        total_credit_hours = 0
        total_grade_points = 0
        print("Course         ", "Credit hours", "Credit Points", "Grade Points", "Letter Grade")
        for e in self.enrollments.values():
            if e.student.student_id == student.student_id:
                
                if e.grade in ["A","B","C","D","F"]:
                    total_credit_hours += e.course.credit_hours
                    
                credit_points = self.__get_credit_points( e.grade)
                
                grade_points = e.course.credit_hours * credit_points

                total_grade_points += grade_points
                
                
                print(format(e.course.title, '15'),
                      format(e.course.credit_hours, '13'),
                      format(credit_points, '12'),
                      format(grade_points, '12'),
                      format(' ' + e.grade, '12'))
            
            
            
        print("="*30)
        print(format(total_credit_hours, '26'),
              format(total_grade_points, '26'))
            
        if total_credit_hours >= 1:
            print("GPA: " + format(total_grade_points/total_credit_hours,'.2f'))
        else:
            print("GPA: ")
       

    def __get_credit_points(self, grade):
        credit_points = 0

        if grade == 'A':
            credit_points = 4
        elif grade == 'B':
            credit_points = 3
        elif grade == 'C':
            credit_points = 2
        elif grade == 'D':
            credit_points = 1

        return credit_points





