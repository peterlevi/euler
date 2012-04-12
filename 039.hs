module Main where

import qualified Data.Map as Map
import qualified Data.List as List

main = print $
    List.foldl1 (\(a, b) (c, d) -> if b > d then (a, b) else (c, d)) $ 
    Map.toList $ Map.fromListWith (+) $ 
    List.map (\([a, b, c], 1) -> (a + b + c, 1)) $ List.nub $ 
    [(List.sort [a, b, c], 1) | m <- [1..34], n <- [1..(m - 1)], k <- [1..30], 
        let a = k * (m^2 - n^2), 
        let b = k * 2 * m * n, 
        let c = k * (m^2 + n^2), 
        let p = a + b + c, 
        p > 0, p <= 1000]

