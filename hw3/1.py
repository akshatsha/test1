# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:51:03 2014

@author: user
"""

import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
students = db.students

def find_lowest_entry(scores):
    lowest = None
    lowest_score = 100    
    for data in scores:
        if((data['type']=="homework") and (data["score"] < lowest_score)):
            lowest = data
            lowest_score = data["score"]
            
    return lowest
    

def main():
    user = students.find()
    for i in user:
        scores = i["scores"]        
        lowest = find_lowest_entry(scores)
        if(scores is not None):            
            print"lowest score found for user ",i['name'] , " is " , lowest["score"]
            scores.remove(lowest)
            students.update({'_id': i['_id']},{'$set' : {'scores': scores}})

main()