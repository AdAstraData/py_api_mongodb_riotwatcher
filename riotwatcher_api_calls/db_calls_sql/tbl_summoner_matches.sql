
--DELETE [DataScience].[dbo].tbl_summoner_matches

SELECT * FROM [DataScience].[dbo].tbl_summoner_matches
ORDER BY match_start_date desc, match_start_time desc

/*
SELECT *
FROM [DataScience].[dbo].tbl_summoner_matches
WHERE match_id = 'EUW1_6166598877'
*/

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
*/

/*
SELECT
	match_id
	,min_since_match_end = DATEDIFF(MINUTE, CAST(CONCAT(match_end_date,' ',match_end_time) AS DATETIME), integration_datetime)

FROM [DataScience].[dbo].tbl_summoner_matches
ORDER BY min_since_match_end asc
*/

/*
;WITH tmp_tbl_a AS (
	SELECT
		today_date = GETDATE()
		,summoner_name
		,num = COUNT(*)
	FROM [DataScience].[dbo].[tbl_summoner_matches]
	GROUP BY summoner_name
	),

tmp_tbl_b AS (
	SELECT
		summoner_name
		,num
		,total_num = SUM(num) OVER (PARTITION BY today_date)

	FROM tmp_tbl_a
	)

SELECT
	*
	,perc = CAST(ROUND(100.0 * num/total_num, 2) AS FLOAT(2))

FROM tmp_tbl_b
ORDER BY perc desc
*/
