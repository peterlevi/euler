module Main where

import Char

f (a,b) x = (b `div` g, (x*b + a) `div` g) where g = gcd b (x*b + a)
numer n = (snd $ foldl f (1, head ds) $ drop 1 ds) where ds = reverse (2:(take (n-1) $ drop 1 $ [if x `mod` 3 == 0 then 2*(x `div` 3) else 1 | x <- [1..]]))
main  = print $ sum $ map digitToInt $ show $ numer 100

