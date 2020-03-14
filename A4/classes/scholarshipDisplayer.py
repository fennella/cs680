from .scholarship import Scholarship
from .dataBase import DataBase

class ScholarshipDisplayer():

    def __init__(self):

        self._dataBase = DataBase()
    
    # Display all scholarships to user
    def display(self):

        scholarships = self._loadScholarships()

        for row in scholarships:
            scholarship = self._loadScholarship(row)
            print(scholarship.toString())

    # Load all scholarships from database
    def _loadScholarships(self):

        c = self._dataBase.dbConnection.cursor()
        sql = ''' SELECT * FROM scholarships'''
        c.execute(sql)
        scholarships = c.fetchall()
        c.close()
        return scholarships
        
    # Initialize the scholarship object
    def _loadScholarship(self, row):

        scholarship = Scholarship()
        scholarship.getScholarship(row)
        return scholarship
