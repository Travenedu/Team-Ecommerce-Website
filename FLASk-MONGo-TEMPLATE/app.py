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



# edit 



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




