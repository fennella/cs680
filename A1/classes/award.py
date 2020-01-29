from openpyxl import load_workbook
from datetime import date
from .dataFiles import DataFiles
from .application import Application

class Award():

    def __init__(self, adminID, applicationID=None):
        self._dataFiles = DataFiles()
        self._adminID = adminID
        if applicationID is None:
            self.application = self._getApplication()
        else: self.application = Application(self._adminID, applicationID)


    def awardScholarship(self):

        if self.application.scholarship.amountAvailable < 1:
            print("Unable to award scholarship. All scholarships are currently taken")
            return 
        
        self._writeNewAward()
        self._updateApplication()
        self._decrementScholarship()

        print("\nScholarship successfully awarded\n")
    
    def removeScholarship(self):

        rowNum = self._getAwardRow()
        self._dataFiles.awardSheet.cell(row=rowNum, column=6).value = False
        self._dataFiles.save()
        self._incrementScholarship()

        print("\nScholarship successfully removed\n")

    def _writeNewAward(self):

        awardID = self._genAwardPK()
        lastRow = self._dataFiles.awardSheet.max_row + 1

        self._dataFiles.awardSheet.cell(row=lastRow, column=1).value = awardID
        self._dataFiles.awardSheet.cell(row=lastRow, column=2).value = self.application.scholarship.scholarshipID
        self._dataFiles.awardSheet.cell(row=lastRow, column=3).value = self.application.student.studentID
        self._dataFiles.awardSheet.cell(row=lastRow, column=4).value = self.application.applicationID
        self._dataFiles.awardSheet.cell(row=lastRow, column=5).value = date.today()
        self._dataFiles.awardSheet.cell(row=lastRow, column=6).value = True
        self._dataFiles.awardSheet.cell(row=lastRow, column=7).value = self._adminID

        self._dataFiles.save()

    def _getAwardRow(self):

        for i,row in enumerate(self._dataFiles.awardSheet.iter_rows()):
            if i == 0: continue
            if int(row[3].value) == int(self.application.applicationID):
                return i + 1

    def _decrementScholarship(self):

        for i,row in enumerate(self._dataFiles.scholarshipSheet.iter_rows()):
            if i == 0: continue
            if int(row[0].value) == int(self.application.scholarship.scholarshipID):
                currAmount = int(self._dataFiles.scholarshipSheet.cell(row=i + 1, column=10).value)
                self._dataFiles.scholarshipSheet.cell(row=i + 1, column=10).value = currAmount - 1
                self._dataFiles.save()
                return

    def _incrementScholarship(self):

        for i,row in enumerate(self._dataFiles.scholarshipSheet.iter_rows()):
            if i == 0: continue
            if int(row[0].value) == int(self.application.scholarship.scholarshipID):
                currAmount = int(self._dataFiles.scholarshipSheet.cell(row=i + 1, column=10).value)
                self._dataFiles.scholarshipSheet.cell(row=i + 1, column=10).value = currAmount + 1
                self._dataFiles.save()
                return

    def _updateApplication(self):

        for i,row in enumerate(self._dataFiles.applicationSheet.iter_rows()):
            if i == 0: continue
            if int(row[0].value) == int(self.application.applicationID):
                self._dataFiles.applicationSheet.cell(row=i + 1, column=5).value = "Approved"
                self._dataFiles.save()
                return

    def _getApplication(self):

        while True:
            appID = input("Enter the application ID for the application you would like to access: ")
            if self._validateAppID(appID): return Application(self._adminID, appID)
            else: print("Invalid Application ID. Please try again")
        
    def _validateAppID(self, appID):

        if not appID.isdigit(): return False

        for i,row in enumerate(self._dataFiles.applicationSheet.iter_rows()):
            if i == 0: continue
            if int(row[0].value) == int(appID) and row[4].value == "Pending":
                return True
        return False

    def _genAwardPK(self):

        maxValue = 1
        for i,row in enumerate(self._dataFiles.awardSheet.iter_rows()):
            if i == 0: continue
            if maxValue < int(row[0].value):
                maxValue = int(row[0].value)

        return maxValue + 1





