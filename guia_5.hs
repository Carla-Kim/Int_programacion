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

--1.4
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso(xs) ++ (x : [])

--2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:lista) | y == x = True
                      | otherwise = pertenece x lista

pertenece1 :: (Eq t) => t -> [t] -> Bool 
pertenece1 valorABuscar lista | longitud(lista) == 0 = False
                              | head(lista) == valorABuscar = True 
                              | otherwise = pertenece valorABuscar (tail lista)

--2.2 
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:resto) | x == y = todosIguales (y:resto)
                         | otherwise = False

--2.3
todosDiferentes :: (Eq t) => [t] -> Bool
todosDiferentes lista | not(todosIguales lista) = True
                      | otherwise = False

--2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:y:lista) | x == y = True
                         | otherwise = hayRepetidos lista

--2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar elem (x:lista) | elem == x = lista
                      | otherwise = x : quitar elem lista

--2.6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos elem lista | pertenece elem lista == False = lista
                       | pertenece elem lista == True = quitarTodos elem (quitar elem lista)

--2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:lista) = x : eliminarRepetidos(quitarTodos x lista)

--2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos lista1 lista2 | longitud(eliminarRepetidos(lista1)) == longitud(eliminarRepetidos(lista2)) = mismosElementosAux lista1 lista2
                              | otherwise = False

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] _ = True
mismosElementosAux (x:lista1) lista2 | pertenece x lista2 = mismosElementosAux lista1 lista2
                                     | otherwise = False

--3.3
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x : lista) | x > maximo(lista) = x 
                   | otherwise = maximo lista