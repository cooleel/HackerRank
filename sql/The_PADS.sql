/*
P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):
* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).

@Shanshan Wang
@https://www.hackerrank.com/cooleel
*/


SELECT concat(NAME,concat("(",concat(substr(OCCUPATION,1,1),")"))) 
FROM OCCUPATIONS 
ORDER BY NAME ASC;

SELECT "There are a total of ", count(OCCUPATION), concat(lower(occupation),"s.") FROM OCCUPATIONS 
GROUP BY OCCUPATION 
ORDER BY count(OCCUPATION), OCCUPATION ASC;