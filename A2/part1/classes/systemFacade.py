from .manager import Manager

# Facade to access manager class
class SystemFacade():

    def __init__(self):

        self._studentManager = Manager()
    
    def displayAllStudents(self):
        
        self._studentManager.displayStudentList()

    def enterNewStudent(self):
        
        self._studentManager.addStudent()
