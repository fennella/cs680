from .studentManager import StudentManager
from .scholarshipManager import ScholarshipManager


# Facade to access manager classes
class SystemFacade():

    def __init__(self):

        self._studentManager = StudentManager()
        self._scholarshipManager = ScholarshipManager()
        
    def displayAllStudents(self):
        
        self._studentManager.displayer.display()
        
    def enterNewStudent(self):
        
        self._studentManager.adder.add()
    
    def displayAllScholarships(self):

        self._scholarshipManager.displayer.display()
    
    def enterNewScholarship(self):

        self._scholarshipManager.adder.add()
