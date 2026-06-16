import pymongo
import json


# Import le LSJ en base Mongodb

MONGO_DETAILS = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(MONGO_DETAILS)
database = client.LSJ
lsj_coll = database.get_collection('Words')
lsj_coll.drop()
#Open Json file
lsj=open('lsj.json')

#return json object as a dictionary
lsj=json.load(lsj)

key = 1
for i in lsj:
    entry = lsj[i]
    entry["sort_key"] = key
    key += 1
    x = lsj_coll.insert_one(entry)
    print(x)








