from .admin import Admin
from .application import Application

class Client():

    def __init__(self):

        self._OPTIONS_DICT = {
            1:"Display Scholarship Information",
            2:"View Available Scholarships",
            3:"View Eligible Students for a Scholarship",
            4:"Create A Scholarship Application",
            5:"View Pending Applications",
            6:"Decline a Scholarship Application",
            7:"Award A Scholarship to Student",
            8:"View Active Student Scholarships",
            9:"Remove a Student Scholarship"
        }
    
    def getSelection(self):

        while True:

            print("\nEnter the number of the option you'd like to choose or 'quit' to exit\n")

            for option in self._OPTIONS_DICT:
                print(f'{option}) {self._OPTIONS_DICT[option]}')

            selection = input("\n")
            if selection == "quit": exit(1)

            elif not selection.isdigit() or int(selection) < 1 or int(selection) > len(self._OPTIONS_DICT.keys()):
                print("Invalid input. Please try again")
                
            else:
                return int(selection)

    def performAdminAction(self, admin, selection):

        if selection == 1: admin.accessScholarshipInfo()
        elif selection == 2: admin.viewAvailableScholarships()
        elif selection == 3: admin.viewEligibleStudents()
        elif selection == 4: admin.createApplication()
        elif selection == 5: admin.viewPendingApps()
        elif selection == 6: admin.declineApplication()
        elif selection == 7: admin.awardScholarship()
        elif selection == 8: admin.viewActiveScholarships()
        elif selection == 9: admin.removeScholarship()