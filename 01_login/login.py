""" 
    1. create account with email, username and password and save the details in text file
    2. get username and password from user
    3. validate the credentials stored against the text file 
"""
import getpass
import pwinput
from pyfiglet import figlet_format


def get_credentials():
    login_in = input("Do you want to create a new account[Y/n]:")

    if login_in.lower() == 'y':
        # create a new account
        email = input("Email:")
        username = input("Username: ")
        password = pwinput.pwinput()
        try:
            with open("C:/Users/user/passwords/login_details.txt", "a") as file:
                credentials = f"{email},{username},{password}\n"
                file.write(credentials)
                print("Account created successfully!")
        except:
            print("File path is incorrect.Cannot create the account!")
    elif login_in.lower() == 'n':
        username = input("Username: ")
        # password = input("Password: ")  # mask the password while typing
        # password = getpass.getpass()  # this will not mask instead it will be blank
        password = pwinput.pwinput()  # this will mask the password while typing

        try:
            with open("C:/Users/user/passwords/login_details.txt", "r") as file:
                for line in file:
                    contents = line.rstrip().split(",")
                    if username == contents[1].strip() and password == contents[2].strip():
                        result = True
                        break
                    else:
                        result = False
                if result:
                    print("Logged in successfully!")
                else:
                    print("Your credentials didn't match!")
        except:
            print("File not found!")
    else:
        print("Invalid input.Please try again!!!")


header = figlet_format("Login")
print(header)
get_credentials()
