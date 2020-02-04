from .studentManager import StudentManager
from .scholarshipManager import ScholarshipManager

# Facade to access manager class
class SystemFacade():

    def __init__(self):

        self._studentManager = StudentManager()
        self._scholarshipManager = ScholarshipManager()
    
    def displayAllStudents(self):
        
        self._studentManager.displayStudentList()

    def enterNewStudent(self):
        
        self._studentManager.addStudent()
    
    def displayAllScholarships(self):

        self._scholarshipManager.displayScholarshipList()
    
    def enterNewScholarship(self):

        self._scholarshipManager.addScholarship()