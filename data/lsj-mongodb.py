import pymongo
import json


# Import le LSJ en base Mongodb

MONGO_DETAILS = 'mongodb+srv://jsrey:4QInstruction@test1.d66q5.mongodb.net/test1?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGO_DETAILS)
database = client.LSJ
lsj_coll = database.get_collection('Words')

#Open Json file
lsj=open('lsj.json')

#return json object as a dictionary
lsj=json.load(lsj)

for i in lsj:
    x = lsj_coll.insert_one(lsj[i])
    print(x)


lsj.close()






