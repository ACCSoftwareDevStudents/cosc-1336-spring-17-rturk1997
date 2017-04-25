from tkinter import Frame
from tkinter.ttk import Label

class EnrollmentFrame(Frame):
    """Frame container for the enrollment data entry screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)

        Label(self, text="Enrollment Frame").grid(row=0, column=0, sticky="w")
