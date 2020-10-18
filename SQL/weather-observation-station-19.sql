-- Consider P1(a,c) and P2(b,d) to be two points on a 2D plane where (a,b) are the respective minimum and 
-- maximum values of Northern Latitude (LAT_N) and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

-- Query the Euclidean Distance between points P1 and P2 and format your answer to display 4 decimal digits.

-- Input Format

-- The STATION table is described as follows:

-- Field    Type
-- ID       Number(21)
-- CITY     VARCHAR2(21)
-- STATE    VARCHAR2(2)
-- LAT_N    NUMBER
-- LONG_W   NUMBER

-- where LAT_N is the northern latitude and LONG_W is the western longitude.

-- This problem is solved in MySQL.

select round( sqrt( pow(max(lat_n)-min(lat_n),2 )+pow(max(long_w)-min(long_w),2)),4) from station;