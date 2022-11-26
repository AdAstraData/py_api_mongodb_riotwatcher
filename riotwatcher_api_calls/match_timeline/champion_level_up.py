
""" 
Champion Level Up
"""

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import URL

engine = create_engine("mssql+pyodbc://DESKTOP-CBU1M8B/DataScience?driver=ODBC+Driver+17+for+SQL+Server")

# engine.execute("""
#     DROP TABLE IF EXISTS [DataScience].[dbo].[tbl_champion_events_level_up]
#     CREATE TABLE [DataScience].[dbo].[tbl_events_champion_level_up] (
#         [integration_datetime]          DATETIME,
#         [match_id]                      VARCHAR(MAX),
#         [puuid_id]                      VARCHAR(MAX),
#         [event_id]                      VARCHAR(MAX),
#         [event_timestamp]               INT,
#         [level_up_to]                   INT,
#     )
# """)

def push_sql_tbl_events_champion_level_up(match_id, events_champion_level_up, dict_puuid, engine, integration_datetime):

    dt = events_champion_level_up

    dt.dropna(axis=1, inplace=True)

    dt['match_id'] = match_id
    dt['puuid_id'] = dt['participantId'].map(dict_puuid)
    dt['event_id'] = dt['type'].str.lower()
    dt['event_timestamp'] = dt['timestamp']
    dt['level_up_to'] = dt['level'].astype(int)
    dt['integration_datetime'] = integration_datetime

    dt = dt[['integration_datetime', 'match_id', 'puuid_id', 'event_id', 'event_timestamp', 'level_up_to']]

    df_tmp = pd.read_sql_query("SELECT * from tbl_events_champion_level_up WHERE match_id = '%s'" %(match_id), con=engine)
    
    if df_tmp.empty:
        dt.to_sql('tbl_events_champion_level_up', con=engine, if_exists='append', index=False)
    else:
        pass

