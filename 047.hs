module Main where

import Data.List

factors' y p counted acc
  | y == 1 = acc
  | y `mod` p == 0 = factors' (y `div` p) p True (acc + (if counted then 0 else 1))
  | otherwise = factors' y (p + 1) False acc

factors x = factors' x 2 False 0

cnts = zip [2..] (map factors [2..])

count4s ((a,cnt):rest)
  | cnt /= 4   =  0
  | otherwise  = 1 + count4s rest

solve x
  | count4s x >= 4   = fst $ head x
  | otherwise        = solve $ tail x

main = print $ solve cnts


