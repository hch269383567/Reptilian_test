from pymongo import  MongoClient


cient=MongoClient('mongodb://127.0.0.1:1001,127.0.0.1:1002,127.0.0.1:1003')
# cient=MongoClient(['127.0.0.1:1001','127.0.0.1:1002','127.0.0.1:1003'])

db=cient['db1804']
coll=db['test']

r=coll.insert_one({'test_insert':'use_cluster'})

