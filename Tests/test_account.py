import unittest
from Classes.account import Account

class TestAccount(unittest.TestCase):
  longMessage = False
  """The setup is an example of what the user input should look like
  """
  def setUp(self):
      self.user1 = Account("Abby","Arowolaju", "Abbymerci","Love","abbymercy@gmail.com",  1, 2000)
      self.user2 = Account("Camida", "Damie", "Damica","Sweet","demicami@yahoo.com", 3, 2005)
    
  def test_init_types(self):
      """Checks to see if there are no TypeErrors and if there are this test handles it
    """
      self.assertRaises(TypeError, Account, 2, "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 2, 2005)
      self.assertRaises(TypeError, Account, "Abby", 3, "Abbymerci", "Love123", "abbymercy@gmail.com", 2, 2005)
      self.assertRaises(TypeError, Account, "Abby", "Arowolaju", 34, "Love123", "abbymercy@gmail.com", 2, 2005)
      self.assertRaises(TypeError, Account, "Abby", "Arowolaju", 34, "Love123", 3, 2, 2005)
      self.assertRaises(TypeError, Account, "Abby", "Arowolaju", 34, "Love123", "abbymercy@gmail.com", "feb", 2005)
      self.assertRaises(TypeError, Account, "Abby", "Arowolaju", 34, "Love123", "abbymercy@gmail.com", 2, "thousand")
    



      
  def test_type2(self):
            #checking for value error
        self.assertRaises(ValueError, Account, "Abby", "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 2, -2000)
        self.assertRaises(ValueError, Account, "Abby", "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 3, 2)
        self.assertRaises(ValueError, Account, "Abby", "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 2, 0000)
        self.assertRaises(ValueError, Account, "Abby", "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 0, 0)
        #year 2005 should be the max of the year
        self.assertRaises(ValueError, Account, "Abby", "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 2, 2006)
        self.assertRaises(ValueError, Account, "Abby", "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 13, 2000)
        self.assertRaises(ValueError, Account, "Abby", "Arowolaju", "Abbymerci", "Love123", "abbymercy@gmail.com", 0, 2000)


      
  def test_email(self):
      self.assertEqual(self.user1.email, "abbymercy@gmail.com")
      self.assertEqual(self.user2.email, "demicami@yahoo.com")       

  def test_add_account(self):
    """Checks to see if account are created correctly and raises errors if they are not"""
    self.assertEqual(self.user1.add_account(), "Abbymerci's account has been created.")
    self.assertEqual(self.user2.add_account(), "Damica's account has been created.")

    

  def test_delete_account(self):
    #Check to see if account are deleted correctly and raises error if they are not
    self.assertRaises(TypeError, self.user1.delete_account, 1234, "10", {"Abbymerci":["Love", "abbymercy@gmail.com", 1, 2000]})
    self.assertRaises(TypeError, self.user2.delete_account, "Abbymerci", 1234, {"Damica":["Sweet", "demicami@yahoo.com", 3, 2005]})
    self.assertEqual(self.user1.delete_account("Abbymerci", "Love", {"Abbymerci":["Love", "abbymercy@gmail.com", 1, 2000]}), "Abbymerci's account has been deleted.")
    
    self.assertEqual(self.user2.delete_account("Damica","Sweet", {"Damica":["Sweet", "demicami@yahoo.com", 3, 2005]}), "Damica's account has been deleted.")
    self.assertEqual(self.user2.delete_account("Capital","Tim", {"Damica":["Sweet", "demicami@yahoo.com", 3, 2005]}), "User does not exist")


if __name__ == '__main__':
    unittest.main(failfast=True)
