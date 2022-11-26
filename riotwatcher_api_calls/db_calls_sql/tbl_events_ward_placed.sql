
--DELETE [DataScience].[dbo].[tbl_events_ward_placed]

SELECT COUNT(DISTINCT match_id) FROM [DataScience].[dbo].tbl_events_ward_placed

SELECT * FROM [DataScience].[dbo].tbl_events_ward_placed

/*
DECLARE @summoner_name AS VARCHAR(MAX) = 'AdAstraData'
SELECT @summoner_name

DROP TABLE IF EXISTS #events_ward_placed

SELECT 
	ward_placed.*
	,summoner_matches.match_start_date
	,summoner_matches.summoner_name

INTO #events_ward_placed
FROM [DataScience].[dbo].tbl_events_ward_placed ward_placed
LEFT JOIN (
	SELECT DISTINCT
		match_id
		,match_start_date
		,summoner_puuid
		,summoner_name

	FROM [DataScience].[dbo].tbl_summoner_matches summoner_matches
	) summoner_matches
ON summoner_matches.match_id = ward_placed.match_id AND summoner_matches.summoner_puuid = ward_placed.puuid_id
WHERE summoner_name IS NOT NULL

SELECT DISTINCT ward_type
FROM #events_ward_placed

SELECT 
	match_id
	,match_start_date
	,summoner_name
	,ward_placed_num = COUNT(*)

FROM #events_ward_placed
WHERE summoner_name = @summoner_name
GROUP BY match_id, match_start_date, summoner_name
ORDER BY match_start_date asc
*/
