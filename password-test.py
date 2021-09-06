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
        self.new_user = User("Sharry","Kenyan") # create user object
    

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Mike","winning") # create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Sharry")
        self.assertEqual(self.new_user.password,"Kenyan")

    def test_init(self):
        '''
        test_init test case to test if the credentials object is initialized properly
        '''

        self.assertEqual(self.new_credentials.lname,"Mike")
        self.assertEqual(self.new_credentials.pword,"winning")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the password list
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.password_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.password_list = []
    
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our password_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","user") # new contact
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.password_list),2)
    
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.password_list)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential from our credential list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","user") # new credentials 
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credential object
            self.assertEqual(len(Credentials.password_list),1)
    


if __name__ == '__main__':
    unittest.main()