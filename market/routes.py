from market import app, db
from flask import render_template,redirect,url_for,flash,request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market", methods=["GET", "POST"])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    if request.method == "POST":
        # Purchase Item
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You successfully purchased {p_item_object.name}!",category="success")
            else:
                flash(f"Insufficient balance! Cannot purchase {p_item_object.name}!",category="danger")

        # Sell Item
        sold_item = request.form.get("sold_item")
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"You have successfully sold out your {s_item_object.name}!", category='info')
            else:
                flash(f"Something went wrong. Could not sell {s_item_object}!", category='danger')
        return redirect(url_for('market_page'))
    
    if request.method == "GET":
        items = Item.query.all()
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template("market.html", items=items, owned_items=owned_items,purchase_form=purchase_form,sell_form=sell_form)


# For our route to handle post requests, we need to provide it with methods argument as shown
@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    # validate_on_submit function validates and checks the conditional
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            # password_hash=form.password1.data,
            password=form.password1.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f"Account created successfully! You are now logged in as: {user_to_create.username}",
            category="success",
        )
        return redirect(url_for("market_page"))

    # If there are no errors from validations
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"There was an error creating a user: {err_msg}", category="danger")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            # Below function takes the User object as argument and logs in the user
            login_user(attempted_user)
            flash(
                f"Success! You are logged in as: {attempted_user.username}",
                category="success",
            )
            return redirect(url_for("market_page"))
        else:
            flash(
                "Username and Password do not match! Please try again!",
                category="danger",
            )
    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been successfully logged out!", category="info")
    return redirect(url_for("home_page"))
