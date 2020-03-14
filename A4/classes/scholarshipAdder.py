from .scholarship import Scholarship
from .dataBase import DataBase

class ScholarshipAdder():

    def __init__(self):

        self._dataBase = DataBase()

    # Write a new scholarship to the Excel sheet
    def add(self):
        
        desc = input("\nEnter Scholarship Description: \n")
        amount = input("\nEnter Scholarship Amount: \n")

        if not self._validScholarship(desc, amount):
            print("\nInvalid Scholarship Input. Please try again")
            return
        
        scholarship = Scholarship()
        scholarship.setScholarship(desc, amount)
        self._storeScholarship(scholarship)

        print(f'\nSuccessfully added scholarship: {scholarship.toString()}\n\n')


    # When a new scholarship is created, write it to the database
    def _storeScholarship(self, scholarship):

        data = (scholarship._description, scholarship._amount)
        sql = ''' INSERT INTO scholarships(description,amount)
              VALUES(?,?) '''
        c = self._dataBase.dbConnection.cursor()
        c.execute(sql, data)
        self._dataBase.dbConnection.commit()
        c.close()

    # Helper function to validate user input
    def _validScholarship(self, desc, amount):

        return len(desc) > 0 and amount.isdigit() and int(amount) > 0

    