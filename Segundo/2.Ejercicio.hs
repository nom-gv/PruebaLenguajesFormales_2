calculadora :: String -> Int -> Int -> Int
calculadora x
    | x == "+" = \a b -> a + b
    | x == "-" = \a b -> a - b
    | x == "*" = \a b -> a * b
    | x == "/" = \a b -> a `div` b

main :: IO ()
main = do 
    a <- getLine
    b <- getLine
    putStrLn $ "Suma: " ++ (show (calculadora "+" (read a) (read b)))
    putStrLn $ "Resta: " ++ (show (calculadora "-" (read a) (read b)))
    putStrLn $ "Multiplicacion: " ++ (show (calculadora "*" (read a) (read b)))
    putStrLn $ "Division: " ++ (show (calculadora "/" (read a) (read b)))