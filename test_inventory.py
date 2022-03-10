# import unittest
# #TODO: from <name_of_file> import <name_of_class> (example below)
# from inventory import Inventory
# #attributes: product_name, quantity, price (feel free to add more when you are coding - just let me know what you update)

# class TestInventory(unittest.TestCase):
#   def test_values(self):
#     self.assertRaises(ValueError, Inventory, "Lotion", -200, 3.50)
#     self.assertRaises(ValueError, Inventory, "Lotion", 200, -3.50)
#     self.assertRaises(ValueError, Inventory, "Lotion", -200, -3.50)
    
#   def test_types(self):
#     self.assertRaises(TypeError, Inventory, "Lotion", "200", "3.50")
#     self.assertRaises(TypeError, Inventory, 10, "200", "3.50")
#     self.assertRaises(TypeError, Inventory, "Lotion", 200, "3.50")
#     self.assertRaises(TypeError, Inventory, "Lotion", "200", 3.50)
#     self.assertRaises(TypeError, Inventory, 10, 200, 3.50) 
import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):
  def setUp(self):
    self.test_inventory = Inventory("Jane", "Doe", 12345)

  def test_employee_articles(self):
    #checks to see if the datatypes entered are correct
    self.assertRaises(TypeError, Inventory, 12345, "Doe", 12345)
    self.assertRaises(TypeError, Inventory, "Jane", 12345, 12345)
    self.assertRaises(TypeError, Inventory, "Jane", "Doe", "12345")
    self.assertRaises(ValueError, Inventory, "Jane", "Doe", -12345)

  def test_add_item(self):
    #checks to see if the add_item method is working and that all datatypes entered are correct
    self.assertEqual(self.test_inventory.add_item, "Jergens Smoothing Aloe", 200, "200 of Jergens Smoothing Aloe has been added to stock")
    self.assertEqual(self.test_inventory.add_item, "Jergens Cloud Creme", 250, "250 of Jergens Cloud Creme has been added to stock")
    self.assertEqual(self.test_inventory.add_item, "Jergens Dry Skin", 100, "100 of Jergens Dry Skin has been added to stock")
    self.assertRaises(TypeError, self.test_inventory.add_item, 12345, 200)
    self.assertRaises(ValueError, self.test_inventory.add_item, "Lotion", -200)
    self.assertRaises(TypeError, self.test_inventory.add_item, "Lotion", "200")
    self.assertEqual(self.test_inventory.add_item, "Jergens Smoothing Aloe", 200, "Item already in stock")
  
  def test_remove_item(self):
    #checks to see if the remove_item method is working and that all datatypes entered are correct
    self.assertEqual(self.test_inventory.remove_item, "Lotion", "Item is not in stock")
    self.assertRaises(TypeError, self.test_inventory.remove_item, 200)
    self.assertEqual(self.test_inventory.remove_item, "Jergens Smoothing Aloe", "Jergens Smoothing Aloe has been removed")
    
  def test_add_item_stock(self):
    #checks to see if the add_item_stock method is working and that all datatypes entered are correct
    self.assertEqual(self.test_inventory.add_item, "Jergens Dry Skin", 150, "150 of Jergens Dry Skin has been added to stock")
    self.assertRaises(TypeError, self.test_inventory.add_item, 12345, 200)
    self.assertRaises(TypeError, self.test_inventory.add_item, "Jergens Dry Skin", "150")
    self.assertRaises(ValueError, self.test_inventory.add_item, "Jergens Dry Skin", -200)
    self.assertEqual(self.test_inventory.add_item, "Jergens Instant Sun", 250, "250 of Jergens Instant Sun has been added to stock")

  def test_remove_item_stock(self):
    #checks to see if the remove_item_stock method is working and that all datatypes entered are correct
    self.assertRaises(TypeError, self.test_inventory.add_item, 12345, 200)
    self.assertRaises(TypeError, self.test_inventory.add_item, "Jergens Dry Skin", "150")
    self.assertRaises(ValueError, self.test_inventory.add_item, "Jergens Dry Skin", -200)
    self.assertEqual(self.test_inventory.remove_item, "Lotion", "That item is currently not in our inventory")
    self.assertEqual(self.test_inventory.remove_item, "Jergens Dry Skin", "Jergens Dry Skin was removed from stock")

  def test_check_item_stock(self):
    #checks to see if the check_item_stock method is working and that all datatypes entered are correct
    self.assertRaises(TypeError, self.test_inventory.add_item, 12345)
    self.assertEqual("Jergens Instant Sun", "There is currently 250 of Jergens Instant Sun in stock")
    self.assertEqual("Lotion", "Jergens Dry Skin is currently not in our inventory")
    self.assertEqual("Jergens Dry Skin", "Jergens Dry Skin is currently out of stock")
