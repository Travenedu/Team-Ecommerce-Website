#Uploaded by Traven code done by Alexis
class Account:
  """
  This class makes up and operates the user account of the website. 
  It accepts a user's username, password, email address and birth month and year.
  This class does not accpect incorrect datatypes (e.g. an integer for a user name or a string for the birth month) and incorect value types (e.g. the user has to be born before 2005)
  """
  
  def __init__(self, first_name, last_name, user_name, password, email, month, year):
    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.password = password
    self.email = email
    self.month = month
    self.year = year

    if type(self.last_name) != str:
      raise TypeError("Incorrect input for last name")
    if type(self.first_name) != str:
      raise TypeError("Incorrect input for first name")
    if type(self.user_name) != str:
      raise TypeError("Incorrect input for user name")
      
    if type(password) != str:
      raise TypeError("Password must be a string!")
    if type(month) != int:
      raise TypeError("Birth month has to be an number")
    if type(year) != int:
      raise TypeError("Birth year has to be an number")
    if month == "" and year == "":
      raise ValueError ("Invalid input")
      
      
    
    
    elif year > 2005:
      raise ValueError("You have to be born before 2006")
    elif year <= 0 or month <= 0:
      raise ValueError("Year cannot be a negative integer")
    elif month > 12:
      raise ValueError("Month does not exist")
    elif year < 1900:
      raise ValueError("Year does not exist")
    else:
      self.month = month
      self.year = year
      self.users = {}

  def add_account(self):
    self.users = {self.user_name:[self.password, self.email, self.month, self.year]}
    return self.user_name + "'s account has been created."

  def delete_account(self, username, password, accounts):
    self.users = accounts
    if type(username) != str:
      raise TypeError("Incorrect input for user name")
    if type(password) != str:
      raise TypeError("Incorrect input for user name")
      
    for users in self.users:
      if username not in self.users:
        return "User does not exist"
      elif self.users[username][0] == password:
        self.users.pop(username)
        return username + "'s account has been deleted."
