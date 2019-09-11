import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm, AddUser

app = Flask(__name__)

#MongoDB Atlas config linked to Enviroment Variables in Heroku Settings
app.config["MONGO_DBNAME"] = 'cimilestone3'
app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")
#secret key config linked to Enviroment Variable in Heroku Settings
app.config["SECRET_KEY"]= os.environ.get("SECRET_KEY")

#Initilize Pymongo
mongo = PyMongo(app)

#Main Route
@app.route('/')
@app.route('/index')
def index():
    return render_template("landing.html", title='Lets get Cookin')

#User Routes

#Get User Route ADMIN
@app.route('/get_user')
def get_user():
    return render_template("user.html", users=mongo.db.user.find())

#Login user
@app.route('/login', methods=['GET', 'POST'])
def login():
#check to see if user in session
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index', title="Loggedin"))
#get user to login and check password in database against login
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.user
        user_login = user.find_one({'username' : request.form['username']})
        if user_login:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), user_login['password']) == user_login['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('index', title="Sign In", form='form'))
            flash('Invalid Username or Password')    
    return render_template("login.html", title="Loggedin", form=form)

#register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = AddUser(request.form)
    if form.validate_on_submit():
        user = mongo.db.user
        dose_user_exist = user.find_one({'username':request.form['username']})
       
        if dose_user_exist is None:
            cryptpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            user.insert_one({'username':request.form['username'],
                                'password': cryptpass,
                                'email':request.form['email']})
            session['username'] = request.form['username']
            flash('Your Account has been created, You can now login', 'success')
            return redirect(url_for('login'))
        flash('That username already exists, Please try again')
        return redirect(url_for('register'))
    return render_template("register.html", title='Register', form=form)

#Log out by clearing user session
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

#Recipe Routes

#Get Recipe Route ADMIN
@app.route('/get_recipe')
def get_recipe():
    return render_template("recp_view.html", recipes=mongo.db.recipe.find())

#Add Recipe Route
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", title='Add a New Recipe')

#Get Shop Route
@app.route('/get_shop')
def get_shop():
    return render_template("shop.html", title='Shop')

#Remove Debug flag for deployment
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)