# Write your MySQL query statement below

SELECT Weather.id as "Id" FROM Weather JOIN Weather x ON DATEDIFF(weather.recordDate, x.recordDate)=1 AND Weather.temperature>x.temperature