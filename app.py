import os
import bcrypt
import re
import math
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo, DESCENDING
from bson.objectid import ObjectId
from forms import LoginForm, AddUser, AddRecipe, EditRecipe

app = Flask(__name__)

#MongoDB Atlas config linked to Enviroment Variables in Heroku Settings
app.config["MONGO_DBNAME"] = 'cimilestone3'
#app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")
#secret key config linked to Enviroment Variable in Heroku Settings
#app.config["SECRET_KEY"]= os.environ.get("SECRET_KEY")
app.config["SECRET_KEY"] = 'codeinstitute' 
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:KGvZjQwMBmy3N05k@myfirstcluster-zp3d6.mongodb.net/cimilestone3?retryWrites=true&w=majority')


#Initilize Pymongo
mongo = PyMongo(app)

#Main Route
@app.route('/')
@app.route('/index')
def index():
    return render_template("landing.html", title='Lets get Cookin', recipes=mongo.db.recipe.find().limit(5).sort("votes",-1), recipesuser=mongo.db.recipe.find() )

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
    #check if user exists in the database
    if form.validate_on_submit():
        user = mongo.db.user
        dose_user_exist = user.find_one({'username':request.form['username']})
    #if user dose not exist create user
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
    return redirect(url_for('index', title="Logged Out"))

#Recipe Routes

#Get Recipe Route 
@app.route('/get_recipe')
def get_recipe():
   
    #pagination
    #set page limit
    page_limit = 5
    #create dic with request.args
    page = int(request.args.get('page',1))
    #count total recipes in db
    #https://api.mongodb.com/python/current/tutorial.html
    numrecipes = mongo.db.recipe.count_documents({})
    #sorts database returns by top voted   
    reciperet = mongo.db.recipe.find().sort('votes', pymongo.DESCENDING).skip((page -1)*page_limit).limit(page_limit)
    #used to return the sequence of pages in the range
    totalpages = range(1, int(math.ceil(numrecipes / page_limit))+ 1)
    return render_template("recp_view.html", recipes=reciperet, totalpages=totalpages, page=page, title="Recipes")

#Search Recipes
@app.route('/search_recp', methods=['GET', 'POST'])
def search_recp():
    
    page_limit = 5
    page = int(request.args.get('page',1))
    numrecipes = mongo.db.recipe.count_documents({})
   
    #Help from Mentor with following code using regular expressions
    search_query=request.args['query']  
    
    query = {'$regex': re.compile('.*{}.*'.format(search_query)), '$options': 'i'}
    #will return query a result based on top votes
    result = mongo.db.recipe.find({
        '$or':[
            {'title': query},
            {'ingredient': query},
            {'tag': query},
            {'dish_type': query},
        ]
    }).sort('votes', pymongo.DESCENDING).skip((page -1)*page_limit).limit(page_limit)
    
    totalpages = range(1, int(math.ceil(numrecipes / page_limit))+ 1)

    return render_template('search_recp.html', title="Search Results", results=result, totalpages=totalpages, page=page)

#Add Recipe Route
@app.route('/add_recipe', methods=['POST', 'GET'])
def add_recipe():

  form = AddRecipe(request.form)
  if form.validate_on_submit():
        recipedb = mongo.db.recipe
        recipedb.insert_one({'title':request.form['title'],'author':session['username'], 'tags': request.form['tags'], 'image': request.form['image'], 'discription': request.form['discription'],'ingredient':request.form['ingredient'],'instructions':request.form['instructions'],'votes':0,'visits':0})
        flash('Your Recipe has been added', 'alert-success')
        return redirect(url_for('index', title='Recipe Added'))
  return render_template("add_recipe.html", title='Add a New Recipe', form=form)

#Edit Recipe Route
@app.route('/edit_recipe/<recipe_id>', methods=['POST', 'GET'])
def edit_recipe(recipe_id):
    if request.method == 'POST':
        recipedb = mongo.db.recipe
        recipedb.update({"_id": ObjectId(recipe_id)},{'title':request.form['title'],'author':session['username'], 'tags': request.form['tags'], 'image': request.form['image'], 'discription': request.form['discription'],'ingredient':request.form['ingredient'],'instructions':request.form['instructions'],'votes':0,'visits':0})
        flash('Your Recipe has been updated', 'alert-success')
        return redirect(url_for('index', title='Recipe Updated'))
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    form = EditRecipe(data=recipe)
    return render_template("edit_recipe.html", title='Edit a Recipe', form=form)


#Show Recipe Route
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('show_recipe.html', recipe=recipe)

#Delete Recipe Route
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = mongo.db.recipe.remove({"_id": ObjectId(recipe_id)})
    flash('Your Recipe has been deleted', 'alert-success')
    return redirect(url_for('index', title='Recipe Deleted'))
    return render_template('landing.html', recipe=recipe)

#Add Vote to Recipe
@app.route('/vote/<recipe_id>')
def vote(recipe_id):
    recipe = mongo.db.recipe
    recipe.find_one_and_update({'_id' : ObjectId(recipe_id)},
    {'$inc': {'votes': 1}})
    return redirect(url_for('index', title=""))


#Get Shop Route
@app.route('/get_shop')
def get_shop():
    return render_template("shop.html", title='CookIT Shop')

#remove debug flag for deployment
if __name__ == '__main__':
    app.run(debug=True)

   #app.run(host=os.environ.get('IP'),
   #      port=int(os.environ.get('PORT')),
   #      debug=True)

    