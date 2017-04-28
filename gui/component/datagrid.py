from tkinter import NO
from tkinter.ttk import Treeview

class DataGrid(Treeview):

    def __init__(self, parent, headers, data_source):
        Treeview.__init__(self, parent, columns=headers)
        self.parent = parent
        self.data_source = data_source
        self.data_dictionary = data_source.data
        self.headers = headers
        self.__create_headers()
        self.__insert_rows()
        self.selection_set('I001')
        self.current_item = 'I001'
        self.bind("<<TreeviewSelect>>", lambda e: self.on_select_record())

    def on_next_record(self):
    
        self.item = self.next(self.selection())
        self.selection_set(self.item)
        
    def on_previous_record(self):

        self.item = self.prev(self.selection())
        self.selection_set(self.item)

    def on_update_record(self, record):

        i = 0
        self.focus(self.selection()[0])

        while i < len(record):
            d = self.set(self.focus(), self.headers[i], record[i])
            i += 1

    def on_delete_record(self):
        self.focus(self.selection()[0])
        self.delete(self.focus())

    def on_select_record(self):
        
        if not self.selection() == '':
            key = self.set(self.selection()[0], 'Id')
        
            if(not key == ''):
                self.data_source.set_current_record(int(key))

    def on_set_record(self, key):

        children = self.get_children('')

        for child in children:
            text = self.item(child, 'text')

            if text == key:
                self.selection_set(child)


    def __create_headers(self):

        indx = 0
        for header in self.headers:
            self.heading(str(indx), text=header)
            self.column(str(indx), width=100, stretch=NO)
            indx += 1

    def __insert_rows(self):

        for key in self.data_dictionary:
            record = self.data_dictionary[key]
            
            self.insert('', 'end', text=record[0] , values=record)
