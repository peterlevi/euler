import Data.Ratio

main = print $ length $ filter ok $ init $ map (1+) (scanr (\x a -> 1/(x + a)) 0 (take 1000 $ repeat 2)) 
    where ok r = (length $ show $ numerator r) > (length $ show $ denominator r)

