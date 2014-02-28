import pymongo

from pymongo import Connection
connection = Connection('localhost', 27017)

db = connection.akshat

responses = db.user

item = responses.find_one()

print item['id']
