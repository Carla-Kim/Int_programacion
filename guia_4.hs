--1.
fib :: Integer -> Integer 
fib x | x == 0 = 0
      | x == 1 = 1
      | otherwise = fib (x - 1) + fib (x - 2)

fibonacci :: Integer -> Integer 
fibonacci x = fib (x)

--2
parteEntera :: Float -> Integer
parteEntera x | ((x < 1) && (x >= 0))  || ((x > (-1)) && (x <= 0)) = 0
              | x >= 0 = parteEntera (x -1) + 1
              | x <= 0 = parteEntera (x + 1) - 1

--3 
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | (x > y) || (x - y > 0) = False 
                | (x - y == 0) = True 
                | otherwise = esDivisible (x - y) y 

--4 
sumaImpares :: Integer -> Integer
sumaImpares x | x == 0 = 0
              | otherwise = (2 * x - 1) + sumaImpares (x - 1)

--5
medioFact :: Integer -> Integer
medioFact x |  (x == 0 || x == 1) = 1
            | otherwise = (x) * medioFact (x - 2) 

--6
sumaDigitos :: Integer -> Integer
sumaDigitos x | x == 0 = 0
              | otherwise = (mod x 10) + sumaDigitos (div x 10)

--7: dado un numero entero: true si al comparar todos los dígitos de un número son iguales y false si no lo son
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x | x < 10 = True
                      | (unidades x == decenas x) = todosDigitosIguales(div x 10)
                      | otherwise = False

unidades :: Integer -> Integer
unidades x = mod x 10

decenas :: Integer -> Integer 
decenas x = unidades(div x 10)

--8: dado un número y una posición, nos devuelve el valor del digito del número de esa posición. 113 2 3
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito x y | y == cantDigitos x = unidades x
                 | otherwise = iesimoDigito (div x 10) y

cantDigitos :: Integer -> Integer 
cantDigitos x | x < 10 = 1
              | otherwise = 1 + cantDigitos (div x 10)

      -- Tenes que aprender a analizarlo como una computadora, de ir analizando caso por caso

--9: 
{- esCapicua :: Integer -> Bool
esCapicua x -}

--10.a
f1 :: Integer -> Integer
f1 x | x == 0 = 0
     | otherwise = (2 ^ x) + f1 (x - 1)

--10.b:
f2 :: Integer -> Float -> Float
f2 x y | x == 0 = 0
       | otherwise = (y ^ x) + f2 (x - 1) y

--10.c: x=2 y=2, 2^4 + 2^3 + 2^2 + 2^1 + 2^0 = 30. En este ejercicio para hacer la sumatoria desde 2*x llame a f2 (que cumple una función parecida) y la llame de x a 2*x)
f3 :: Integer -> Float -> Float 
f3 x y = f2 (2 * x) y

--10.d: x=3 y=2, 2^6 + 2^5 + 2^4 + 2^3 = 120. Acá en vez de aplicar funciones muy ocmplicadas simplemente aplique prop. de sumatoria de restar la sum de 2*x con la sum de x-1.
f4 :: Integer -> Float -> Float
f4 x y = f2 (2 * x) y - f2 (x - 1) y

--11: fromIntegral :: (Num b, Integral a) => a -> b. A partir de esta declaración podemos decir que toma un número entero y lo convierte en un número más general. Esto es útil cuando estas trabajando con números reales y enteros al mismo tiempo
factorial :: Integer -> Integer
factorial x | x == 0 = 1
            | otherwise = x * factorial (x -1)

eAprox :: Integer -> Float 
eAprox x | x == 0 = 1
         | otherwise = 1 / fromIntegral (factorial x ) + eAprox (x - 1)

e :: Float
e = eAprox 10

--12:
{- raizDe2Aprox :: Float -> Float
raizDe2Aprox x | x == 2 = 0
               | otherwise = ((2 + (1 / x)) -1 ) + raizDe2Aprox (x - 1) -}

--13
simpleSumatoria :: Integer -> Integer -> Integer
simpleSumatoria i j | j == 0 = 0
                    | otherwise = (i ^ j) + simpleSumatoria i (j-1)

dobleSumatoria :: Integer -> Integer -> Integer
dobleSumatoria i j | i == 0 = 0
                   | otherwise = simpleSumatoria i j + dobleSumatoria (i - 1) j 

--14









---------------------------

combinacionesMenoresOiguales :: Integer -> Integer
combinacionesMenoresOiguales x | (contadorSum x * sumaGauss x) <= x = 1
                               | otherwise = 0

sumaGauss :: Integer -> Integer
sumaGauss x = (div (x * (x + 1)) 2)

contadorSum:: Integer -> Integer
contadorSum x | x == 0 = 0
              | otherwise = x + contadorSum (x - 1)