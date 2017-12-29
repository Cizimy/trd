
# coding: utf-8

# In[2]:


import signal
import time
import requests

def task(arg1, arg2):
    r = 8 * 2
    print(r)

signal.signal(signal.SIGALRM, task)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

while True:
    time.sleep(1)

