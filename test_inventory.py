import unittest
#TODO: from <name_of_file> import <name_of_class> (example below)
from inventory import Inventory
#attributes: product_name, quantity, price (feel free to add more when you are coding - just let me know what you update)

class TestInventory(unittest.TestCase):
  def test_values(self):
    self.assertRaises(ValueError, Inventory, "Lotion", -200, 3.50)
    self.assertRaises(ValueError, Inventory, "Lotion", 200, -3.50)
    self.assertRaises(ValueError, Inventory, "Lotion", -200, -3.50)
    
  def test_types(self):
    self.assertRaises(TypeError, Inventory, "Lotion", "200", "3.50")
    self.assertRaises(TypeError, Inventory, 10, "200", "3.50")
    self.assertRaises(TypeError, Inventory, "Lotion", 200, "3.50")
    self.assertRaises(TypeError, Inventory, "Lotion", "200", 3.50)
    self.assertRaises(TypeError, Inventory, 10, 200, 3.50) 
