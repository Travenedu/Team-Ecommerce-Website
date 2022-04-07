from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from company_information import item_dict, product_types
import bcrypt
import secrets
import os

app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'database'

app.config[
    'MONGO_URI'] = "mongodb+srv://Abbymercy:Abbymerci2!@cluster0.a5hk8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo = PyMongo(app)

app.secret_key = secrets.token_urlsafe(16)

@app.route('/')
@app.route('/index')
def index():
    users = mongo.db.users
    user = users.find_one({"email": "Abby@a.com"})
    product_collection = mongo.db.Head2Toe
    products = product_collection.find({})
    return render_template('index.html', products=products)

@app.route('/seed')
def seed():
    product_collection = mongo.db.Head2Toe
    product_collection.insert_many(item_dict)
    return "OK"

@app.route('/item/<item_id>')
def product(item_id):
    product_collection = mongo.db.Head2Toe
    product = product_collection.find_one({"_id": ObjectId(item_id)})
    return render_template('product.html', product=product)

@app.route('/AbotUs')
def aboutUs():
    return render_template('AboutUs.html')

@app.route('/session/<item_id>')
def addto_cart(user_id):
    user = mongo.db.user
    product_collection = mongo.db.Head2Toe
    
@app.route('/cart')
def cart():
    product_collection = mongo.db.customers
    products = product_collection.find({})
    sum = 0
    for items in products:
        sum += items["item"]["price"]
    product_collection = mongo.db.customers
    products = product_collection.find({})
    return render_template('shopping_cart.html', products=products, price=sum)

@app.route('/save-cart/<itemID>')
def save_cart(itemID):
    users = mongo.db.users
    user = users.find_one({"email": "Abby@a.com"})
    collection = mongo.db.Head2Toe
    item = collection.find_one({"_id": ObjectId(itemID)})
    product_collection = mongo.db.customers
    products = product_collection.insert_one({"item": item, "user": user})
    return render_template('addcart.html')

@app.route('/delete-cart/<itemID>/delete')
def delete_cart(itemID):
    collection = mongo.db.customers
    collection_p = mongo.db.Head2Toe
    item = collection_p.find_one({"_id": ObjectId(itemID)})
    item = collection.find_one({"item": item})
    item = collection.find_one({"name":itemID})
    collection.delete_one(item)
    return redirect('/cart')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template('Signup.html')
  else:
    users = mongo.db.users
    existing_user = users.find_one({'name': request.form['username']})
    if not existing_user:
      firstname = request.form['first_name']
      lastname = request.form['last_name']
      emailaddress = request.form['email']
      birth_month = request.form['month']
      birth_year = request.form['year']
      username = request.form['user_name']
      passworD = request.form['password']
      
      salt = bcrypt.gensalt()
      hashed = bcrypt.hashpw(passworD, salt)
      
      users.insert_one({'firstname': firstname, 'lastname': lastname, 'email': emailaddress, 'username': username, 'password': hashed, 'birthmonth': birth_month, 'birthyear': birth_year})
      session['username'] = request.form['user_name']
      return redirect('/Homepage')
    else:
      return 'Seems like you already have an account with us. Try logging in!'

@app.route('/login', methods = ['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('Login.html')
  else:
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['user_name']})
    if not login_user:
      return 'Invalid username and password combination.'
    else:
      db_password = login_user['password']
      password = request.form['password'].encode("utf-8") 
      if bcrypt.checkpw(password, db_password):
          session['user_name'] = request.form['user_name']
          return redirect('/Homepage')
      else:
          return 'Invalid username and password combination.'

@app.route('/logout')
def logout(userID):
  session.clear()
  return redirect('/')

@app.route('/inventory_view')
def inventory_view():
  collection = mongo.db.Head2Toe
  products = collection.find({})
  return render_template('inventory_all_items.html', products=products, Type_of_Product=product_types, label="All")

#This route is to look at the item individually 
@app.route('/item/<itemID>')
def item(itemID):
  collection = mongo.db.Head2Toe
  item = collection.find_one({"_id": ObjectId(itemID)})
  return render_template('Inventory_item.html', item=item)

# This route is to add an item to inventory
@app.route('/new', methods=['GET', 'POST'])
def new_inventory_item():
  if request.method == 'GET':
      return render_template('new_item.html', TypeofProduct=product_types)

  else:
      name = request.form['name'] 
      price = request.form['price'] 
      stock = request.form['stock'] 
      TypeofProduct = request.form['TypeofProduct']
      collection = mongo.db.Head2Toe
      collection.insert_one({"name":name, "price":price, "stock":stock, "TypeofProduct":TypeofProduct})
      return redirect('/inventory_view')

# This route is to view the products in inventory
@app.route('/inventory_view')
def inventory_view():
    collection = mongo.db.Head2Toe
    products = collection.find({})
    return render_template('inventory_all_items.html', products=products, Type_of_Product=product_types, label="All")

@app.route('/product_type_view/<product_type>')
def product_type_view(product_type):
    collection = mongo.db.Head2Toe
    products = collection.find({"Type of Product":product_type})
    product_type = product_type.capitalize()
    return render_template('inventory_all_items.html', products=products, Type_of_Product=product_type, label=product_type)


@app.route('/item/delete/<itemID>')
def delete(itemID):
    collection = mongo.db.Head2Toe
    item = collection.find_one({"name":itemID})
    collection.delete_one(item)
    return redirect('/inventory_view')


