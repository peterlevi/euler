#!/usr/bin/runhaskell

import Data.List
import Data.Char
import Debug.Trace

test = [
    0,0,3,0,2,0,6,0,0,
    9,0,0,3,0,5,0,0,1,
    0,0,1,8,0,6,4,0,0,
    0,0,8,1,0,2,9,0,0,
    7,0,0,0,0,0,0,0,8,
    0,0,6,7,0,8,2,0,0,
    0,0,2,6,0,9,5,0,0,
    8,0,0,2,0,3,0,0,9,
    0,0,5,0,1,0,3,0,0]

get s i j = s !! (i*9 + j)

row s i = take 9 $ drop (9*i) s
col s j = [get s r j | r <- [0..8]]
square s i j = [get s (m + x) (n + y) | let m = 3*i, let n = 3*j, x <- [0..2], y <- [0..2]]

free s i j = [1..9] \\ ((row s i) ++ (col s j) ++ (square s (i `div` 3) (j `div` 3)))

set i j a s = (take (i*9 + j) s) ++ [a] ++ (drop (i*9 + j + 1) s)

ok s = null $ filter (==0) s

empty s = minimum [(length f, f, i, j) | i <- [0..8], j <- [0..8], get s i j == 0, let f = free s i j]

solve s = trace ("solve: " ++ show s) (solve' s)

solve' s
    | ok s = trace ("solution: " ++ show s) s
    | otherwise = if null solutions then []
                  else head $ solutions
                        where solutions = filter (not . null) [solve' (set i j d s) | let (_, f, i, j) = empty s, d <- f]

val s = foldl (\a l -> a*10 + l) 0 $ take 3 s

go l acc
    | null l = acc
    | otherwise = go (drop 10 l) (acc + (val $ solve $ parseSudoku $ take 9 $ drop 1 l))

parseSudoku = foldl (\a line -> a ++ (map digitToInt $ take 9 line)) [] 

main = do
    x <- readFile "096_sudoku.txt"
    print $ go (lines x) 0

