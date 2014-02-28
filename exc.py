import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.akshat

user = db.user

data = {'fname':'akshat','lname':'sharma'}

print data

try:
	user.insert(data)
except:
	print "Error ", sys.exc_info()[0]


