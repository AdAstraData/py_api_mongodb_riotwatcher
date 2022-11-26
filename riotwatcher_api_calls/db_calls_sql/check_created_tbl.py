
--DELETE FROM [DataScience].[dbo].[tbl_events_champion_level_up]
--DELETE FROM [DataScience].[dbo].[tbl_events_skill_level_up]
--DELETE FROM [DataScience].[dbo].[tbl_events_ward_placed]
--DELETE FROM [DataScience].[dbo].[tbl_events_ward_kill]
--DELETE FROM [DataScience].[dbo].[tbl_events_champion_kill]

SELECT DISTINCT integration_datetime, match_id FROM [DataScience].[dbo].[tbl_events_champion_level_up]
--SELECT TOP 10 * FROM [DataScience].[dbo].[tbl_events_skill_level_up]
--SELECT TOP 10 * FROM [DataScience].[dbo].[tbl_events_ward_placed]
--SELECT TOP 10 * FROM [DataScience].[dbo].[tbl_events_ward_kill]
--SELECT TOP 10 * FROM [DataScience].[dbo].[tbl_events_champion_kill]

SELECT COUNT(*) FROM [DataScience].[dbo].[tbl_events_champion_level_up]


SELECT * FROM [DataScience].[dbo].[tbl_events_champion_level_up]
WHERE puuid_id = 'bZZNu22YOLpn8iDq1FCmW2u4fjW6hNGed3YKTh9LvQeNI65gSjd9EghgBq4HXyj9EKhH-bozh8EvjQ'
ORDER BY level_up_to asc

