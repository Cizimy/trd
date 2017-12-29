
# coding: utf-8

# In[1]:


import signal
import time

def task(arg1, arg2):
    print(time.time())

signal.signal(signal.SIGALRM, task)

while True:
    time.sleep(1)

