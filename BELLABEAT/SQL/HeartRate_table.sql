SELECT HR.Id,CAST(Time AS datetime) AS Date_Time,Value,SUM(CAST(Calories AS float)) AS Total_Calories
FROM Project.dbo.heartrate_seconds_merged AS HR
INNER JOIN Project.dbo.minuteCaloriesNarrow_merged AS MC ON MC.Id=HR.Id AND CAST(MC.ActivityMinute AS datetime)=HR.Time
GROUP BY HR.id,Time,Value
ORDER BY Time,HR.Id