import Primes

main = print $ (\y -> (y + 1) `div` 2) $ fst $ head $ dropWhile (\(cnt, pr) -> pr * 10 >= (fromIntegral cnt)) $ drop 2 $ scanl (\(a, b) (c, d) -> (c, b + d)) (0,0) $ map (\x -> (2*x-1, s x)) [1,3..] 
    where s x = length $ filter isPrime [x*x - x + 1, x*x - 2*x + 2, x*x - 3*x + 3]
