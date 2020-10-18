-- You are given a table, Functions, containing two columns: X and Y.

-- columns     Type
-- X           Integer
-- Y           Integer

-- Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

-- Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.

-- Sample Input

-- X    Y
-- 20   20
-- 20   20
-- 20   21
-- 23   22
-- 22   23
-- 21   20

-- Sample Output

-- 20 20
-- 20 21
-- 22 23

-- This problem is solved in MySQL.

Select distinct a.x as w,a.y from functions a ,functions b 
Where a.x =b.y and b.x = a.y and a.x < b.x Union all Select a1.x as w,a1.y from functions a1 where a1.x = a1.y group by a1.x,a1.y having count(*)>1 Order by w;