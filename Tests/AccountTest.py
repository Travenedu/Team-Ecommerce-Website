import unittest
from Classes.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        try:
            self.user1 = Account("Abbymercy1","Love23","abbymercy@gmail.com", 1, 2000)
        except:
            print("\nYou must edit the Account class to be instance variable: username, password, email, month, day")
            raise
        self.user2 = Account("Camida2", "Damie23", "demicami@yahoo.com", 3, 2005)
    def test_type(self):
        self.assertRaises(TypeError, Account, False, "Love123", "abbymercy@gmail.com", 2, 2005)
        self.assertRaises(TypeError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 1, 2000)
        try:
            self.assertRaises(TypeError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", "month", 2000)
        except AssertionError as e:
            print("\nmonth should be an integers. Raise Typeerror if the user input a string")
            raise
        self.assertRaises(TypeError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", "month", "2000")
      
        try:
            self.assertRaises(TypeError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 2000, "month")
        except AssertionError as e:
            print("year should be an integers. Raise Typeerror if the user input a string")
            raise
        self.assertRaises(TypeError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", "month", "2000")


      
    def test_type2(self):
            #checking for value error
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 2, -2000)
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 3, 2 )
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", -2, -2019 )
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 0, 0000)
        #year 2005 should be the max of the year
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 2, 2006)
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 2)
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 2, 20 )
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com",13, 2002)
        self.assertRaises(ValueError, Account, "Abbymercy1", "Love23", "abbymercy@gmail.com", 2, 2032)


      
    def test_email(self):
        self.assertEqual(self.user1.email, "abbymerci@gmail.com")
        self.assertEqual(self.user2.email, "demicami@yahoo.com")       

      
    def test_username(self):
        self.assertRaises(ValueError, self.user1.username, 111111)
        self.assertRaises(ValueError, self.user1.username, 1.543 )

        
        
        
        
    
        
        
        
        
        
        
        
      
    
        
  