
from student import Student
from course import Course
from enrollment import Enrollment
class Transcript:
    def __init__(self, enrollments, students):
        self.enrollments = enrollments
        self.students = students
    def print_transcript(self):

        s = Student
        c = Course
        e = Enrollment 
        print(s.first_name," ",s.last_name)
        for key in self.enrollments:
            if self.enrollments[key].student_id == self.student_id:
                self.credit_points = self.__get_credit_points(self, e.letter_grade)
                self.total_credit_points += self.credit_points
                if self.credit_points.isdigit() == True:
                    self.grade_points = self.credit_points * c.credit_hour
                else:
                    self.grade_points = " "
                self.total_credit_hours += c.credit_hour
            lines_indiv += (c.title, c.credit_hour,self.credit_points, self.grade_points,'\n')  
            print("Class", "Credit Hours", "Credit Points", "Grade Points", "Grade", format(sep='\t'))
            print(lines_indiv)
            print("="*30)
            print('\t', self.total_credit_hours, '\t', self.total_credit_points)
            if self.total_credit_hours >= 1:
                print("GPA: " + format((self.total_credit_points/self.total_credit_hours),'.2f'))
            else:
                print("GPA: ")
        else:
            print("ID not found")

    def __get_credit_points(self, letter_grade):
##        see your homeworks for get credit points if block
        if letter_grade == 'A' or letter_grade == 'a':
            return '4'
        elif letter_grade == 'B' or letter_grade == 'b':
            return '3'
        elif letter_grade == 'C' or letter_grade == 'c':
            return '2'
        elif letter_grade == 'D' or letter_grade == 'd':
            return '1'
        elif letter_grade == 'F' or letter_grade == 'f':
            return '0'
        elif letter_grade == 'W' or letter_grade == 'w':
            return " "





