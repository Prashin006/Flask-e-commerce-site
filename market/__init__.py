from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '3616be61fb6431a19e371c9c'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"     # This tells our login_manager that our login page is located at login_page route
login_manager.login_message_category = "info"

# Decorators are like functions that execute before the functions itself
# If we import a file, Python tries to execute the file
from market import routes

# A package in Python is a way of organizing related modules into a single directory hierarchy. The presence of __init__.py in a directory indicates that the directory is a package.
# Now as we have a __init__.py file inside of our Market directory, outside of Market directory, every python file recognizes it as a "Package"
# __init__.py can be an empty file or contain initialization code for the package. It can initialize package-level variables or import submodules to simplify package imports.
# It helps organize your code into modules and sub-packages, making it easier to manage and maintain large codebases.
# By structuring your code into packages, you can avoid naming conflicts and improve code readability.