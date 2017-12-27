
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
import requests

client = MongoClient('10.142.0.3', 27017)

db = client.test_database
collection = db.test_collection

r = requests.get("https://api.binance.com/api/v3/ticker/price")

posts = r.json()
result1 = collection.insert_many(posts)

print("end")

