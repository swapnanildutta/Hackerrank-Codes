-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
-- For example, if there are three records in the table with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. The query returns 1, because

select count(city)-count(distinct city) from station;