# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# We add the below configuration to our Flask app using key-value pairs so that Flask app can recognize where our database is stored.
# Enter the following steps sequentially in terminal after writing the code to create database models
# >>> python
# >>> from market import db
# >>> db.create_all()
# >>> from market import Item
# >>> item1 = Item(name="Iphone10",price=500,barcode="846154104831",description="The iPhone X, released in November 2017, marks a significant shift in Apple's smartphone design. With its 5.8-inch Super Retina OLED display, it delivers stunning visuals 
# and vibrant colors. The device features an edge-to-edge display, eliminating the home button and introducing Face ID for secure facial recognition unlocking. Powered by the A11 Bionic chip, the iPhone X offers impressive performance and efficiency. The dual 12MP rear cameras support portrait mode and advanced image processing, while the 7MP front camera enables high-quality selfies and FaceTime. The glass back allows for wireless charging, and the device is water and dust resistant with an IP67 rating. Running iOS 11 out of the box, it provides a seamless user experience with access to a wide range of apps and features. The iPhone X combines cutting-edge technology with sleek design, making it a flagship device that set the standard for future smartphones. Available in Silver and Space Gray, it comes in 64GB and 256GB storage options.")
# >>> db.session.add(item1)
# >>> db.session.commit()
# >>> for item in Item.query.filter_by(price=1350):
# ...     item.name
# ...     item.barcode
# ...     item.price
# We will now see a market.db file in our folder structure
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# db = SQLAlchemy(app)


# Python classes that we make/use will get converted to database tables and these classes are called models. So, in all we are using flask_sqlalchemy ORM(Object Relational Model)
# Type below two statements in cmd in same directory as this file to set environment variables
# set FLASK_APP=market.py
# set FLASK_ENV=development
# set FLASK_DEBUG=1 => to activate debugger
# To return more complicated and good looking web pages, we make a folder "templates" and keep our html files inside it and we can return them from our routes. Name the folder "templates" only and nothing else
# Jinja is special web templating syntax that we can access via html. It is specially designed for Python web frameworks


# Part 1
# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1>"

# # For social media companies like Linkedin and Facebook, they cannot hardcode every route for a different user. So, we use dynamic routing which accepts variables in the url
# @app.route('/about/<username>')
# def about(username):
#     return f"<h1>This is about user {username}!!!</h1>"


# Part 2
# @app.route("/")
# @app.route("/home")
# def home_page():
#     return render_template("home.html")


# @app.route("/market")
# def market_page():
#     # items = [
#     #     {"id": 1, "name": "Phone", "barcode": "893212299897", "price": 500},
#     #     {"id": 2, "name": "Laptop", "barcode": "123985473165", "price": 900},
#     #     {"id": 3, "name": "Keyboard", "barcode": "231985128446", "price": 150},
#     # ]
#     items = Item.query.all()
#     return render_template("market.html", items=items)

# WE NOW PERFORM PROJECT RESTRUCTURING. This leads to Circular Imports. To avoid this, Python uses "PACKAGES". We'll now move on towards creating a package and a python file that knows which import to make first and execute all the imports step by step

# Hence, this market.py file is not longer useful for us. WE MAKE A NEW DIRECTORY "MARKET" WHICH WILL BE OUR PACKAGE