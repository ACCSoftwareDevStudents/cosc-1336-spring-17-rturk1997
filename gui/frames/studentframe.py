from tkinter import Frame
from tkinter.ttk import Label

class StudentFrame(Frame):
    """Frame container for the student data entry screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        Label(self, text="Student Frame").grid(row=0, column=0, sticky="w")
