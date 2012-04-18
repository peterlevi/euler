module Main where

import qualified Data.Set as Set

main = print $ Set.intersection (Set.intersection a b) c
            where a = foldl (flip Set.insert) Set.empty [n*(n+1)/2 | n <- [1..10000]]
                  b = foldl (flip Set.insert) Set.empty [n*(3*n-1)/2 | n <- [1..10000]] 
                  c = foldl (flip Set.insert) Set.empty [n*(2*n-1) | n <- [1..10000]] 
