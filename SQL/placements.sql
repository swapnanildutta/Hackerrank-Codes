-- You are given three tables: Students, Friends and Packages. Students contains two columns: ID and Name.
-- Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend).
-- Packages contains two columns: ID and Salary (offered salary in $ thousands per month).

-- Write a query to output the names of those students whose best friends got offered a higher salary than them.
-- Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.

SELECT S.Name FROM Friends F JOIN Students S USING (ID) JOIN Packages P1 ON S.ID=P1.ID JOIN Packages P2 ON F.Friend_ID=P2.ID AND P1.Salary<P2.Salary 
ORDER BY P2.Salary