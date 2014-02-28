import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school

score = db.scores

query = {"type":"exam","student_id": {'$gt' : 10,'$lt': 70}}

selection = {"student_id":1}


cursor = score.find(query,selection).limit(100)

for i in cursor:
	print i
