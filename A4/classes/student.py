from random import randint

class Student():

    # Initiallly set all student attributes to None
    def __init__(self):

        self._studentID = None
        self._first = None
        self._last = None
        self._email = None
    
    # Set student attributes when given first and last name
    def setStudent(self, first, last):

        self._first = first
        self._last = last
        self._studentID = self._genStudentID()
        self._email = self._studentID + "@drexel.edu"

    # Get students attributes from a row in the Excel sheet
    def getStudent(self, row):

        self._studentID = row[0]
        self._first = row[1]
        self._last = row[2]
        self._email = row[3]

    def toString(self):
        
        return f'{self._first} {self._last} ({self._studentID})'   

    def _genStudentID(self):

        return self._first[0].lower() + self._last[0].lower() + str(randint(100, 999))