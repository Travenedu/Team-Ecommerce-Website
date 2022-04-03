from flask import Flask
from flask import render_template
from flask import request, redirect, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from company_information import item_dict, product_types 
import collections
import secrets
import bcrypt
import os

app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb+srv://Abbymercy:"+os.environ.get('ABBY_PWD')+"@cluster0.a5hk8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo = PyMongo(app)

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

@app.route('/inventory')
def inventory():
    #collection = mongo.db.Head2Toe
    #if session:
    #    pass
        #user = session['username']
        #user_ID = collection.find_one({}) 
        #job_title = collection.find_one({})
        #employee_image = collection.find_one({})
    #else:
    #untill everything is connected
    user = "guest"
    user_ID = 123
    job_title = "Unavailble"
    return render_template('Inventory.html', user = user, user_ID = user_ID, job_title = job_title)

#This route is to look at the item individually 
@app.route('/item/<itemID>')
def item(itemID):
    collection = mongo.db.Head2Toe
    item = collection.find_one({"_id":ObjectId(itemID)})
    return render_template('Inventory_item.html', item=item) 

#This route is to add an item to inventory 
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

#This route is to view the products in inventory
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

@app.route('/item/<itemID>/delete')
def delete(itemID):
    collection = mongo.db.Head2Toe
    item = collection.find_one({"_id":ObjectId(itemID)})
    collection.delete_one(item)
    return redirect('/inventory_view')
