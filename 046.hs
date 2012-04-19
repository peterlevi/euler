module Main where

primes = [x | x <- [2..], isPrime x]

isPrime :: Integer -> Bool
isPrime x = null $ filter (\y ->  x `mod` y == 0) $ takeWhile (\y ->  y*y <= x) [2..]

bad :: Integer -> Bool
bad x = (not $ isPrime x) && null [p | p <- takeWhile (<x) primes, is2sq (x - p)]

isInt :: Double -> Bool
isInt x = x == fromInteger (round x)

is2sq :: Integer -> Bool
is2sq x = isInt $ sqrt $ (fromIntegral x) / 2

main = print $ head $ filter bad [3,5..]

