from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from company_information import item_dict 
# import secrets
import os

app = Flask(__name__)

# app.config['MONGO_DBNAME'] = 'database'

app.config['MONGO_URI'] = "mongodb+srv://Abbymercy:"+os.environ.get('ABBY_PWD')+"@cluster0.a5hk8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo = PyMongo(app)

app.secret_key = secrets.token_urlsafe(16)

@app.route('/homepage', methods = ['GET', 'POST'])
def homepage():
  pass

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
  if request.method() == "GET":
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

#Route Section
@app.route('/')
@app.route('/index')
def index():
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
    print("Hello SDS")
    print(item_id)
    product_collection = mongo.db.Head2Toe
    product = product_collection.find_one({"_id":ObjectId(item_id)})
    print(product)
    return render_template('product.html', product=product)


@app.route('/session/<item_id>')
def addto_cart(user_id):
     user = mongo.db.user

     product_collection = mongo.db.Head2Toe