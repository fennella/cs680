from .student import Student
from .scholarship import Scholarship
from openpyxl import load_workbook
from datetime import date


class Application():

    def __init__(self, adminID):

        self._dataFile = load_workbook('dataFiles/dataFile.xlsx')
        self._studentID = None
        self._scholarshipID = None
        self._adminID = adminID
        self._applicationSheet = self._dataFile['Applications']
        self._scholarshipSheet = self._dataFile['Scholarships']
        self._studentSheet = self._dataFile['Students']
        self._awardSheet = self._dataFile['AwardedScholarships']
        
    def createApplication(self):

        self._scholarshipID = input("Enter the scholarship ID to create a scholarship application for: ")
        if not self._isValidScholarshipSelection(self._scholarshipID):
            print("Invalid input. Please enter a valid scholarship ID. Please try again. \n")
            self.createApplication()
        self._studentID = input("Enter student ID for this scholarship: ")
        if not self._isValidStudentID(self._studentID):
            print("Invalid input. Please enter a valid student ID. Please try again.\n")
            self.createApplication()
        if not self._studentQualifies(self._studentID, self._scholarshipID):
            print("Invalid student selection, this student does not qualify for this scholarship. Please try again. \n")
            self.createApplication()


        primaryKey = self._genApplicationPK()
        lastRow = self._applicationSheet.max_row + 1
        
        self._applicationSheet.cell(row=lastRow, column=1).value = primaryKey
        self._applicationSheet.cell(row=lastRow, column=2).value = self._studentID
        self._applicationSheet.cell(row=lastRow, column=3).value = self._scholarshipID
        self._applicationSheet.cell(row=lastRow, column=4).value = self._adminID
        self._applicationSheet.cell(row=lastRow, column=5).value = "Pending"

        self._dataFile.save('dataFiles/dataFile.xlsx')

        print("Successfully added application\n")
    
    def viewPendingApplications(self):

        pendingApps = []
        
        for i,row in enumerate(self._applicationSheet.iter_rows()):
            if i == 0: continue
            if row[4].value == "Pending":
                student = {
                    "Application ID":row[0].value,
                    "Student ID":row[1].value,
                    "Scholarship ID":row[2].value,
                    "Admin ID":row[3].value
                }
                pendingApps.append(student)
        
        if len(pendingApps) == 0:
            print("No pending student applications found")
            return
        
        for app in pendingApps:
            print("")
            for attr in app.keys():
                print(f'{attr}: {app[attr]}', end=", ")
        print("")

    def declineApplication(self):

        applicationID = input("Enter Application ID: ")
        rowNum = self._isValidApplication(applicationID, "Pending")
        if rowNum is False:
            print("Invalid Application ID. Please try again.\n")
            self.declineApplication()

        self._applicationSheet.cell(row=rowNum, column=4).value = self._adminID
        self._applicationSheet.cell(row=rowNum, column=5).value = "Declined"
        
        self._dataFile.save('dataFiles/dataFile.xlsx')

        print("\nScholarship Successfully Declined\n")
    
    def approveApplication(self):

        applicationID = input("Enter Application ID: ")
        rowNum = self._isValidApplication(applicationID, "Pending")
        if rowNum is False:
            print("Invalid Application ID. Please try again.\n")
            self.approveApplication()
        
        scholarship = Scholarship(int(self._applicationSheet.cell(row=rowNum, column=3).value))
        if scholarship.amountAvailable < 1:
            print("\nNo available scholarships for this scholarship\n")
            return
            

        self._applicationSheet.cell(row=rowNum, column=4).value = self._adminID
        self._applicationSheet.cell(row=rowNum, column=5).value = "Approved"

        appID = self._applicationSheet.cell(row=rowNum, column=1).value
        studentID = self._applicationSheet.cell(row=rowNum, column=2).value
        scholarshipID = self._applicationSheet.cell(row=rowNum, column=3).value

        self._awardApplication(appID, studentID, scholarshipID)
        self._decrementAmountLeft(int(scholarshipID))

        self._dataFile.save('dataFiles/dataFile.xlsx')

    def viewScholarships(self):

        awards = []
        for i,row in enumerate(self._awardSheet.iter_rows()):
            if i == 0: continue
            if row[5].value:
                award = {
                    "Award ID":row[0].value,
                    "Scholarship ID":row[1].value,
                    "Student ID":row[2].value,
                    "Application ID":row[3].value,
                    "Award Date":row[4].value
                }
                awards.append(award)
        if len(awards) == 0:
            print("\nNo scholarships are currently awarded\n")
            return
        
        for award in awards:
            print("")
            for attr in award.keys():
                print(f'{attr}: {award[attr]}', end=", ")
        print("")

    def removeScholarship(self):

        awardID = input("Enter the award ID of the scholarship to be removed from the student: ")
        rowInfo = self._isValidAwardID(awardID)
        if rowInfo is False:
            print("Invalid award ID. Please try again")
            self.removeScholarship()

        self._awardSheet.cell(row=rowInfo[0], column=6).value = False
        self._incrementAmountLeft(int(self._awardSheet.cell(row=rowInfo[0], column=2).value))

        self._dataFile.save('dataFiles/dataFile.xlsx')

        print("\nScholarship successfully removed from student\n")

    def _awardApplication(self, appID, studentID, scholarshipID):
        

        awardID = self._genAwardPK()
        lastRow = self._awardSheet.max_row + 1

        self._awardSheet.cell(row=lastRow, column=1).value = awardID
        self._awardSheet.cell(row=lastRow, column=2).value = scholarshipID
        self._awardSheet.cell(row=lastRow, column=3).value = studentID
        self._awardSheet.cell(row=lastRow, column=4).value = appID
        self._awardSheet.cell(row=lastRow, column=5).value = date.today()
        self._awardSheet.cell(row=lastRow, column=6).value = True
        self._awardSheet.cell(row=lastRow, column=7).value = self._adminID

        print("\nScholarship Successfully Awarded\n")
    
    def _studentQualifies(self, studentID, scholarshipID):

        student = Student(studentID)
        scholarship = Scholarship(int(scholarshipID))

        if scholarship.amountAvailable < 1: return False

        if scholarship.type == "Academic":
            return self._validateAcademicApp(student, scholarship)
        
        else: return self._validateFinancialApp(student, scholarship)
    
    def _validateAcademicApp(self, student, scholarship):

        if scholarship.studentType != "All":
            if scholarship.studentType != student.status: return False
        if scholarship.citizenship != student.citizenship: return False
        if scholarship.eligColleges != "All":
            if scholarship.eligColleges != student.college: return False
        if float(scholarship.minGPA) > float(student.gpa): return False
        
        return True

    def _validateFinancialApp(self, student, scholarship):

        if scholarship.studentType != "All":
            if scholarship.studentType != student.status: return False
        if scholarship.citizenship != student.citizenship: return False
        if scholarship.eligColleges != "All":
            if scholarship.eligColleges != student.college: return False
        if int(scholarship.maxFamilyIncome) < int(student.familyIncome): return False
        
        return True

    def _isValidStudentID(self, studentID):

        if len(studentID) < 1 or len(studentID) > 7: return False
        for row in self._studentSheet.iter_rows():
            if row[0].value == studentID: return True
        return False
    
    def _isValidApplication(self, applicationID, status):

        if applicationID.isdigit():
            for i,row in enumerate(self._applicationSheet.iter_rows()):
                if i == 0: continue
                if int(row[0].value) == int(applicationID) and row[4].value == status:
                    return i + 1
        return False

    def _isValidScholarshipSelection(self, selection):

        if not selection.isdigit() or int(selection) < 1 or int(selection) > self._scholarshipSheet.max_row - 1:
            return False
        return True

    def _isValidAwardID(self, awardID):

        if awardID.isdigit():
            for i,row in enumerate(self._awardSheet.iter_rows()):
                if i == 0: continue
                if int(row[0].value) == int(awardID) and row[5].value:
                    return (i + 1, int(row[1].value))
        return False

    def _genApplicationPK(self):

        maxValue = 1
        for i,row in enumerate(self._applicationSheet.iter_rows()):
            if i == 0: continue
            if maxValue < int(row[0].value):
                maxValue = int(row[0].value)

        return maxValue + 1

    def _incrementAmountLeft(self, scholarshipID):

        for i,row in enumerate(self._scholarshipSheet.iter_rows()):
            if i == 0: continue
            if int(row[0].value) == int(scholarshipID):
                amountLeft = int(self._scholarshipSheet.cell(row=i + 1, column=10).value)
                self._scholarshipSheet.cell(row=i + 1, column=10).value = amountLeft + 1
                self._dataFile.save('dataFiles/dataFile.xlsx')
                return

    def _decrementAmountLeft(self, scholarshipID):

        for i,row in enumerate(self._scholarshipSheet.iter_rows()):
            if i == 0: continue
            if int(row[0].value) == int(scholarshipID):
                amountLeft = int(self._scholarshipSheet.cell(row=i + 1, column=10).value)
                self._scholarshipSheet.cell(row=i + 1, column=10).value = amountLeft - 1
                self._dataFile.save('dataFiles/dataFile.xlsx')
                return
    
    def _genAwardPK(self):

        maxValue = 1
        for i,row in enumerate(self._awardSheet.iter_rows()):
            if i == 0: continue
            if maxValue < int(row[0].value):
                maxValue = int(row[0].value)

        return maxValue + 1