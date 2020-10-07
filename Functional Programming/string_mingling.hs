ming :: String -> String -> String
ming [] [] = []
ming (x:xs) (y:ys) = x : y : ming xs ys


main = interact $ (\(x:y:_) -> ming x y) . lines