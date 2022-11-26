
""" 
Champion Kill
"""

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import URL

engine = create_engine("mssql+pyodbc://DESKTOP-CBU1M8B/DataScience?driver=ODBC+Driver+17+for+SQL+Server")

# engine.execute("""
#     DROP TABLE IF EXISTS [DataScience].[dbo].[tbl_events_champion_kill]
#     CREATE TABLE [DataScience].[dbo].[tbl_events_champion_kill] (
#         [integration_datetime]          DATETIME,
#         [match_id]                      VARCHAR(MAX),
#         [event_id]                      VARCHAR(MAX),
#         [event_timestamp]               INT,
#         [map_coord_x]                   VARCHAR(MAX),
#         [map_coord_y]                   VARCHAR(MAX),
#         [puuid_killer_id]               VARCHAR(MAX),
#         [kill_streak_len]               INT,
#         [puuid_victim_id]               VARCHAR(MAX),
#         [kill_value]                    INT,
#         [bounty_value]                  INT,
#     )
# """)

def push_sql_tbl_events_champion_kill(match_id, events_champion_kill, dict_puuid, engine, integration_datetime):
    
    dt = events_champion_kill

    dt.dropna(axis=1, inplace=True)

    dt['match_id'] = match_id
    dt['event_id'] = dt['type'].str.lower()
    dt['event_timestamp'] = dt['timestamp']
    dt['map_coord_x'] = dt['position.x']
    dt['map_coord_y'] = dt['position.y']
    dt['puuid_killer_id'] = dt['killerId'].map(dict_puuid)
    dt['kill_streak_len'] = dt['killStreakLength'].astype(int)
    dt['puuid_victim_id'] = dt['victimId'].map(dict_puuid)
    dt['kill_value'] = dt['bounty'].astype(int)
    dt['bounty_value'] = dt['shutdownBounty'].astype(int)
    dt['integration_datetime'] = integration_datetime

    dt = dt[[
        'integration_datetime', 'match_id', 'event_id', 'event_timestamp',
        'map_coord_x', 'map_coord_y', 'puuid_killer_id', 'kill_streak_len', 'puuid_victim_id', 
        'kill_value', 'bounty_value'
    ]]
    
    df_tmp = pd.read_sql_query("SELECT * from tbl_events_champion_kill WHERE match_id = '%s'" %(match_id), con=engine)
    
    if df_tmp.empty:
        dt.to_sql('tbl_events_champion_kill', con=engine, if_exists='append', index=False)
    else:
        pass
