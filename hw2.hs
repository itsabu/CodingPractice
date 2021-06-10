fib :: (Integral a) => a -> a
remove :: [b] -> Int -> [b]
lreduce :: (a -> a -> a) -> [a] -> a

fibHelp n a b   | n == 0 = a
            |  n == 1 = b
            | otherwise = fibHelp (n-1) b (a+b)

fib n = fibHelp n 0 1

remove (x:xs) i | i > length(x:xs) = (x:xs)
                | i == 1 = xs
                | otherwise = x:remove xs (i-1)



main = do 
   print(remove [1..10] 3)