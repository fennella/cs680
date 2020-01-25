from openpyxl import load_workbook

class Scholarship():
    
    def __init__(self, scholarshipID):
        dataFile = load_workbook('dataFiles/dataFile.xlsx')
        self._scholarshipSheet = dataFile['Scholarships']
        self.scholarshipID = scholarshipID
        attributes = self._getAttributes()
        self.name = attributes[1].value
        self.description = attributes[2].value
        self.studentType = attributes[3].value
        self.dollarAmount = attributes[4].value
        self.type = attributes[5].value
        self.citizenship = attributes[6].value
        self.eligColleges = attributes[7].value
        self.minGPA = float(attributes[8].value)
        self.amountAvailable = int(attributes[9].value)
        self.maxFamilyIncome = int(attributes[10].value)

    def _getAttributes(self):
        
        for i,row in enumerate(self._scholarshipSheet.iter_rows()):
            if i == 0: continue
            if int(row[0].value) == self.scholarshipID:
                return row


