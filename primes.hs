module Primes(primes, isPrime, factors, phi) where

import Data.List

-- duplicates-removing union of two ordered increasing lists
unite (x:xs) (y:ys) = case (compare x y) of 
           LT -> x : unite  xs  (y:ys)
           EQ -> x : unite  xs     ys 
           GT -> y : unite (x:xs)  ys

primes = 2 : gaps 3 (join [[p*p,p*p+2*p..] | p <- primes'])
  where
    primes' = 3 : gaps 5 (join [[p*p,p*p+2*p..] | p <- primes'])
    join  ((x:xs):t)        = x : unite xs (join (pairs t))
    pairs ((x:xs):ys:t)     = (x : unite xs ys) : pairs t
    gaps k xs@(x:t) | k==x  = gaps (k+2) t 
                    | True  = k : gaps (k+2) xs

isPrime x = x /= 1 && (null $ [p | p <- takeWhile (\p -> p*p <= x) primes, x `mod` p == 0])

factors x = unfoldr findFactor x
   where
       findFactor 1 = Nothing
       findFactor x = Just (nextFactor, x `div` nextFactor)
           where nextFactor = head $ filter (\f -> x `mod` f == 0) primes

phi n = foldl (\a p -> a * (p - 1) `div` p) n (nub $ factors n)

