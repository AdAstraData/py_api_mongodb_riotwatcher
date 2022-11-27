

""" 
Get events from match timeline 
"""

import pandas as pd
from datetime import datetime

# def get_specific_type_event(df_frame, specific_type_event, df_specific_type_event, events_specific_type_event):

#     df_specific_type_event = df_frame.copy()
#     df_specific_type_event = df_specific_type_event.query("type == '@specific_type_event'")
#     if df_specific_type_event.empty:
#         pass
#     else:
#         df_specific_type_event.dropna(axis=1, how='all', inplace=True)
#         events_pause_end = pd.concat([events_pause_end, df_specific_type_event], ignore_index=True)
        

def get_events_from_match_timeline(watcher_match_timeline):

    # """ timeline events """
    # events_all = pd.DataFrame()
    # events_pause_end = pd.DataFrame()

    # """ vision events """
    # events_ward_placed = pd.DataFrame()
    # events_ward_kill = pd.DataFrame()

    # """ champion events """
    # events_champion_level_up = pd.DataFrame()
    # events_skill_level_up = pd.DataFrame()

    # """ item events """
    # events_item_purchased = pd.DataFrame()
    # events_item_undo = pd.DataFrame()
    # events_item_destroyed = pd.DataFrame()
    # events_item_sold = pd.DataFrame()

    """ kill events """
    events_champion_kill = pd.DataFrame()
    # events_champion_special_kill = pd.DataFrame()
    # events_elite_monster_kill = pd.DataFrame()

    # """ turret events """
    # events_turret_plate_destroyed = pd.DataFrame()
    # events_building_kill = pd.DataFrame()

    for frame_num in range(len(watcher_match_timeline['info']['frames'])):

        df_frame = pd.json_normalize(watcher_match_timeline['info']['frames'][frame_num]['events'])
        
        if df_frame.empty:
            pass
        else:

            # """ timeline events - pause end """
            # df_all = df_frame.copy()
            # if df_all.empty:
            #     pass
            # else:
            #     df_all_slim = df_all.dropna(axis=1, how='all')
            #     events_all = pd.concat([events_all, df_all_slim], ignore_index=True)
            
            # """ timeline events - pause end """
            # df_pause_end = df_frame.copy()
            # df_pause_end = df_pause_end.query("type == 'PAUSE_END'")
            # if df_pause_end.empty:
            #     pass
            # else:
            #     df_pause_end_slim = df_pause_end.dropna(axis=1, how='all')
            #     events_pause_end = pd.concat([events_pause_end, df_pause_end_slim], ignore_index=True)
            
            # """ vision events - ward placed """
            # df_ward_placed = df_frame.copy()
            # df_ward_placed = df_ward_placed.query("type == 'WARD_PLACED'")
            # if df_ward_placed.empty:
            #     pass
            # else:
            #     df_ward_placed_slim = df_ward_placed.dropna(axis=1, how='all')
            #     events_ward_placed = pd.concat([events_ward_placed, df_ward_placed_slim], ignore_index=True)

            # """ vision events - ward kill """
            # df_ward_kill = df_frame.copy()
            # df_ward_kill = df_ward_kill.query("type == 'WARD_KILL'")
            # if df_ward_kill.empty:
            #     pass
            # else:
            #     df_ward_kill_slim = df_ward_kill.dropna(axis=1, how='all')
            #     events_ward_kill = pd.concat([events_ward_kill, df_ward_kill_slim], ignore_index=True)

            # """ champion events - champion level up """
            # df_champion_level_up = df_frame.copy()
            # df_champion_level_up = df_champion_level_up.query("type == 'LEVEL_UP'")
            # if df_champion_level_up.empty:
            #     pass
            # else:
            #     df_champion_level_up_slim = df_champion_level_up.dropna(axis=1, how='all')
            #     events_champion_level_up = pd.concat([events_champion_level_up, df_champion_level_up_slim], ignore_index=True)

            # """ champion events - skill level up """
            # df_skill_level_up = df_frame.copy()
            # df_skill_level_up = df_skill_level_up.query("type == 'SKILL_LEVEL_UP'")
            # if df_skill_level_up.empty:
            #     pass
            # else:
            #     df_skill_level_up_slim = df_skill_level_up.dropna(axis=1, how='all')
            #     events_skill_level_up = pd.concat([events_skill_level_up, df_skill_level_up_slim], ignore_index=True)

            # """ item events - item purchased """
            # df_item_purchased = df_frame.copy()
            # df_item_purchased = df_item_purchased.query("type == 'ITEM_PURCHASED'")
            # if df_item_purchased.empty:
            #     pass
            # else:
            #     df_item_purchased_slim = df_item_purchased.dropna(axis=1, how='all')
            #     events_item_purchased = pd.concat([events_item_purchased, df_item_purchased_slim], ignore_index=True)

            # """ item events - item undo """
            # df_item_undo = df_frame.copy()
            # df_item_undo = df_item_undo.query("type == 'ITEM_UNDO'")
            # if df_item_undo.empty:
            #     pass
            # else:
            #     df_item_undo_slim = df_item_undo.dropna(axis=1, how='all')
            #     events_item_undo = pd.concat([events_item_undo, df_item_undo_slim], ignore_index=True)

            # """ item events - item destroyed """
            # df_item_destroyed = df_frame.copy()
            # df_item_destroyed = df_item_destroyed.query("type == 'ITEM_DESTROYED'")
            # if df_item_destroyed.empty:
            #     pass
            # else:
            #     df_item_destroyed_slim = df_item_destroyed.dropna(axis=1, how='all')
            #     events_item_destroyed = pd.concat([events_item_destroyed, df_item_destroyed_slim], ignore_index=True)

            # """ item events - item sold """
            # df_item_sold = df_frame.copy()
            # df_item_sold = df_item_sold.query("type == 'ITEM_SOLD'")
            # if df_item_sold.empty:
            #     pass
            # else:
            #     df_item_sold_slim = df_item_sold.dropna(axis=1, how='all')
            #     events_item_sold = pd.concat([events_item_sold, df_item_sold_slim], ignore_index=True)

            """ kill events - champion kill """
            df_champion_kill = df_frame.copy()
            df_champion_kill = df_champion_kill.query("type == 'CHAMPION_KILL'")
            if df_champion_kill.empty:
                pass
            else:
                df_champion_kill_slim = df_champion_kill.dropna(axis=1, how='all')
                events_champion_kill = pd.concat([events_champion_kill, df_champion_kill_slim], ignore_index=True)

            # """ kill events - champion special kill """
            # df_champion_special_kill = df_frame.copy()
            # df_champion_special_kill = df_champion_special_kill.query("type == 'CHAMPION_SPECIAL_KILL'")
            # if df_champion_special_kill.empty:
            #     pass
            # else:
            #     df_champion_special_kill_slim = df_champion_special_kill.dropna(axis=1, how='all')
            #     events_champion_special_kill = pd.concat([events_champion_special_kill, df_champion_special_kill_slim], ignore_index=True)

            # """ kill events - elite monster kill """
            # df_elite_monster_kill = df_frame.copy()
            # df_elite_monster_kill = df_elite_monster_kill.query("type == 'ELITE_MONSTER_KILL'")
            # if df_elite_monster_kill.empty:
            #     pass
            # else:
            #     df_elite_monster_kill_slim = df_elite_monster_kill.dropna(axis=1, how='all')
            #     events_elite_monster_kill = pd.concat([events_elite_monster_kill, df_elite_monster_kill_slim], ignore_index=True)

            # """ building events - turret plate destroyed """
            # df_turret_plate_destroyed = df_frame.copy()
            # df_turret_plate_destroyed = df_turret_plate_destroyed.query("type == 'TURRET_PLATE_DESTROYED'")
            # if df_turret_plate_destroyed.empty:
            #     pass
            # else:
            #     df_turret_plate_destroyed_slim = df_turret_plate_destroyed.dropna(axis=1, how='all')
            #     events_turret_plate_destroyed = pd.concat([events_turret_plate_destroyed, df_turret_plate_destroyed_slim], ignore_index=True)

            # """ building events - turret plate destroyed """
            # df_building_kill = df_frame.copy()
            # df_building_kill = df_building_kill.query("type == 'BUILDING_KILL'")
            # if df_building_kill.empty:
            #     pass
            # else:
            #     df_building_kill_slim = df_building_kill.dropna(axis=1, how='all')
            #     events_building_kill = pd.concat([events_building_kill, df_building_kill_slim], ignore_index=True)

    return (
        # events_all,
        # events_pause_end,
        # events_ward_placed,
        # events_ward_kill,
        # events_champion_level_up,
        # events_skill_level_up,
        # events_item_purchased,
        # events_item_undo,
        # events_item_destroyed,
        # events_item_sold,
        events_champion_kill,
        # events_champion_special_kill,
        # events_elite_monster_kill,
        # events_turret_plate_destroyed,
        # events_building_kill,
    )
    
