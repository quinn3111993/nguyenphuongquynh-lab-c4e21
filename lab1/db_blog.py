# 1. Connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://quinn_311:a123456@ds135852.mlab.com:35852/quinndb"

client = MongoClient(uri)
db = client.get_default_database()

# 2. Select collection
posts = db["posts"]

# 3. Create document
post = {
    "title": "How to think like a computer scientist",
    "content": "Đây là 1 cuốn sách rất dễ hiểu và hữu ích cho những người mới lập trình",
}

# 4. Insert document
# posts.insert_one(post)

# print("Done")

post_list = posts.find()
# for post in post_list:
#     print(post)
cond = {
    "title": {
        '$regex': 'Điểm',
        '$options': 'i'
        }
}
post = posts.find_one(cond)
print(post)