#python 3.7.9

from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_pymongo import PyMongo
from pprint import pprint
from data import online_users
import logging



app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://testadmin:testadmin@localhost:27017/Test"
# mongo = PyMongo(app)
app.config["DEBUG"] = True

@app.route("/")
def home_page():     
    return "running..."

@app.route("/users")
def users():
    return jsonify(online_users)


@app.route("/users/name/<string:name>",methods=['GET'])
def user_by_name(name):
    output = []
    for s in online_users:
        if s['First Name']==name:
            output.append(s)
    return jsonify({'users' : output})

@app.route("/user")
def user_by_id():
    output = []
    if 'name' in request.args:
        name = str(request.args['name'])
    else:
        return "Error: param missing."

    for s in online_users:
        if s['First Name']==name:
            output.append(s)
    return jsonify({'users' : output})
 

app.run()