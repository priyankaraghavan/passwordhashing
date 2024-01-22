import unittest

import getUserDetailsAndSave
import random


class TestgetUserDetailsAndSave(unittest.TestCase):

     def test_retrieveifusernameeandpasswordexistsinDb(self):
        #setup
        username="priyanka"
        password="test1234"

        #act
        result= getUserDetailsAndSave.retrieveifusernameandpasswordexistsinDb(username, password,True)
        self.assertFalse(result)

     def test_storeUsernameAndPassword(self):
        #setup
        username="priyanka"
        random_number =random.randrange(100,1000)
        random_number_str= str(random_number)
        password="test1234"+ random_number_str
        username= username+ random_number_str

        #act
        getUserDetailsAndSave.storeUsernameAndPassword(username, password,True)
        checkifusernameexist1= getUserDetailsAndSave.retrieveifusernameandpasswordexistsinDb(username,password,True)
        self.assertTrue(checkifusernameexist1)

     def test_retrieveifusernameexistsinDb(self):
        #setup
        username="brian"
        
        #act
        checkifusernameexist1= getUserDetailsAndSave.retrieveifusernameexistsinDb(username,True)
        self.assertTrue(checkifusernameexist1)
        


if __name__ == '__main__':
    unittest.main()
