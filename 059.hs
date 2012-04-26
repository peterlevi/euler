module Main where

import Data.Char
import Text.Regex
import Data.Bits
import Data.List

applyKey key [] = []
applyKey (k:key) (c:str) =  ((k `xor` c) : (applyKey (key ++ [k]) str))

genKey 0 = [[]]
genKey n = [(c:key) | c <- [(ord 'a')..(ord 'z')], key <- genKey (n-1)]

ok key text = ("darkness" `isInfixOf` s) where s = map chr $ applyKey key text

main = do x <- readFile "059_cipher1.txt" 
          print $ head $ [(sum sol, map chr key, map chr sol) | let text = map (read :: String -> Int) $ splitRegex (mkRegex ",") x, key <- genKey 3, let sol = applyKey key text, ok key text] 

