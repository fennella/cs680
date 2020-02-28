class Scholarship():

    # Initiallly set all scholarship attributes to None
    def __init__(self):

        self._id = None
        self._description = None
        self._amount = None
    
    # Set scholarship attributes when given first and last name
    def setScholarship(self, desc, amount, scholarshipID):

        self._description = desc
        self._amount = amount
        self._id = scholarshipID

    # Get scholarship attributes from a row in the Excel sheet
    def getScholarship(self, row):
        
        self._id = row[0].value
        self._description = row[1].value
        self._amount = row[2].value

    def toString(self):
        
        return f'{self._description} for ${self._amount} dollars'   
