
# coding: utf-8

# In[15]:


from pymongo import MongoClient
from time import sleep
import requests

client = MongoClient('10.142.0.3', 27017)

db = client.ticker
collection = db.binance

while True:

    r = requests.get("https://api.binance.com/api/v3/ticker/bookTicker")

    posts = r.json()
    result1 = collection.insert_many(posts)
    
    sleep(1)



