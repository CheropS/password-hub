class User:
    """
    Class that generates a login username and password for existing users
    """
    password_list = [] #empty password list

    def __init__(self, username, password):
        """
        init method that helps us define our objects

        Args: 
            username= new username.
            password = New password.
        """

        self.username= username
        self.password = password


class Credentials:
    """
    this is the class that contains user credentials for its users
    """
    password_list = [] #empty password list

    def __init__(self, login_name, pword):
        """
        init method that helps us define our objects

        Args: 
            lname= new login_name.
            pword = New password.
        """

        self.lname= login_name
        self.pword = pword


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.password_list = []

    def save_credentials(self):

        '''
        save_password method saves password objects into password_list
        '''

        Credentials.password_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved password from the password_list
        '''

        Credentials.password_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the saved credentials list
        '''
        return cls.password_list
    
    


