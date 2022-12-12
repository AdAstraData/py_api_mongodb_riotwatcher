import pandas as pd
import numpy as np

from datetime import date, datetime
import time

import requests, urllib, json
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
Use 'match_timeline' collections and add/update/upsert/delete records 
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

match_timeline_euw1 = db['match_timeline_euw1']
match_timeline_eun1 = db['match_timeline_eun1']
match_timeline_br1 = db['match_timeline_br1']
match_timeline_la1 = db['match_timeline_la1']
match_timeline_la2 = db['match_timeline_la2']
match_timeline_na1 = db['match_timeline_na1']
match_timeline_oc1 = db['match_timeline_oc1']
match_timeline_tr1 = db['match_timeline_tr1']
match_timeline_jp1 = db['match_timeline_jp1']
match_timeline_kr = db['match_timeline_kr']

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

list_colls_match_timeline = [
    match_timeline_euw1, match_timeline_eun1, match_timeline_br1, match_timeline_la1, match_timeline_la2,
    match_timeline_na1, match_timeline_oc1, match_timeline_tr1, match_timeline_jp1, match_timeline_kr,
   ]

""""
Fetch list of gameId per server from featured_match and API call GET match_timeline for each (if not already present in match_timeline)
"""

for region_idx in range(len(list_regions)):
      
    print(list_regions[region_idx])

    list_records_gameId = list_colls_featured_match[region_idx].find({}, {'gameId':1, 'platformId':1})

    for record_id in list_records_gameId:
        
        time.sleep(5)
        var_match_id = str(record_id['platformId'])+"_"+str(record_id['gameId'])
        print(var_match_id)

        record_match_timeline = watcher.match.timeline_by_match(region=list_regions[region_idx],match_id=var_match_id)

        list_colls_match_timeline[region_idx].update_one(
            {'matchId' : record_match_timeline['metadata']['matchId']},
            {'$set' : record_match_timeline},
            upsert=True
        )
