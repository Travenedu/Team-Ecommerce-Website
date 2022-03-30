#code pushed to github by Traven but work done by Alexis
import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):
  longMessage = False
  def setUp(self):
    self.test_inventory = Inventory("Jane", "Doe", 123)

  def test_employee_articles(self):
    #checks to see if the datatypes entered are correct
    self.assertRaises(TypeError, Inventory, 12345, "Doe", 123)
    self.assertRaises(TypeError, Inventory, "Jane", 12345, 123)
    self.assertRaises(TypeError, Inventory, "Jane", "Doe", "123")
    self.assertRaises(ValueError, Inventory, "Jane", "Doe", -123)

  def test_add_item(self):
    #checks to see if the add_item method is working and that all datatypes entered are correct
    self.assertEqual(self.test_inventory.add_item("Jergens Smoothing Aloe Pluto", 200),"200 of Jergens Smoothing Aloe Pluto has been added to stock")
    
    self.assertEqual(self.test_inventory.add_item("Jergens Cloud Creme 300", 250), "250 of Jergens Cloud Creme 300 has been added to stock")
    
    self.assertEqual(self.test_inventory.add_item("Jergens Dry Skin 2.0", 100), "100 of Jergens Dry Skin 2.0 has been added to stock")
    
    self.assertRaises(TypeError, self.test_inventory.add_item, 12345, 200)
    self.assertRaises(ValueError, self.test_inventory.add_item, "Lotion", -200)
    self.assertRaises(TypeError, self.test_inventory.add_item, "Lotion", "200")
    self.assertEqual(self.test_inventory.add_item("Jergens Smoothing Aloe", 200), "Item already in stock")
  
  def test_remove_item(self):
    #checks to see if the remove_item method is working and that all datatypes entered are correct
    self.assertEqual(self.test_inventory.remove_item("Lotion"), "Item is not in stock")
    self.assertRaises(TypeError, self.test_inventory.remove_item, 200)
    self.assertEqual(self.test_inventory.remove_item("Jergens Smoothing Aloe"), "Jergens Smoothing Aloe has been removed")
    
  def test_add_item_stock(self):
    #checks to see if the add_item_stock method is working and that all datatypes entered are correct
    self.assertEqual(self.test_inventory.add_item_stock("Jergens Dry Skin", 150), "150 of Jergens Dry Skin was added to stock")
    self.assertRaises(TypeError, self.test_inventory.add_item_stock, 12345, 200)
    self.assertRaises(TypeError, self.test_inventory.add_item_stock, "Jergens Dry Skin", "150")
    self.assertRaises(ValueError, self.test_inventory.add_item_stock, "Jergens Dry Skin", -200)
    self.assertEqual(self.test_inventory.add_item_stock("Jergens Instant Sun", 250), "250 of Jergens Instant Sun was added to stock")

  def test_remove_item_stock(self):
    #checks to see if the remove_item_stock method is working and that all datatypes entered are correct
    self.assertRaises(TypeError, self.test_inventory.remove_item_stock, 12345, 200)
    self.assertRaises(TypeError, self.test_inventory.remove_item_stock, "Jergens Dry Skin", "150")
    self.assertRaises(ValueError, self.test_inventory.remove_item_stock, "Jergens Dry Skin", -200)
    self.assertEqual(self.test_inventory.remove_item("Jergens Instant Sun"), "Jergens Instant Sun has been removed")
    self.assertEqual(self.test_inventory.remove_item("Jergens Dry Skin"), "Jergens Dry Skin has been removed")

  def test_check_item_stock(self):
    #checks to see if the check_item_stock method is working and that all datatypes entered are correct
    self.assertRaises(TypeError, self.test_inventory.check_item_stock, 12345)
    self.assertEqual(self.test_inventory.check_item_stock("Jergens Instant Sun"), "There is currently 100 of Jergens Instant Sun in stock")
    self.assertEqual(self.test_inventory.check_item_stock("Tooth Paste"), "Tooth Paste is currently not in our inventory")
    self.assertEqual(self.test_inventory.check_item_stock("Jergens Dry Skin 400"), "Jergens Dry Skin 400 is currently out of stock")

if __name__ == '__main__':
    unittest.main(failfast=True)
