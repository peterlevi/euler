module Main where

import Data.List
import Primes 

perm x y = (sort $ show x) == (sort $ show y)

phi n x y = n - (n `div` x) - (n `div` y) + 1

main = print $ minimum $ [((fromIntegral n) / (fromIntegral $ phi n x y), n, x, y, phi n x y) | x <- takeWhile (<5*10^6) primes, y <- takeWhile (\p -> p <= x && x*p < 10^7) primes, let n = x*y, perm n (phi n x y)]

