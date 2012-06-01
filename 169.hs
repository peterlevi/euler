#!/usr/bin/runhaskell

-- Slow! Needs memoization

f 0 _ = 1
f 1 True = 1
f 1 False = 0
f n False 
    | odd n = 0 
    | otherwise = f (n `div` 2) True
f n True
    | even n = (f (n - 2) False) + (f n False)
    | otherwise = f (n - 1) False

main = print $ f (10^25) True
