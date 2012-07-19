import Primes

main = print $ (+1) $ length $ takeWhile (\(n, p) -> (even n || 2*n*p <= 10^10)) $ zip [1..] Primes.primes

