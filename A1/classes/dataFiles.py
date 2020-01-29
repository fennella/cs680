from openpyxl import load_workbook

class DataFiles():

    def __init__(self):

        self.workbook = load_workbook('dataFiles/dataFile.xlsx')
        self.studentSheet = self.workbook['Students']
        self.scholarshipSheet = self.workbook['Scholarships']
        self.applicationSheet = self.workbook['Applications']
        self.awardSheet = self.workbook['AwardedScholarships']
    
    def save(self):

        self.workbook.save('dataFiles/dataFile.xlsx')
