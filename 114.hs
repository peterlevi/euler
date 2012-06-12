#!/usr/bin/runhaskell

cnts = map cnt [0..50]

cnt 0 = 1
cnt 1 = 1
cnt 2 = 1
cnt n = cnts !! (n - 1) + sum [cnts !! (n - r - 1) | r <- [3..(n - 1)]] + 1

main = print $ cnt 50

