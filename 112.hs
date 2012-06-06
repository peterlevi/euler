#!/usr/bin/runhaskell

import Data.List

solve n acc = if acc * 100 == n * 99 then n else solve (n + 1) (if bouncy (n + 1) then (acc + 1) else acc)
    where bouncy x = let s = (sort . show) x in show x /= s && show x /= (reverse s)

main = print $ solve 1 0
