from os.path import isfile
import pickle
class SchoolDB:
    def __init__(self,school_initializer):
        self.school_initializer = school_initializer
        self.file_name = r".\enroll.dat"
        self.data = school_initializer.enrollments
        self.load_data()

    def load_data(self):
        if(isfile(self.file_name)):
            self.file = open(self.file_name, 'rb')
            self.data = pickle.load(self.file)
            self.file.close()

            
    def save_data(self):
        self.file = open(self.file_name, 'wb')
        pickle.dump(self.data, self.file)
        self.file.close()

        
