import pandas as pd
import numpy as np
import json

from datetime import date, datetime
import time

import urllib, json
from dotenv import dotenv_values
config = dotenv_values("./.env")

import pymongo

"""
Connect to MongoDB Atlas DataBase
"""
conn_str = (
   "mongodb+srv://"
   + urllib.parse.quote(config['MONGODB_USER']) 
   + ":"
   + urllib.parse.quote(config['MONGODB_PWD'])
   + "@hugoafsantos-datascienc.yvocwdh.mongodb.net/?retryWrites=true&w=majority"
)

client = pymongo.MongoClient(conn_str)
db = client['riotwatcher_api_fetch_data']

# print(db.command("collstats", "featured_match")["totalSize"]/1048576)
# print(db.command("dbstats")["storageSize"]/1048576)

"""
Retrieve all collections from 'riotwatcher_api_fetch_data' MongoDB instance 
"""
# print(db.list_collection_names())

"""
Use 'featured_match' collections and add/update/upsert/delete records 
"""
featured_match_euw1 = db['featured_match_euw1']
featured_match_eun1 = db['featured_match_eun1']
featured_match_br1 = db['featured_match_br1']
featured_match_la1 = db['featured_match_la1']
featured_match_la2 = db['featured_match_la2']
featured_match_na1 = db['featured_match_na1']
featured_match_oc1 = db['featured_match_oc1']
featured_match_tr1 = db['featured_match_tr1']
featured_match_jp1 = db['featured_match_jp1']
featured_match_kr = db['featured_match_kr']
# featured_match.drop()

# featured_match.delete_many({})

# from bson import ObjectId

# for record_id in featured_match_euw1.find():
#    print(ObjectId(record_id['_id']).generation_time)


""" 
Initialize RiotWatcher API 
"""
from riotwatcher import LolWatcher

watcher = LolWatcher(config['RIOTW_API_KEY'])

list_regions = [
      'euw1','br1','eun1', 'la1', 'la2', 'na1', 'oc1', 'tr1', 'jp1', 'kr'
   ]

list_colls_featured_match = [
      featured_match_euw1, featured_match_eun1, featured_match_br1, featured_match_la1, featured_match_la2,
      featured_match_na1, featured_match_oc1, featured_match_tr1, featured_match_jp1, featured_match_kr,
   ]

""""
While 1 > 0: THEN ...
"""

while 1 > 0:
   time.sleep(30)
   
   for region_idx in range(len(list_regions)):
      
      time.sleep(1)
      print(list_regions[region_idx])
      
      list_records_featured_match = watcher.spectator.featured_games(region=list_regions[region_idx])['gameList']

      for record_idx in range(len(list_records_featured_match)):

         print(list_regions[region_idx]+"_"+str(list_records_featured_match[record_idx]['gameId']))

         list_colls_featured_match[region_idx].update_one(
            {'gameId' : list_records_featured_match[record_idx]['gameId']},
            {'$set' : list_records_featured_match[record_idx]},
            upsert=True
         )