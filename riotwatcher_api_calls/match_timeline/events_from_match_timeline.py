

""" 
Get events from match timeline 
"""

import pandas as pd
from datetime import datetime

def get_events_from_match_timeline(watcher_match_timeline):

    """ vision events """
    events_ward_placed = pd.DataFrame()
    events_ward_kill = pd.DataFrame()

    """ champion events """
    events_champion_level_up = pd.DataFrame()
    events_skill_level_up = pd.DataFrame()

    """ item events """
    events_item_purchases = pd.DataFrame()
    events_item_undo = pd.DataFrame()
    events_item_destroyed = pd.DataFrame()
    events_item_sold = pd.DataFrame()

    """ kill events """
    events_champion_kill = pd.DataFrame()
    events_champion_special_kill = pd.DataFrame()
    events_elite_monster_kill = pd.DataFrame()

    """ turret events """
    events_turret_plate_destroyed = pd.DataFrame()
    events_building_kill = pd.DataFrame()

    for frame_num in range(len(watcher_match_timeline['info']['frames'])):

        if frame_num == 0:
            df_frame = pd.json_normalize(watcher_match_timeline['info']['frames'][frame_num]['events'])
            timeline_start_date = datetime.fromtimestamp(int(df_frame['realTimestamp']) / 1000).strftime('%Y-%m-%d')
            timeline_start_time = datetime.fromtimestamp(int(df_frame['realTimestamp']) / 1000).strftime('%H:%M')

        else:
            df_frame = pd.json_normalize(watcher_match_timeline['info']['frames'][frame_num]['events'])

            """ vision events """
            df_ward_placed = df_frame.query("type == 'WARD_PLACED'").dropna(axis=1)
            events_ward_placed = pd.concat([events_ward_placed, df_ward_placed], ignore_index=True)

            df_ward_kill = df_frame.query("type == 'WARD_KILL'").dropna(axis=1)
            events_ward_kill = pd.concat([events_ward_kill, df_ward_kill], ignore_index=True)

            """ champion events """
            df_champion_level_up = df_frame.query("type == 'LEVEL_UP'").dropna(axis=1)
            events_champion_level_up = pd.concat([events_champion_level_up, df_champion_level_up], ignore_index=True)

            df_skill_level_up = df_frame.query("type == 'SKILL_LEVEL_UP'").dropna(axis=1)
            events_skill_level_up = pd.concat([events_skill_level_up, df_skill_level_up], ignore_index=True)

            """ item events """
            df_item_purchases = df_frame.query("type == 'ITEM_PURCHASED'").dropna(axis=1)
            events_item_purchases = pd.concat([events_item_purchases, df_item_purchases], ignore_index=True)

            df_item_undo = df_frame.query("type == 'ITEM_UNDO'").dropna(axis=1)
            events_item_undo = pd.concat([events_item_undo, df_item_undo], ignore_index=True)

            df_item_destroyed = df_frame.query("type == 'ITEM_DESTROYED'").dropna(axis=1)
            events_item_destroyed = pd.concat([events_item_destroyed, df_item_destroyed], ignore_index=True)

            df_item_sold = df_frame.query("type == 'ITEM_SOLD'").dropna(axis=1)
            events_item_sold = pd.concat([events_item_sold, df_item_sold], ignore_index=True)

            """ kill events """
            df_champion_kill = df_frame.query("type == 'CHAMPION_KILL'").dropna(axis=1)
            events_champion_kill = pd.concat([events_champion_kill, df_champion_kill], ignore_index=True)

            df_champion_special_kill = df_frame.query("type == 'CHAMPION_SPECIAL_KILL'").dropna(axis=1)
            events_champion_special_kill = pd.concat([events_champion_special_kill, df_champion_special_kill], ignore_index=True)

            df_elite_monster_kill = df_frame.query("type == 'ELITE_MONSTER_KILL'").dropna(axis=1)
            events_elite_monster_kill = pd.concat([events_elite_monster_kill, df_elite_monster_kill], ignore_index=True)

            """ turret events """
            df_turret_plate_destroyed = df_frame.query("type == 'TURRET_PLATE_DESTROYED'").dropna(axis=1)
            events_turret_plate_destroyed = pd.concat([events_turret_plate_destroyed, df_turret_plate_destroyed], ignore_index=True)

            df_building_kill = df_frame.query("type == 'BUILDING_KILL'").dropna(axis=1)
            events_building_kill = pd.concat([events_building_kill, df_building_kill], ignore_index=True)

    return (
        events_ward_placed,
        events_ward_kill,
        events_champion_level_up,
        events_skill_level_up,
        events_item_purchases,
        events_item_undo,
        events_item_destroyed,
        events_item_sold,
        events_champion_kill,
        events_champion_special_kill,
        events_elite_monster_kill,
        events_turret_plate_destroyed,
        events_building_kill,
    )
    
