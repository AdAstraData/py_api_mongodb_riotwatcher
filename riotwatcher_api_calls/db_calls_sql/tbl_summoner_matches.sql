
--DELETE [DataScience].[dbo].tbl_summoner_matches

SELECT * FROM [DataScience].[dbo].tbl_summoner_matches
ORDER BY match_start_date desc, match_start_time desc

/*
SELECT * FROM [DataScience].[dbo].tbl_summoner_matches
WHERE summoner_name = 'AdAstraData'
ORDER BY integration_datetime desc

SELECT * FROM [DataScience].[dbo].tbl_summoner_matches
WHERE summoner_name = 'Storm and Sin'
ORDER BY integration_datetime desc

SELECT * FROM [DataScience].[dbo].tbl_summoner_matches
WHERE summoner_name NOT IN ('Storm and Sin', 'AdAstraData')
ORDER BY integration_datetime desc

SELECT *
FROM [DataScience].[dbo].tbl_summoner_matches
WHERE match_id = 'EUW1_6122482710'
*/
