from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['libary']
books = db['books']

# books.insert_many([
#     {"title":"book1","author":"author1","year":2020,"publisher":"publisher1","price":100},
#     {"title":"book2","author":"author2","year":2021,"publisher":"publisher2","price":200},
#     {"title":"book3","author":"author3","year":2022,"publisher":"publisher3","price":300},
#     {"title":"book4","author":"author4","year":2023,"publisher":"publisher4","price":400},
#     {"title":"book5","author":"author5","year":2024,"publisher":"publisher5","price":500},
# ])

print("-----------------------------")
print("all books")
for book in books.find():
    print(book)
    
print("-----------------------------")
print("books published in 2021")
for book in books.find({"year":2021}):
    print(book)
    
print("-----------------------------")
print("books published in 2024 and publisher5")
for book in books.find({"year":2024,"publisher":"publisher5"}):
    print(book)
    
print("-----------------------------")
print("updating book1 price to 150")
books.update_one({"title":"book1"},{"$set":{'price': 150}})
print("updated price for book1")
for book in books.find({"title":"book1"}):
    print(book)
    
print("-----------------------------")
print("books price in desecnding orrder")
for book in books.find().sort("price",-1):
    print(book)
    
print("-----------------------------")
# books.update_one({"title":"book4"},{"$mul":{'price':10}})
# print("updated price for book4")
# for book in books.find({"title":"book4"}):
#     print(book)
    
print("-----------------------------")
print("books price between 300 and 500")
for book in books.find({"price":{"$gte":300,"$lte":500}}):
    print(book)

print("Total books:", books.count_documents({}))
