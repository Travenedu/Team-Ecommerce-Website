import unittest

class Inventory:
    """
    This class makes up and operates the inventory of the website
    
    Attributes:
        inventory: A dictionary containing the items and stock of each item 

    Methods:
        add_item
        remove_item
        add_item_stock
        remove_item_stock
        check_item_stock
        head_count
        full_restock
    """

    def __init__(self): #def __init__(self, item, quantity):
        """Inits class with items, quantity, and price"""
        self.inventory = {}
        #self.inventory = { "Jergens Soothing Aloe": 0, "Jergens Cloud Creme": 0,"Jergens Dry Skin": 0 ,"Jergens Secret Citrius": 0 ,"Jergens Secret Lavender": 0,"Jergens Firming Glow Set": 0 , "Jergens Daily Moisterizer Glow Set": 0, "Jergens Instant Sun": 0}

    def add_item(self, item, quantity):
        """This method checks if specified item is in inventory and if it isn't it adds specified item to inventory."""
        if type(item) != str:
            raise TypeError("Incorrect item input")
        if type(quantity) != int:
            raise TypeError("Incorrect quantity input")
        if quantity < 0:
            raise ValueError("Quantity can not be a negative amount")
        if item in self.inventory:
            return "Item already in stock"
        else:
            self.inventory[item] = quantity

        return str(quantity) + " of " + item + " has been added to stock"

    def remove_item(self, item):
        """This method checks if specified item is in inventory and if it is it removes specified item from inventory"""
        if type(item) != str:
            raise TypeError("Incorrect item input")
        if item not in self.inventory:
            return "Item is not in stock"
        else:
            self.inventory.pop(item)

        return item + " has been removed"

    def add_item_stock(self, item, quantity):
        """This method checks if specified item is in inventory and if it is it adds specified quantity to stock"""
        if type(item) != str:
            raise TypeError("Incorrect item input")
        if type(quantity) != int:
            raise TypeError("Incorrect quantity input")
        if quantity < 0:
            raise ValueError("Can not add a negative amount")
        if item not in self.inventory:
            self.inventory[item] = quantity
        else:
            self.inventory[item] += quantity

        return str(quantity) + " of " + item + " was added to stock"

    def remove_item_stock(self, item, quantity):
        """This method checks if specified item is in inventory and if it is it removes specified quantity from stock"""
        if type(item) != str:
            raise TypeError("Incorrect item input")
        if type(quantity) != int:
            raise TypeError("Incorrect quantity input")
        if quantity < 0:
            raise ValueError("Can not add a negative amount")
        if item not in self.inventory:
            return "That item is currently not in our inventory"
        else:
            self.inventory[item] -= quantity

        return str(quantity) + " of " + item + " was removed to stock"

    def check_item_stock(self, item):
        """This method checks an item is in inventory and if it is it returns amount of stock"""
        if type(item) != str:
            raise TypeError("Incorrect item Input")
        
        if item not in self.inventory:
            return item + " is currently not in our inventory"
        elif self.inventory[item] == 0:
            return item + " is currently out of stock"
        else:
            return "There is currently " + str(self.inventory[item]) + " of " + item + " in stock"

    def head_count(self):
        """This method does a head count of all the products together and of them individualy"""
        product_count = 0
        product_quantity = 0
        for product, value in self.inventory.items():
            product_count += 1
            product_quantity += value
            print(product + " has " + str(value) + " in stock")

        return "There is a total of " + str(product_count) + " products in stock at a total of " + str(product_quantity)

    def full_restock(self):
        """This method restocks everything in inventory to its maximum stock"""
        for product_value in self.inventory.values():
            self.inventory[product_value] = 100

        return "Everything is fully restocked"



#employ = Inventory()

#print(employ.add_item("Soap", 13))
#print(employ.add_item("Face Wipes", 103))
#print(employ.add_item("Shampoo", 43))
#print(employ.head_count())
