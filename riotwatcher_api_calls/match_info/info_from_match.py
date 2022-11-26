

""" 
Get info from match 
"""

import pandas as pd
from datetime import datetime
import time

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import URL

engine = create_engine("mssql+pyodbc://DESKTOP-CBU1M8B/DataScience?driver=ODBC+Driver+17+for+SQL+Server")

# engine.execute("""
#     DROP TABLE IF EXISTS [DataScience].[dbo].[tbl_summoner_matches]
#     CREATE TABLE [DataScience].[dbo].[tbl_summoner_matches] (
#         [integration_datetime]          DATETIME,
#         [summoner_puuid]                VARCHAR(MAX),
#         [summoner_name]                 VARCHAR(MAX),
#         [summoner_region]               VARCHAR(MAX),
#         [match_id]                      VARCHAR(MAX),
#         [match_start_date]              DATE,
#         [match_start_time]              TIME(0),
#         [match_end_date]                DATE,
#         [match_end_time]                TIME(0),
#         [match_duration]                INT,
#         [match_game_mode]               VARCHAR(MAX),
#         [match_game_type]               VARCHAR(MAX),
#         [match_game_version]            VARCHAR(MAX),
#     )
# """)

def push_sql_tbl_summoner_matches(
    watcher, 
    var_summoner_puuid, 
    var_summoner_name, 
    var_summoner_region, 
    var_match_id, 
    engine, 
    integration_datetime):

        """ instantiate match info """
        match_info = {
            "integration_datetime": [],
            "summoner_puuid": [],
            "summoner_name": [],
            "summoner_region": [],
            "match_id": [],
            "match_start_date": [],
            "match_start_time": [],
            "match_end_date": [],
            "match_end_time": [],
            "match_duration": [],
            "match_game_mode": [],
            "match_game_type": [],
            "match_game_version": [],
        }

        match_info['integration_datetime'].append(integration_datetime)
        match_info['summoner_puuid'].append(var_summoner_puuid)
        match_info['summoner_name'].append(var_summoner_name)
        match_info['summoner_region'].append(var_summoner_region)
        match_info['match_id'].append(var_match_id)
        
        watcher_match = watcher.match.by_id(region=var_summoner_region, match_id=var_match_id)

        """ match_start / timestamp """
        match_start_date = datetime.fromtimestamp(watcher_match['info']['gameStartTimestamp']/1000).strftime('%Y-%m-%d')
        match_start_time = datetime.fromtimestamp(watcher_match['info']['gameStartTimestamp']/1000).strftime('%H:%M')

        match_info['match_start_date'].append(match_start_date)
        match_info['match_start_time'].append(match_start_time)

        """ match_end / timestamp """
        match_end_date = datetime.fromtimestamp(watcher_match['info']['gameEndTimestamp']/1000).strftime('%Y-%m-%d')
        match_end_time = datetime.fromtimestamp(watcher_match['info']['gameEndTimestamp']/1000).strftime('%H:%M')

        match_info['match_end_date'].append(match_end_date)
        match_info['match_end_time'].append(match_end_time)

        """ match_duration / in seconds """
        match_duration = watcher_match['info']['gameDuration']

        match_info['match_duration'].append(match_duration)

        """ game_mode """
        match_game_mode = watcher_match['info']['gameMode'].lower()

        match_info['match_game_mode'].append(match_game_mode)

        """ game_type """
        match_game_type = watcher_match['info']['gameType'].lower()

        match_info['match_game_type'].append(match_game_type)

        """ game_mode """
        match_game_version = watcher_match['info']['gameVersion']

        match_info['match_game_version'].append(match_game_version)
        
        dt = pd.DataFrame(match_info)

        """ push dt to SQL tbl_summoner_matches """
        df_tmp = pd.read_sql_query("""
        SELECT * 
        FROM tbl_summoner_matches 
        WHERE 
            match_id = '%s'
            AND summoner_puuid = '%s'
        """ %(var_match_id, var_summoner_puuid), con=engine)
        
        if df_tmp.empty:
            dt.to_sql('tbl_summoner_matches', con=engine, if_exists='append', index=False)
        else:
            pass

        time.sleep(1)
