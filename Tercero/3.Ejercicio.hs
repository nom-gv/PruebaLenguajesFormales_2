palabras :: String -> [String]
palabras "" = []
palabras xp = yp : (palabras . drop 1) zp
   where (yp, zp) = span(/=' ') xp
