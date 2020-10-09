-- The Fibonacci Series

-- The Fibonacci sequence begins with  and . These are the first and second terms, respectively. After this, every element is the sum of the preceding elements:

-- Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)  
-- Task
-- Given the starter code, complete the Fibonacci function to return the  term.

-- We start counting from Fibonacci. This might differ from some other notations that treats Fibonacci.

-- The overall equation is:

--              = 0 , n = 1
-- Fibonacci(n) = 1 , n = 2
--                Fibonacci(n-1) + Fibonacci(n-2)  , n > 2

-- Input Format --

-- One line of input, the integer .

-- Constraints


-- Output Format --

-- Output one integer, the  Fibonacci number.

-- Sample Input

-- 3  
-- Sample Output

-- 1  

fib :: Int -> Int
fib n
    | n == 1 = 0
    | n == 2 = 1
    | otherwise = fib(n-1) + fib(n-2)


-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main = do
    input <- getLine
    print . fib . (read :: String -> Int) $ input