#!/usr/bin/runhaskell

f m n = cnts !! n where
    cnts = map cnt [0..]
    cnt i
        | i < m = 1
        | otherwise = cnts !! (i - 1) + sum [cnts !! (i - r - 1) | r <- [m..(i - 1)]] + 1

main = print $ head $ [(n, ff) | n <- [1..], let ff = f 50 n, ff > 10^6]

