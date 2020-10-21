-- Pawel and Shaka recently became friends. They believe their friendship will last forever if they merge their favorite strings.

-- The lengths of their favorite strings are the same, . Mingling two strings,  and , both of length , will result in the creation of a new string  of length . It will have the following structure:

-- You are given two strings  (Pawel's favorite) and  (Shaka's favorite), determine the mingled string .

-- Input Format

-- The first line of input contains the string .
-- The second line contains .

-- Output Format

-- Print the mingled string, .

-- Constraints


-- The string only consists of lowercase English characters ().
-- length(P) = length(Q) 

-- Sample Input #00

-- abcde
-- pqrst
-- Sample Output #00

-- apbqcrdset
-- Sample Input #01

-- hacker
-- ranker
-- Sample Output #01

-- hraacnkkeerr


ming :: String -> String -> String
ming [] [] = []
ming (x:xs) (y:ys) = x : y : ming xs ys


main = interact $ (\(x:y:_) -> ming x y) . lines