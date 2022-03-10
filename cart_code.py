"""
    This class makes up the operation of adding items to the cart, removing  items from the cart and summing up the total price of items in the cart. 
  Attribute are lastname and firstname containing the names of each customers.
  Methods:
      add_item
      remove_item
      total_price
  """
from item_dictionary import item_dict
class Cart:
  def __init__(self, first_name, last_name): 
    self.last_name = last_name
    self.first_name = first_name
    self.users_cart = {}
    if type(first_name) != str:
      raise TypeError
    if type(last_name) != str:
      raise TypeError
    if first_name == "Jergens":
      raise TypeError
    if first_name or last_name == "":
      raise TypeError
    

  def add_to_cart(self,item,quantity):
    if type(quantity) != int:
      raise TypeError(f'{quantity} must be an integer')
    if type(item) != str:
      raise TypeError(f' {item} must be a string')
    if item in item_dict and not item in self.users_cart:
      self.users_cart[item] = quantity
    elif quantity < 1:
      raise ValueError(f' {quantity} has to be greater than 0')
    elif item in self.users_cart:
      self.users_cart[item] += quantity
    else:
      raise ValueError(f' {item} not available in cart')

  def remove_from_cart(self,item,quantity):
    
    if type(quantity) != int:
      raise TypeError(f'{quantity} must be an integer')
    if type(item) != str:
      raise TypeError(f' {item} must be a string')
    elif quantity < 1:
      raise ValueError(f' {quantity} has to be greater than 0')
    elif item in self.users_cart:
      self.users_cart[item] -= quantity 
    else:
      raise ValueError(f' {item} cant remove item not available in cart')


  def total_price(self):
    total = 0
    for key, value in self.users_cart.items():
      total += item_dict[key] * value
    return total
      
      

      
      
