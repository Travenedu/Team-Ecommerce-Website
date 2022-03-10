import unittest
#TODO: from <name_of_file> import <name_of_class> (example below)
from cart import Cart

class Testcart(unittest.TestCase):

  def setUp(self):
    self.customer1 = Cart("Jullian", "Myers")
    self.customer2 = Cart("Alysha", "Watson")
    
  def test_init_types(self):
    #class variable init check@
    self.assertRaises(TypeError, Cart, 12345, "tom")
    self.assertRaises(TypeError, Cart, "Jergens", 290)
    self.assertRaises(TypeError, Cart, "Jergens", "200")
    self.assertRaises(TypeError, Cart, 150, 200)
    self.assertRaises(TypeError, Cart, " ", " ")

  def test_init(self):
    #class variables accuracy check@
    self.assertEqual(self.customer1.first_name, "Jullian")
    self.assertEqual(self.customer1.last_name, "Myers")
    self.assertEqual(self.customer2.first_name, "Alysha")
    self.assertEqual(self.customer2.last_name, "Watson")
    
  def test_add_to_cart(self):
    #add_to_cart type error test@
    self.assertRaises(TypeError, self.customer1.add_to_cart, "Lotion", "10")
    self.assertRaises(TypeError, self.customer2.add_to_cart, 123, 456)
    #add_to_cart value error test@
    self.assertRaises(ValueError, self.customer1.add_to_cart, "Lotion", -10)
    
    #add_to_cart accuracy test@
    self.assertEqual(self.customer1.add_to_cart("Lotion", 10), "A quantity of 10 Lotion was added to cart")
    self.assertEqual(self.customer1.add_to_cart("Lotion", 12), "A quantity of 12 Lotion was added to cart")
    self.assertEqual(self.customer2.add_to_cart("Lotion", 7), "A quantity of 7 Lotion was added to cart")

  def total_price(self):
    #total_price accuracy test
    self.assertAlmostEqual(self.customer1.total_price(), 129.9)
    self.assertEqual(self.customer2.total_price(), 27.93)
  
  def test_remove_from_cart(self):
    #add_to_cart type error test
    self.assertRaises(TypeError, self.customer1.remove_from_cart, "Lotion", "10")
    self.assertRaises(TypeError, self.customer1.remove_from_cart, 123, 456)
     
    #add_to_cart value error test
    self.assertRaises(ValueError, self.customer1.remove_from_cart, "Lotion", -10)
    #add_to_cart accuracy test
    self.assertEqual(self.customer1.remove_from_cart("Lotion", 10), "A quantity of 10 Lotion was removed from cart")
    self.assertEqual(self.customer1.remove_from_cart("Lotion", 6), "A quantity of 6 Lotion was removed from cart")
    self.assertEqual(self.customer2.remove_from_cart("Lotion", 5), "A quantity of 5 Lotion was removed from cart")


if __name__=='__main__':
    unittest.main()

