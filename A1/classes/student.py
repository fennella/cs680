from openpyxl import load_workbook
from .dataFiles import DataFiles

class Student():

    def __init__(self, studentID=None):

        self._dataFiles = DataFiles()

        if studentID is None:
            self.studentID = self._getStudentID()
        else: self.studentID = studentID

        attributes = self._getStudentAttributes()
    
        self._firstName = attributes[1].value
        self._lastName = attributes[2].value
        self._email = attributes[3].value
        self.status = attributes[4].value
        self.college = attributes[5].value
        self._major = attributes[6].value
        self.citizenship = attributes[7].value
        self.gpa = attributes[8].value
        self.familyIncome = attributes[9].value

    def _getStudentAttributes(self):

        for row in self._dataFiles.studentSheet.iter_rows():
            if row[0].value == self.studentID:
                return row
        return False

    def _getStudentID(self):

        while True:
            studentID = input("Enter the student ID of the student you would like to select: ")
            if not self._validateStudentID(studentID):
                print("Invalid student ID. Please enter a valid student ID. Please try again.\n")
            else: return studentID
    
    def _validateStudentID(self, studentID):

        if len(studentID) < 1 or len(studentID) > 7: return False
        for row in self._dataFiles.studentSheet.iter_rows():
            if row[0].value == studentID: return True
        return False




