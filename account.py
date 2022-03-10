lass Account:
  """
  This class makes up and operates the user account of the website. 
  It accepts a user's username, password, email address and birth month and year.
  This class does not accpect incorrect datatypes (e.g. an integer for a user name or a string for the birth month) and incorect value types (e.g. the user has to be born before 2005)
  """
  
  def __init__(self, user_name, password, email, month, year):
    if type(user_name) != str:
      raise TypeError("Name must be a string!")
    else:
      self.user_name = user_name
      
    if type(password) != str:
      raise TypeError("Password must be a string!")
    else:
      self.password = password
      
    if type(email) != str:
      raise TypeError("Email must be a string!")
    else:
      self.email = email
      
    if type(month) != int:
      raise TypeError("Birth month has to be an integer")
    elif type(year) != int:
      raise TypeError("Birth year has to be an integer")
    elif year < 2005:
      raise ValueError("You have to be born after 2005")
    elif year <= 0 or month <= 0:
      raise ValueError("Year cannot be a negative integer")
    elif month > 12:
      raise ValueError("Month does not exist")
    elif year > 1900:
      raise ValueError("Year does not exist")
    else:
      self.month = month
      self.year = year
      
  def add_account(self):
    self.users = {self.user_name:[self.password, self.email, self.month, self.year]}
    return self.user_name + "'s account has been created."

  def delete_account(self, username, password):
    for users in self.users:
      if self.users[username] == password:
        self.users.pop(username)
        return username + "'s account has been deleted."
      return "User does not exist"
