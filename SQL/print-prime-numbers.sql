-- Write a query to print all prime numbers less than or equal to 1000. Print your result on a single line, 
-- and use the ampersand (&) character as your separator (instead of a space).

-- For example, the output for all prime numbers <=10 would be:

-- 2&3&5&7

-- It is solved in Oracle

select listagg (num, '&') within group (order by num) from 
( select n1.num num, sum(case when mod(n1.num,n2.num) = 0 then 1 else 0 end) as cnt from 
(select rownum num from dual connect by level <= 1000) n1, 
(select rownum num from dual connect by level <= 1000) n2 where n1.num<>1 and n2.num<>1 and n1.num>=n2.num group by n1.num) a where cnt = 1;