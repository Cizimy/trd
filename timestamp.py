#!/usr/bin/python
 
# using pymongo-2.2
from bson.objectid import ObjectId
import datetime
 
now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
start_date = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
end_date = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
oid_start = ObjectId.from_datetime(start_date)
oid_stop = ObjectId.from_datetime(end_date)
 
print '{ "_id" : { "$gte" : { "$oid": "%s" }, "$lt" : { "$oid": "%s" } } }' % ( str(oid_start), str(oid_stop) )
