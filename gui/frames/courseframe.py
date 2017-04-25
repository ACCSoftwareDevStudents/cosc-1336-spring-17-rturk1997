from tkinter import Frame
from tkinter.ttk import Label

class CourseFrame(Frame):
    """Frame container for the course data entry screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        Label(self, text="Course Frame").grid(row=0, column=0, sticky="w")
