-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

--Sample Input

--For example, CITY has four entries: DEF, ABC, PQRS and WXY.

--Sample Output

--ABC 3
--PQRS 4
--Explanation

--When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . The longest name is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.

--Note
--You can write two separate queries to get the desired output. It need not be a single query.

select city, length(city)
from
(
  select 
    city, 
    row_number() over (order by length(city), city) as shortest_is_one,
    row_number() over (order by length(city) desc, city) as longest_is_one
  from station
)
where shortest_is_one = 1 or longest_is_one = 1;