from openpyxl import load_workbook
from .scholarship import Scholarship
from .application import Application

class Admin():

    def __init__(self):

        self._adminID = self._getAdminID()
        self._dataFile = load_workbook('dataFiles/dataFile.xlsx')
        self._scholarshipSheet = self._dataFile['Scholarships']
        self._studentSheet = self._dataFile['Students']
        self._applicationSheet = self._dataFile['Applications']
        self._applicationPrivileges = Application(self._adminID)

    def accessScholarshipInfo(self):

        headers = self._scholarshipSheet[1]
        
        print("\n")
        for i,row in enumerate(self._scholarshipSheet.iter_rows()):
            if i == 0: continue
            for j in range(0, len(row)):
                print(f'{headers[j].value}: {row[j].value}', end=", ")
            print("\n")

    def viewAvailableScholarships(self):

        foundAvailable = False
        print("\n")
        for i, row in enumerate(self._scholarshipSheet.iter_rows()):
            if i == 0: continue
            if int(row[9].value) > 0:
                foundAvailable = True
                print(f'Scholarship ID: {row[0].value}, Name: {row[1].value}, Remaining Scholarships: {row[9].value}')
        if not foundAvailable:
            print("There are no available scholarships to be awared to students")

    def viewEligibleStudents(self):

        self.accessScholarshipInfo()
        selection = input("Enter the scholarship ID of the scholarship you'd like to view available students for: ")
        if not self._isValidScholarshipSelection(selection):
            print("Invalid Selection. Please try again")
            self.viewEligibleStudents()
        
        scholarship = Scholarship(int(selection))
        if scholarship.type == "Academic":
            validStudents = self._academicFilter(scholarship)
        else: 
            validStudents = self._financialFilter(scholarship)
        
        if len(validStudents) > 0:
            print(f'Eligible Students for the {scholarship.name}\n')
            print("-----------------------------------------------------------")
            for student in validStudents:
                print("\n")
                for attr in student.keys():
                    print(f'{attr}:{student[attr]}', end=", ")
        else:
            print("No students are eligible for this scholarship")

        print("")

    def _academicFilter(self, scholarship):

        validStudents = []
        for i, row in enumerate(self._studentSheet.iter_rows()):
            if i == 0: continue
            if scholarship.studentType != "All":
                if scholarship.studentType != row[4].value: continue
            if scholarship.citizenship != row[7].value: continue
            if scholarship.minGPA > float(row[8].value): continue
            if scholarship.eligColleges != "All":
                if scholarship.eligColleges != row[5].value: continue
            student = {
                "Student ID":row[0].value,
                "Name":row[1].value + " " + row[2].value,
                "Email":row[3].value,
                "Status":row[4].value,
                "GPA":float(row[8].value)
            }
            validStudents.append(student)

        return sorted(validStudents, key=lambda k: k['GPA'], reverse=True)
                
    def _financialFilter(self, scholarship):
        
        validStudents = []
        for i, row in enumerate(self._studentSheet.iter_rows()):
            if i == 0: continue
            if scholarship.studentType != "All":
                if scholarship.studentType != row[4].value: continue
            if scholarship.citizenship != row[7].value: continue
            if scholarship.eligColleges != "All":
                if scholarship.eligColleges != row[5].value: continue
            if scholarship.maxFamilyIncome < row[9].value: continue
            student = {
                "Student ID":row[0].value,
                "Name":row[1].value + " " + row[2].value,
                "Email":row[3].value,
                "Status":row[4].value,
                "GPA":float(row[8].value)
            }
            validStudents.append(student)

        return sorted(validStudents, key=lambda k: k['GPA'], reverse=True)

    def _isValidScholarshipSelection(self, selection):

        if not selection.isdigit() or int(selection) < 1 or int(selection) > self._scholarshipSheet.max_row - 1:
            return False
        return True
        
    def _getAdminID(self):

        adminID = input("Enter Your Admin ID: ")
        if len(adminID) < 1 or len(adminID) > 10:
            print("Invalid Admin ID. Please try again")
            self.getAdminID()

        return adminID
        
        
    



            




        

            

    

