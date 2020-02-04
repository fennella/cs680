from classes.client import Client

def main():

    client = Client()

    print("Welcome to Drexel's Scholarship Manager")
    print("-----------------------------------------\n")

    while True:

        client.run()

main()