import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import LoginForm

app = Flask(__name__)

#MongoDB Atlas config linked to Enviroment Variables in Heroku Settings
app.config["MONGO_DBNAME"] = 'cimilestone3'
app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")
#secret key config linked to Enviroment Variable in Heroku Settings
app.config["SECRET_KEY"]= os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

#Main Route
@app.route('/')
def index():
    return render_template("base.html")

#User Route code

#Get User Route
@app.route('/get_user')
def get_user():
    return render_template("user.html", users=mongo.db.user.find())

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

#Get Recipe Route
@app.route('/get_recipe')
def get_recipe():
    return render_template("recp_view.html", recipes=mongo.db.recipe.find())

#Get Shop Route
@app.route('/get_shop')
def get_shop():
    return render_template("shop.html")

#Remove Debug flag for deployment
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)