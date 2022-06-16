import pymongo

client=pymongo.MongoClient()

mydb=client["mydb"]

mycol=mydb["Employee"]

# data={'Name':'Prajwal', 'Age':'23'}
# mycol.insert_one(data)
#
# datalist=[{'Name':'ABC','Age':'25'},{'Name':'XYZ','Age':'30'}]
# x=mycol.insert_many(datalist)

for x in mycol.find({'Age':'25'}):
    print(x)