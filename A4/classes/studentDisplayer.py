from .student import Student
from .dataBase import DataBase

class StudentDisplayer():

    def __init__(self):

        self._dataBase = DataBase()

    # Present all students in the system to the user
    def display(self):

        students = self._loadStudents()

        for row in students:
            student = self._loadStudent(row)
            print(student.toString())

    # Iterate through all students in Excel sheet and add a student object to studentList for each one
    def _loadStudents(self):

        c = self._dataBase.dbConnection.cursor()
        sql = ''' SELECT * FROM students'''
        c.execute(sql)
        students = c.fetchall()
        c.close()
        return students

    # Create student object from a row in the Excel sheet
    def _loadStudent(self, row):

        student = Student()
        student.getStudent(row)
        return student