module Main where

import Data.List
import Primes

ps = 0 : (snd $ mapAccumL (\x y -> (x + y, x + y)) 0 $ takeWhile (<10000) primes)

main = print $ head $ head $ [l | n <- [length ps, length ps - 1..], 
    let l = filter (\d -> isPrime d && d < 1000000) $ zipWith (\x y -> y-x) ps (drop n ps), 
    not $ null $ l]

