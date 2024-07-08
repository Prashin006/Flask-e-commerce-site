from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.models import User


# As we are working with forms where we render an html page and client submits his/her information, this requires some security. So we need to set a security key for working with forms in Flask
# We generate a secret key using the os library
class RegisterForm(FlaskForm):
    # As we are inheriting from FlaskForm class, if any function startwith "validate_", FlaskForm first checks for such functions and then moves on to the next word (username, email_address in our case) and checks whether a field of this name even exists. If the field exists then it executes/calls the function for validating the field.
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("User Name already exists! Please try a different User Name!")

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email address already exists! Please try a different email address!")

    username = StringField(
        label="User Name:", validators=[Length(min=6, max=30), DataRequired()]
    )
    email_address = StringField(
        label="Email Address:", validators=[Email(), DataRequired()]
    )
    password1 = PasswordField(
        label="Password:", validators=[Length(min=6, max=60), DataRequired()]
    )
    password2 = PasswordField(
        label="Confirm Password:", validators=[EqualTo("password1"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell')