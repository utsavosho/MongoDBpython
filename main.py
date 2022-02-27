#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:01:53 2022

@author: utsav
"""
import pymongo as pymongo
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId

# connection to the db

client = pymongo.MongoClient("mongodb+srv://j1503c:jatin15031996@cluster0.ralqq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
server_api=ServerApi('1'))
db = client.test

countries = db.countries
continents = db.continents



# 1. Get all the Country where a letter or word given is in the name, for example: FR Fran..


def FindCountryByQuery(name):
    for i in countries.find({'name': {"$regex": name, "$options": 'i'}}):
        print(i['name'])

#FindCountryByQuery('ra')






# 3. Send the list of continent with there number of countries

def GetContriesandContinents():
    query = [
        {
            '$project': {
                'name': "$name",
                'countries': {'$size': "$countries"}}
        }
    ]
    continent = continents.aggregate(query)
    for i in continent:
        print(i)
        
#GetContriesandContinents()

# 4. Send back the fourth countries of a continent by alphabetic order

def FourthCountry():
     for i in continents.find():
         for j in i['countries']:
             res = countries.find({'_id': ObjectId(j)}).sort("name")
             print(i['name'],':',res[0]['name'])

#FourthCountry()




# 6. Get all the countries order by number of people first the less populated and last the most populated
def OrderByPopulation():
    for i in countries.find({}).sort("population"):
        print("The country name is", i['name'], i['population'])

#OrderByPopulation()

# 7. Get countries which have a u in their name and more 100000 people inside

def SearchByu():
    for i in countries.find(
            {
                'name':
                    {'$regex': 'u', '$options': 'i'}, 'population': {'$gt': 100000}
            }
            ).sort("population"):
        print("The country name is", i['name'], i['population'])


#SearchByu()





# Get Countries 

def FindCountry():
    for i in countries.find():
        print(i['name'])
        
FindCountry()
        
# Find Conuntries By id         

def FindContrybyId(country_id):
    for i in countries.find({'_id': ObjectId(country_id)}):
        print(i['name'])
        
#FindContrybyId('')
