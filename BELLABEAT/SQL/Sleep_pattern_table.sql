SELECT DISTINCT DA.Id,CAST(ActivityDate AS DATE) AS ActivityDate,TotalSteps,TotalDistance,
SedentaryMinutes,TotalMinutesAsleep,TotalTimeInBed,TotalSleepRecords,

	  CASE
		WHEN (CAST(([TotalMinutesAsleep]) AS INT))<=420 THEN 'Poor Sleep'
		WHEN (CAST(([TotalMinutesAsleep]) AS INT))>420 AND (CAST(([TotalMinutesAsleep]) AS INT))<=540 THEN 'Good Sleep'
		ELSE 'Excess Sleep' 
	  END  AS Sleep_Pattern,
(CAST(TotalTimeInBed AS INT)-CAST(TotalMinutesAsleep AS INT)) AS Idle_minutes_on_bed
FROM Project.dbo.dailyActivity_merged AS DA
INNER JOIN Project.dbo.sleepDay_merged AS SD ON DA.Id=SD.Id AND ActivityDate=SleepDay


