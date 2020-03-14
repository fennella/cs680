class Scholarship():

    # Initiallly set all scholarship attributes to None
    def __init__(self):

        self._description = None
        self._amount = None
    
    # Set scholarship attributes when given first and last name
    def setScholarship(self, desc, amount):

        self._description = desc
        self._amount = amount
        

    # Get scholarship attributes from a row in the Excel sheet
    def getScholarship(self, row):
        
        self._description = row[1]
        self._amount = row[2]

    def toString(self):
        
        return f'{self._description} for ${self._amount} dollars'   
