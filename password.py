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

    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Credentials.password_list.append(self)

    def delete_password(self):

        '''
        delete_password method deletes a saved password from the password_list
        '''

        Credentials.password_list.remove(self)
    

    def test_save_multiple_password(self):
            '''
            test_save_multiple_passwords to check if we can save multiple credential
            objects to our password_list
            '''
            self.new_credential.save_password()
            test_credentials = User("username","password") # new user login and credentials 
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.password_list),2)

if __name__ == '__main__':
    unittest.main()
