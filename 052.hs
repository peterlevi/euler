module Main where
import Data.List
main = print $ head $ [x | x <-[100000..], (length $ nub [sort $ show (k*x) | k <-[1..6]]) == 1]
