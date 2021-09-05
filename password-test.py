import unittest
from password import User
from password import Credentials

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the test user class behavior

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_username = User("Sharry","Kenyan") # create user object
    

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Mike","winning") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_username.username,"Sharry")
        self.assertEqual(self.new_username.password,"Kenyan")

    def test_save_multiple_password(self):
            '''
            test_save_multiple_passwords to check if we can save multiple credential
            objects to our password_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("username","password") # new user login and credentials 
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.password_list),2)

if __name__ == '__main__':
    unittest.main()