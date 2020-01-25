from classes.admin import Admin
from classes.client import Client

    
def main():

    print("\nWelcome to Drexel's Scholarship Management Program")
    print("---------------------------------------------------")

    client = Client()
    admin = Admin()

    while True:

        selection = client.getSelection()
        client.performAdminAction(admin, selection)


main()