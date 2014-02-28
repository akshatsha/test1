# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:41:04 2014

@author: user
"""

import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students

coll = db.grades
array = []
#Find Lowest Score

def remove_entry(_id):
    try:    
        coll.remove({'_id':_id})
    except:
        print "Exception remove entry", sys.exc_info()[0]
        
def lowest_score():
    try:    
        cursor = coll.find({'type':'homework'}).sort([('student_id',pymongo.DESCENDING),('score',pymongo.DESCENDING)])
    except:
        print "Exception lowest score", sys.exc_info()[0]
    
    for i in cursor:
        if i['student_id'] in array:
            print("removing entry with stu id ", i['student_id'] , " & score is " , i['score'])             
            remove_entry(i["_id"])
        else:
            print("current entry with stu id " , i['student_id'] , " & score is " , i['score'])
            array.append(i['student_id'])
    
lowest_score()