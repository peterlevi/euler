#!/usr/bin/runhaskell

f n = product [1..n]
c n k = (f n) `div` ((f (n - k)) * (f k))
v n k = c (n + k - 1) k

solve d = (v 10 d) - 1 + sum [v 10 i | i <- [1..d]] - d - 9*d

main = print $ solve 100
