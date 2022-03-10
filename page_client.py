from inventory import Inventory
from cart import Cart
from account import Account
from company_information import item_dict, employee_id

class Client:
    def __init__(self):
        print("Please log in")

    def login(self):
        login = input("Are you an employee or customer?")
        if login == "employee":
            employ_first_name = input("What's your first name?")
            employ_last_name = input("What's your last name?")
            employ_id = input("What's your employee id?")

            if employ_id not in employee_id:
                print("You do not have access")

            else:
                self.employ = Inventory(employ_first_name, employ_last_name, employ_id)

                employee_prompt = input("Would you like to make changes to inventory? (yes or no)")
                if employee_prompt == "yes":
                    print("You can:")
                    print("A: Add an item to inventory")
                    print("B: Remove an item from inventory")
                    print("C: Add items to items stock")
                    print("D: Remove items from items stock")
                    print("E: Check if an item is in stock")
                    print("F: Get a head count of all the items")
                    print("G: Fully restock the items")
                    employee_answer = input("What would you like to do?")

                    if employee_answer == "A":
                        add_item = input("What item are you adding?")
                        add_quantity = input("How much is being added?")
                        self.employ.add_item(add_item, add_quantity)

                    elif employee_answer == "B":
                        remove_item = input("What item are you removing?")
                        self.employ.remove_item(remove_item)
                        
                    elif employee_answer == "C":
                        add_item = input("What item's stock is being add too?")
                        add_quantity = input("How much is being added?")
                        self.employ.add_item_stock(add_item, add_quantity)

                    elif employee_answer == "D":
                        remove_item = input("What item's stock is being removed from?")
                        remove_quantity = input("How much is being removed?")
                        self.employ.remove_item_stock(remove_item, remove_quantity)

                    elif employee_answer == "E":
                        item_check = ("What item are is being checking for?")
                        self.employ.check_item_stock(item_check)

                    elif employee_answer == "F":
                        print("The head count:")
                        self.employ.head_count()

                    elif employee_answer == "G":
                        self.employ.full_restock()     

        elif login == "customer":
            buying = True
            self.cart = Cart("User_name", "User_name")

            print("This is what we have in stock")
            for item, price in item_dict.items():
                print(item + " : " + price)
            while buying == True:
                print("What would you like to buy?")
                item_choice = input("Item:")
                item_quantity = input("Qauntity:")
                self.cart.add_to_cart(item_choice, item_quantity)
                still_shopping = input("Would you like to buy anything else? (yes or no)")
                if still_shopping == "no":
                    buying = False

            print("This is your cart")
            for item_in_cart, quantity in self.cart.user_cart.items():
                print(item_in_cart + " | " + quantity + " | " + item_dict[item_in_cart])

            costumer_answer = input("Would you like to remove anything? (yes or no)")
            if costumer_answer == "yes":
                removing = True

                while removing:

                    remove_item = input("What would you like to remove")
                    remove_quantity = input("How much are you removing?")
                    self.cart.remove_from_cart(remove_item, remove_quantity)

                    still_removing = input("Would you like to remove anything else? (yes or no)")
                    if still_removing == "no":
                        removing = False

            else:
                print("Your total is:")
                self.cart.total_price()
                buying = input("Would you like to purchase? (yes or no)")
                if buying == "yes":
                    print("Your purchase has been made thank you for shopping at Head to Toe")
                else:
                    print("We understand! Please come back again to see us!")
        else:
            print("Not a valid input")

        
        
        #print("Please login")
        #user_question = input("Do you have an account? yes or no")
        #if user_question == "no":
            #print("you will have to make one")
        '''
        user_name = input("User Name?")
        user_password = input("Password?")
        user_email_address = input("Email Address?")
        user_birth_month= input("Birth Month?")
        user_birth_year = input("Year?")
        
        self.user = Account(user_name, user_password, user_email_address, user_birth_month, user_birth_year)
        '''
