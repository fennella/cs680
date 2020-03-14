from .student import Student
from .dataBase import DataBase

class StudentAdder():

    def __init__(self):

        self._dataBase = DataBase()
    
    # Get student input from user then write to Excel sheet
    def add(self):

        first = input("\nEnter Student First Name: ")
        last = input("\nEnter Student Last Name: ")

        if not self._validNames(first, last):
            print("Invalid name entry. Please try again")
            return

        student = Student()
        student.setStudent(first, last)
        self._storeStudent(student)

        print(f'\nSuccessfully added student: {student.toString()}\n\n')

    # Write a new student to the Excel sheet
    # New to refresh the workbook to update it in case user chooses to display students
    # after adding a new one
    def _storeStudent(self, student):

        data = (student._studentID, student._first, student._last, student._email)
        sql = ''' INSERT INTO students(studentID,firstName,lastName,email)
              VALUES(?,?,?,?) '''
        c = self._dataBase.dbConnection.cursor()
        c.execute(sql, data)
        self._dataBase.dbConnection.commit()
        c.close()


    # Helper function to validate user input of first and last name 
    def _validNames(self, first, last):

        return len(first) > 0 and len(last) > 0 and first.isalpha() and last.isalpha()