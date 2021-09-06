from password import User
from password import Credentials

def create_user(login_name,pword):
    """
    This is a function that creates a new user 
    """
    new_credentials=Credentials(login_name,pword)
    return new_credentials

def save_credentials(credentials):
    """
    This is a function to save credentials
    """
    credentials.save_credentials()

def del_credentials(credentials):
    """
    Function to delete a credential
    """
    credentials.delete_credentials()

def display_credentials():
    """
    Function that returns a list of saved credentials
    """
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to your password list. What is your name?")
    login_name = input()

    print(f"Hello {login_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new credentials, dc - display credentials, del - deleting a credential, ex -exit the password list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credentials")
                            print("-"*10)

                            print ("Login Name ....")
                            login_name = input()

                            print("Password ...")
                            p_text = input()

                            save_credentials(create_user(login_name,p_text)) # create and save new contact.
                            print ('\n')
                            print(f"New Credentials {login_name} {p_text} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credentials in display_credentials():
                                            print(f"{Credentials.login_name} {Credentials.pword}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")