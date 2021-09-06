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


    
if __name__ == '__main__':
    unittest.main()