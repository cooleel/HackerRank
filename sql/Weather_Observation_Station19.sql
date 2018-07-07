/*
Consider  and  to be two points on a 2D plane where  are the respective minimum and 
maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum 
values of Western Longitude (LONG_W) in STATION.
Query the Euclidean Distance between points  and  and format your answer to display  decimal digits.


@Shanshan Wang
@https://www.hackerrank.com/cooleel
*/


SELECT round(sqrt(power(min(LAT_N)-max(LAT_N),2)+power(min(LONG_W)-max(LONG_W),2)),4)
FROM STATION;