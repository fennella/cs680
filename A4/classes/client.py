from .systemFacade import SystemFacade

class Client():

    def __init__(self):
        self._OPTIONS = {
            1:"View Students In System",
            2:"Enter A Student Into System",
            3:"Display All Scholarships",
            4:"Enter New Scholarship"
        }
        self._system = SystemFacade()
    
    # Function called from main to get user selection
    def run(self):

        self._presentOptions()

        selection = input("Enter your selection choice or 'quit' to terminate the program: \n\n")

        if selection == "quit": exit(1)

        # Validate user selection
        if not self._isValidSelection(selection):
            print("Invalid Selection. Please try again\n\n")
            return
        
        if int(selection) == 1: self._system.displayAllStudents()
        elif int(selection) == 2: self._system.enterNewStudent()
        elif int(selection) == 3: self._system.displayAllScholarships()
        elif int(selection) == 4: self._system.enterNewScholarship()

        print("\n")


    def _isValidSelection(self, selection):

        return selection.isdigit() and int(selection) in self._OPTIONS.keys()
    
    # Present formatted options for a user to chose from
    def _presentOptions(self):

        print("         SELECTIONS")
        print("-------------------------------")

        for key in self._OPTIONS.keys():
            print(f'{key}) {self._OPTIONS[key]}')
        
        print("\n")
