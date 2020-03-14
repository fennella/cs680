from .studentAdder import StudentAdder
from .studentDisplayer import StudentDisplayer

class StudentManager():

    def __init__(self):
        
        self.adder = StudentAdder()
        self.displayer = StudentDisplayer()


    
