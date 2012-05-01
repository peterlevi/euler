main = print $ maximum [((fromIntegral n) / (fromIntegral d), n, d, n `div` (gcd n d), d `div` (gcd n d)) | d <- [2..10^6], let n = 3*d `div` 7, n*7 < d*3]
