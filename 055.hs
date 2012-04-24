module Main where

pal n = (show n) == (reverse $ show n)
next n = n + (read $ reverse $ show n)
l x i = i < 50 && ((pal x) || l (next x) (i+1))
lychrel x = not $ l (next x) 0
main = print $ length  [x | x <- [0..9999], lychrel x]

