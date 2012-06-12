#!/usr/bin/runhaskell

fibs2 = 1 : 1 : zipWith (+) fibs2 (drop 1 fibs2)
fibs3 = 1 : 1 : 1 : zipWith (+) fibs3 (drop 2 fibs3)
fibs4 = 1 : 1 : 1 : 1 : zipWith (+) fibs4 (drop 3 fibs4)

main = print $ fibs2 !! 50 + fibs3 !! 50 + fibs4 !! 50 - 3

