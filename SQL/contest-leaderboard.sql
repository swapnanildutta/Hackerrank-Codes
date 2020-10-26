-- The total score of a hacker is the sum of their maximum scores for all of the challenges.
-- Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score.
-- If more than one hacker achieved the same total score, then sort the result by ascending hacker_id.
-- Exclude all hackers with a total score of 0 from your result.

-- Input Format
-- Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker. 
-- Submissions: The submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, 
-- challenge_id is the id of the challenge for which the submission belongs to, and score is the score of the submission.

SELECT h.hacker_id, h.name, SUM(m.score) FROM (SELECT hacker_id, MAX(score) AS score FROM Submissions 
	GROUP BY challenge_id, hacker_id) AS m, Hackers h WHERE h.hacker_id=m.hacker_id GROUP BY h.hacker_id, h.name HAVING SUM(m.score)>0 
    ORDER BY SUM(m.score) DESC, h.hacker_id