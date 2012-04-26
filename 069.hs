import Primes

main = print $ product $ take x primes
    where x = last $ takeWhile (\n -> (product $ take n primes) < 10^6) [1..]

