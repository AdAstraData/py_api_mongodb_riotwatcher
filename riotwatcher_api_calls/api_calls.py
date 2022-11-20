""" Import Python packages """
from dotenv import dotenv_values
config = dotenv_values(".env")

import pandas as pd
import json

""" Import Python libraries """
from riotwatcher import LolWatcher, ApiError
# https://riot-watcher.readthedocs.io/en/latest/riotwatcher/LeagueOfLegends/index.html

""" Initialize LolWatcher client """
watcher = LolWatcher(config['riotwatcher_api_key'])

""" game versions """
versions = watcher.data_dragon.versions_for_region("euw1")
# print(versions)

""" summoner/ player ids """

# try:
#     response = watcher.summoner.by_puuid(
#             region="euw1", 
#             encrypted_puuid="bZZNu22YOLpn8iDq1FCmW2u4fjW6hNGed3YKTh9LvQeNI65gSjd9EghgBq4HXyj9EKhH-bozh8EvjQ"
#         )
#     print(response)
# except ApiError as err:
#     if err.response.status_code == 429:
#         print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
#         print('this retry-after is handled by default by the RiotWatcher library')
#         print('future requests wait until the retry-after time passes')
#     elif err.response.status_code == 404:
#         print('404 Error: endpoint not found.')
#     else:
#         raise

""" matches ids """
# response = watcher.match.matchlist_by_puuid(
#     region="euw1", 
#     puuid="bZZNu22YOLpn8iDq1FCmW2u4fjW6hNGed3YKTh9LvQeNI65gSjd9EghgBq4HXyj9EKhH-bozh8EvjQ",
#     count=100,
# )
# list_played_matches = response
# print(list_played_matches)

# for match_id in list_played_matches:
for match_id in ['EUW1_6158830217']:
    timeline_dict = watcher.match.timeline_by_match(
        region="euw1",
        match_id=match_id 
    )

    match_id = timeline_dict['metadata']['matchId'] ### matchId = regionId_gameId
    # game_id = timeline_dict['info']['gameId'] 
    # data_version = timeline_dict['metadata']['dataVersion'] 
    participants_puuids = timeline_dict['metadata']['participants'] ### list of puuids
    # participants_ids = timeline_dict['info']['participants'] ### dict of puuids

    print(pd.json_normalize(
        data=timeline_dict['info'],
        record_path="frames",
        sep="_"
    ))
    # print(pd.DataFrame.from_dict(timeline_dict['info']['frames'][0]['participantFrames']['1']))