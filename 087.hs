module Main where

import Primes
import Data.Set
import Data.List

main = print $ size $ Data.List.foldl (flip Data.Set.insert) Data.Set.empty 
    [p | x <- sq, y <- th, z <- fo, let p = x + y + z, p < 50000000] 
    where
         sq = takeWhile (<50000000) $ Data.List.map (^2) primes
         th = takeWhile (<50000000) $ Data.List.map (^3) primes
         fo = takeWhile (<50000000) $ Data.List.map (^4) primes

