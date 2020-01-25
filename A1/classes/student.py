from openpyxl import load_workbook


class Student():
    def __init__(self, studentID):

        attributes = self._getStudentAttributes(studentID)
        if not attributes:
            return False
        
        self.studentID = attributes[0].value
        self._firstName = attributes[1].value
        self._lastName = attributes[2].value
        self._email = attributes[3].value
        self.status = attributes[4].value
        self.college = attributes[5].value
        self._major = attributes[6].value
        self.citizenship = attributes[7].value
        self.gpa = attributes[8].value
        self.familyIncome = attributes[9].value

    def _getStudentAttributes(self, studentID):
        
        wb = load_workbook('dataFiles/dataFile.xlsx')
        sheet = wb['Students']

        for row in sheet.iter_rows():
            if row[0].value == studentID:
                return row
        return False



