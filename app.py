import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cimilestone3'
app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/get_user')
def get_user():
    return render_template("user.html", users=mongo.db.user.find())

@app.route('/get_recipe')
def get_recipe():
    return render_template("recp_view.html", users=mongo.db.recipe.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)