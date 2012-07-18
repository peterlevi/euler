import Data.List
import Data.Char

main = print $ 
    (!!29) $ sort [x^y | x <- [1..300], y <- [1..100], x^y >= 10, x == (sum $ map digitToInt $ show (x^y))]
