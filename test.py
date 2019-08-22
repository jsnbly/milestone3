from flask_pymongo import PyMongo

import app as app_module

app=app_module.app

app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo=PyMongo(app)
app_module.mongo = mongo

