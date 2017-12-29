
# coding: utf-8

# In[2]:


import signal
import time
import requests

def task(arg1, arg2):
    r = requests.get("https://api.binance.com/api/v3/ticker/bookTicker?symbol=BNBBTC")
    data = r.json()
    print(data)

signal.signal(signal.SIGALRM, task)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
    time.sleep(1)

