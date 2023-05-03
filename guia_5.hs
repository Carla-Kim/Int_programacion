--1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--1.2
ultimo :: [t] -> t
ultimo lista | longitud lista == 1 = head(lista)
             | otherwise = ultimo(tail(lista))

ultimo2 :: [t] -> t
ultimo2 lista = head(reverso(lista))

--1.3
principio :: [t] -> [t]
principio lista = reverso(tail(reverso(lista)))

{- principio2 :: [t] -> [t]
principio2 lista -}

--1.4
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso(xs) ++ (x : [])

--2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x lista | head(lista) == x = True
                  | otherwise = pertenece x (x:lista)

pertenece1 :: (Eq t) => t -> [t] -> Bool 
pertenece1 valorABuscar lista | longitud(lista) == 0 = False
                              | head(lista) == valorABuscar = True 
                              | otherwise = pertenece valorABuscar (tail lista)

--2.2 
{- todosIguales :: (Eq t) => [t] -> Bool
todosIguales 

--2.3
todosDiferentes :: (Eq t) => [t] -> Bool
todosDiferentes lista | not(todosIguales lista) = True
                      | otherwise = False

--2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos -}