from tkinter import LEFT
from tkinter.ttk import Frame, Button

class NavigationBar(Frame):

    def __init__(self, parent, data_source):
        Frame.__init__(self, parent)
        self.data_source = data_source

        self.init_form()

    def init_form(self):
        b1 = Button(self,text="Next   ", command=self.__on_next)
        b2 = Button(self,text="Update ", command=self.__on_update)
        b3 = Button(self,text="Delete ", command=self.__on_delete)
        b4 = Button(self,text="Previous", command=self.__on_previous)
        b5 = Button(self,text="Search", command=self.master.on_search)
        b1.pack(side=LEFT); b2.pack(side=LEFT)
        b3.pack(side=LEFT); b4.pack(side=LEFT); b5.pack(side=LEFT)

    def __on_next(self):
        self.data_source.next_record()

    def __on_update(self):
        self.data_source.request_update()

    def __on_delete(self):
        pass

    def __on_previous(self):
        self.data_source.previous_record()
