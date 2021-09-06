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