suma :: Int -> Int -> Int
suma x y = x + y

resta :: Int -> Int -> Int
resta x y = x - y

multiplicacion :: Int -> Int -> Int
multiplicacion x y = x * y

division :: Int -> Int -> Int
division x y = x `div` y

calculadora :: String -> Int -> Int -> Int
calculadora x y z
    | x == "+" = suma y z
    | x == "-" = resta y z
    | x == "*" = multiplicacion y z
    | x == "/" = division y z

main :: IO ()
main = do 
    a <- getLine
    b <- getLine
    putStrLn $ "Suma: " ++ (show (calculadora "+" (read a) (read b)))
    putStrLn $ "Resta: " ++ (show (calculadora "-" (read a) (read b)))
    putStrLn $ "Multiplicacion: " ++ (show (calculadora "*" (read a) (read b)))
    putStrLn $ "Division: " ++ (show (calculadora "/" (read a) (read b)))