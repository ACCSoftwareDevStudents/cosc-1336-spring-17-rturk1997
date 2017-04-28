from tkinter import Frame
from tkinter.ttk import Label

class AboutFrame(Frame):
    """Frame container for the About screen"""

    def __init__(self, parent):
        Frame.__init__(self, parent)
        label_text = "Inspired by Microsoft's Contoso University example program \n",\
        "LINK HERE \n",\
        "NOT ORIGINAL WORK"

        Label(self, text=label_text).grid(row=0, column=0, sticky="w")
