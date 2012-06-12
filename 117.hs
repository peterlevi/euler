#!/usr/bin/runhaskell

cache = map f [0..]
f 0 = 1
f n = sum [cache !! (n - i) | i <- [1..4], n >= i]

main = print $ f 50

