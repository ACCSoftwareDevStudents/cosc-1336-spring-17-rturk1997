from tkinter import Frame
from tkinter.ttk import Label


from gui.component.datasource import DataSource
from gui.component.datagrid import DataGrid
from gui.component.enrollmentdictionary import EnrollmentDictionary
from gui.component.searchdialog import SearchDialog
from gui.component.textbox import TextBox
from gui.component.navigationbar import NavigationBar


class EnrollmentFrame(Frame):
    """Frame container for the enrollment data entry screen"""

    def __init__(self, parent, school_db):
        Frame.__init__(self, parent)
        self.school_db = school_db

        self.__init_form()
        
        self.bind("<<next_record>>", lambda e: self.on_next_record())
        self.bind("<<previous_record>>", lambda e:self.on_previous_record())
        self.bind("<<navigate_record>>", lambda e:self.__on_navigate())
        self.bind("<<update_record>>", lambda e:self.on_update())

        self.__on_navigate()

    def __init_form(self):
        
        self.d = EnrollmentDictionary(self.school_db.school_initializer.enrollments)
        self.data_source = DataSource(self, self.d)
        Label(self, text="Id").grid(row=0, column=0, sticky="w")
        self.id_text_box = TextBox(self, "",self.data_source, 0)
        self.id_text_box.grid(row = 0, column = 0, sticky = 'e')

        Label(self, text = "Student").grid(row = 1, column = 0, sticky = "w")
        self.student_text_box = TextBox(self, "",self.data_source, 2)
        self.student_text_box.grid(row = 1, column = 0, sticky = 'e')

        Label(self, text = "Course").grid(row = 2, column = 0, sticky = "w")
        self.course_text_box = TextBox(self, "",self.data_source, 1)
        self.course_text_box.grid(row = 2, column = 0, sticky = 'e')

        Label(self, text = "Grade").grid(row = 3, column = 0, sticky = "w")
        self.grade_text_box = TextBox(self, "",self.data_source, 3)
        self.grade_text_box.grid(row = 3, column = 0, sticky = 'e')

        navigation = NavigationBar(self, self.data_source)
        navigation.grid(row = 4)

        self.data_grid=DataGrid(self, ['Id', 'Course', 'Student', 'Grade'], self.data_source)
        self.data_grid.grid(row = 5, columnspan = 2, sticky = 'nsew')

    def on_search(self):
        search_string = SearchDialog(self, "Enter Enroll ID: ").show()
        enrollment_list = self.data_source.data[int(search_string)]
        self.data_source.set_current_record(enrollment_list[0])
        self.data_grid.on_set_record(enrollment_list[0])                
    def on_next_record(self):
        self.__on_navigate()
        self.data_grid.on_next_record()

    def on_previous_record(self):
        self.__on_navigate()
        self.data_grid.on_previous_record()
        
    def __on_navigate(self):
        self.id_text_box.on_data_source_change()
        self.student_text_box.on_data_source_change()
        self.course_text_box.on_data_source_change()
        self.grade_text_box.on_data_source_change()
    def on_update(self):
        enrollment_list = self.data_source.data[int(self.id_text_box.value.get())]
        enrollment_list[3] = self.grade_text_box.value.get()

        enrollment = self.school_db.school_initializer.enrollments[enrollment_list[0]]
        enrollment.grade = self.grade_text_box.value.get()

        self.data_source.update_record(enrollment_list)
        self.data_grid.on_update_record(enrollment_list)
