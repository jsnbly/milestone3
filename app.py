import os
import bcrypt
import re
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm, AddUser, AddRecipe

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
    return render_template("landing.html", title='Lets get Cookin', recipes=mongo.db.recipe.find().limit(3) )

#User Routes

#Get User Route ADMIN Testing
@app.route('/get_user')
def get_user():
    return render_template("user.html", users=mongo.db.user.find())

#Login user
@app.route('/login', methods=['GET', 'POST'])
def login():
#check to see if user in session
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index', title="Logged In"))
#get user to login and check password in database against password used to login
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.user
        user_login = user.find_one({'username' : request.form['username']})
        if user_login:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), user_login['password']) == user_login['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('index', title="Logged In", form='form'))
            flash('Invalid Username or Password', 'alert-danger')    
    return render_template("login.html", title="Log In", form=form)

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
            flash('Your Account has been created, You can now login', 'alert-success')
            return redirect(url_for('login'))
        flash('That username already exists, Please try again', 'alert-danger')
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

#Search Recipes
@app.route('/search_recp', methods=['GET', 'POST'])
def search_recp():

    query=request.form

    results = mongo.db.cimilestone3.find({
        '$text':[
            {'title': query},
            {'ingredients': query},
            {'allergen': query},
            {'dish_type': query},
        ]
    })
    return render_template('search_recp.html', results=result,)

#Add Recipe Route
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():

  form = AddRecipe(request.form)
  if form.validate_on_submit():
        recipedb = mongo.db.recipe
        recipedb.insert_one({'title':request.form['title'],'author':session['username'],'dish_type': request.form['dish_type'],'discription': request.form['discription'],'ingredient':request.form['ingredient'],'instruction':request.form['instruction'],'votes':0,'visits':0})
        flash('Your Recipe has been added', 'alert-success')
        return redirect(url_for('add_recipe', title='Recipe Added'))
  return render_template("add_recipe.html", title='Add a New Recipe', form=form)

#Edit Recipe Route
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', editrecp=recipe )


#Get Shop Route
@app.route('/get_shop')
def get_shop():
    return render_template("shop.html", title='Shop')

#remove debug flag for deployment
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)

    