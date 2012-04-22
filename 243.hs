module Main where

import Data.List 
import Primes

factors' y ps@(p:t) counted acc
  | y == 1 = acc
  | y `mod` p == 0 = factors' (y `div` p) ps True (if counted then acc else p:acc)
  | otherwise = factors' y t False acc

factors1 x = factors' x primes False []

factors x = nub $ unfoldr findFactor x
   where
       findFactor 1 = Nothing
       findFactor x = Just (nextFactor, x `div` nextFactor)
           where nextFactor = head $ filter (\f -> x `mod` f == 0) primes

sublists [] = [[]]
sublists (x:xs) = concat [[(x:s), s] | s <- sublists xs]

r n = n + sum [(-1)^(length s) * (n `div` (product s)) | s <- (sublists $ factors n), not $ null s]

ok n = (r n) * 94744 < (n - 1) * 15499

cap = head $ [x | x <- [1..], ok $ product $ take x primes]
lower = product $ take (cap - 1) primes

solution = head $ [lower * x | x <- [1..], ok (lower * x)]

main = print $ solution

