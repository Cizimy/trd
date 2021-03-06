
# coding: utf-8

# In[2]:


from pymongo import MongoClient
import signal
import time
import requests

client = MongoClient('10.142.0.3', 27017)

db = client.ticker
collection = db.binance

def task(arg1, arg2):
    r = requests.get("https://api.binance.com/api/v1/time")
    post = r.json()
    result1 = collection.insert_one(post)

signal.signal(signal.SIGALRM, task)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

while True:
    time.sleep(1)

