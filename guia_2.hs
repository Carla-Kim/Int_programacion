doble :: Integer -> Integer
doble x = 2 * x

--1.a
f :: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

--1.b
g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

--1-c
h :: Integer -> Integer
h n = (f.g) n
-- h n = f(g(n)),  ambos son iguales 

k :: Integer -> Integer 
k n = (g.f) n

--2.a
absoluto :: Integer -> Integer 
absoluto x = abs x
    -- absoluto x | x > 0 = x
    --            | otherwise = (-x)
    --para mandar un numero negativo debemos mandarlo en parentesis

--2.b
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y |(abs x > abs y) = abs x
                   |otherwise = abs y 
    -- Es importante encapsular con () los ejercicios 

--2.c
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | (x > y) && (x > z) = x
              | (y > x) && (y > z) = y
              | otherwise = z

--2.d
    --sin pattern matching
algunoEs1 :: Float -> Float -> Bool
algunoEs1 x y = x == 0 || y == 0

    -- Con pattern matching
algunoEs2 :: Float -> Float -> Bool
algunoEs2 0 _ = True
algunoEs2 _ 0 = True
algunoEs2 _ _ = False

--2.e
    --Sin pattern matching
ambosSonCero1 :: Float -> Float -> Bool
ambosSonCero1 x y = x == 0 && y == 0

    --Con pattern matching
ambosSonCero2 :: Float -> Float -> Bool
ambosSonCero2 0 0 = True
ambosSonCero2 _ _ = False

--2.f
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | (x <= 3 && y <= 3) = True
                   | (x < 3 && x >= 7) && (y < 3 && y >= 7) = True
                   | (x > 7 && y > 7) = True
                   | otherwise = False

--2.g
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x == y && x == z = x
                    | x == y = x + z
                    | x == z = x + y
                    | y == z = y + x 
                    | otherwise = x + y + z

--2.h
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y | x `mod` y == 0 = True
                 | otherwise = False

--2.i
digitoUnidades :: Integer -> Integer
digitoUnidades x = mod x 10

--2.j
digitoDecenas :: Integer -> Integer
digitoDecenas x = div ((mod x 100) - (mod x 10)) 10
    -- mod 100 -> xy - mod 10 -> y = x0
    -- x0 / 10 = x 

--3.
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados x y | x /= 0 && (-x) `mod` y == 0 = True
                      | otherwise = False

--4.a
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt coord1 coord2 = (fst coord1 * fst coord2) + (snd coord1 * snd coord2)
-- D: ¿qué es el producto interno? -> dando dos tuplas se multiplican las x y las y y se suman.

--4.b
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor tupla1 tupla2 | (fst tupla1 < fst tupla2) && (snd tupla1 < snd tupla2) = True
                        | otherwise = False

--4.c
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos tupla1 tupla2 = sqrt((fst tupla1 + fst tupla2)^2 + (snd tupla1 + snd tupla2)^2)

--4.d
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (x, y, z) = (x + y + z)

--4.e
--sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
--sumarSoloMultiplos (x, y, z) divisor

--4.f
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x, y, z) | mod x 2 == 0 = 0
                       | mod y 2 == 0 = 1
                       | mod z 2 == 0 = 2
                       | otherwise = 4

--4.g
crearPar :: tx -> ty -> (tx, ty)
crearPar x y = (x, y)

--4.h 
invertir :: (tx, ty) -> (ty, tx)
invertir (x, y) = (y, x)

--5
esPar :: Integer -> Bool
esPar x = mod x 2 == 0

f1 :: Integer -> Integer
f1 x | x >= 7 = x^2
     | x < 7 = 2*x - 1

g1 :: Integer -> Integer
g1 y | esPar y = div y 2
     | otherwise = 3*y + 1

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) | (f1 n1 > g1 n1) && (f1 n2 > g1 n2) && (f1 n3 > g1 n3) = True
                          | otherwise = False

--6
bisiesto :: Integer -> Bool
bisiesto x | (not (esMultiploDe x 4) || ((esMultiploDe x 100) && not (esMultiploDe x 400))) = False
           | otherwise = True

--7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float 
distanciaManhattan (p1, p2, p3) (q1, q2, q3) = abs (p1 - q1) + abs (p2 - q2) + abs (p3 - q3)

--8 
sumaUltimoDosDigitos :: Integer -> Integer
sumaUltimoDosDigitos x  = (mod x 10) + (mod (div x 10) 10)
    --la funcion piso siempre sera un numero entero, no hay necesidad de que exista una funcion piso

comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimoDosDigitos a < sumaUltimoDosDigitos b = 1
             | sumaUltimoDosDigitos a > sumaUltimoDosDigitos b = (-1)
             | sumaUltimoDosDigitos a == sumaUltimoDosDigitos b = 0
    --este simbolo ≺ es el equivalente de la palabra comparar dentro del mundo de los numeros
