suma :: Int -> Int -> Int
suma x y = x + y

resta :: Int -> Int -> Int
resta x y = x - y

multiplicacion :: Int -> Int -> Int
multiplicacion x y = x * y

division :: Int -> Int -> Int
division x y = x `div` y

calculadora :: (a -> Int -> Int) -> a -> Int -> Int
calculadora f x y = f x y

main :: IO ()
main = do 
    a <- getLine
    b <- getLine
    putStrLn $ "Suma: " ++ (show (calculadora suma (read a) (read b)))
    putStrLn $ "Resta: " ++ (show (calculadora resta (read a) (read b)))
    putStrLn $ "Multiplicacion: " ++ (show (calculadora multiplicacion (read a) (read b)))
    putStrLn $ "Division: " ++ (show (calculadora division (read a) (read b)))