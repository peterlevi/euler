main = print $ sum $ map r [3..1000] where
    r a = if (even a) then a^2 - 2*a else a^2 - a

