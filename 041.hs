module Main where

import Data.List

isPrime :: Integer -> Bool
isPrime x = null $ filter (\y ->  x `mod` y == 0) $ takeWhile (\y ->  y*y <= x) [2..]

perms :: Eq a => [a] -> [[a]]
perms [] = [[]]
perms xs = [x:ys | x <- xs, ys <- perms(xs \\ [x])]

main :: IO()
main = print $ head $ concat $ [(filter isPrime $ map (read :: String -> Integer) $ perms $ reverse ['1'..x]) | x <- ['7', '6'..'1']]

