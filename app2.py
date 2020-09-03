#python 3.7.9

from pymongo import MongoClient
from flask import Flask,jsonify,jsonify,request
from flask_pymongo import PyMongo
from pprint import pprint
from data import online_users
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
# app.config["MONGO_URI"] = "mongodb://testadmin:testadmin@localhost:27017/Test"
# mongo = PyMongo(app)
def abort_if_user_doesnt_exist(user_id):
    if user_id not in online_users:
        abort(404, message="user {} doesn't exist".format(user_id))


class Users(Resource):
 

    def get(self):
         return jsonify(online_users)

class User(Resource):
 
    def get(self,name):
        output = []
        for s in online_users:
            if s['First Name']==name:
                output.append(s)
            return jsonify({'users' : output})



api.add_resource(Users, '/users')
api.add_resource(User, '/user/<name>')
 

if __name__ == '__main__':
    app.run(debug=True)