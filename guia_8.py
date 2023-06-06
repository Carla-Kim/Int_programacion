import math

# Ejercicio 1
#1.1
def pertenece1(s: list[int], e: int) -> bool:
    return e in s

def pertenece2(s: list[int], e: int) -> bool:
    for i in range(0, len(s) - 1):
        if(s[i] == e):
            return True
    return False

def pertenece3(s: list[int], e: int):
    contador: int = 0
    while(contador < len(s)):
        if(s[contador] == e):
            return True
            contador += 1
    return False

#1.2
def divideAtodos(s: list[int], e: int) -> bool:
    x: int = 0
    while(x < len(s) and s[x] % e == 0): 
        x += 1

    if x == len(s):
        return True
    return False

#1.3 
def sumaTotal(s: list[int]) -> int:
    sumas = 0
    for i in range(0, len(s)):
        sumas += s[i]
    return sumas

#1.4
def ordenados(s: list[int]) -> bool:
    for i in range(0, len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True 
#Para poder entender bien los ciclos uno debe ver en que caso un ciclo debe seguir iterando, uno puede iterar constantemente en una base de un caso borde o un caso que sea erroneo o un caso que queremos que funcione, en este ejemplo, es un for que chequea con un if si s[i] > s[i + 1], si llegase a haber un caso devolvera flase pero si luego de haber chequeado todo el for y el if no se cumple retorna True.
    
#1.5
def hay_palabra_mayor_a_7_Letras(s: list[str]) -> bool:
    for i in range(0, len(s)):
        if(len(s[i]) > 7):
            return True
    return False

#1.6
def palindromo(palabra: str) -> str:
    return palabra[::-1]
    # reversed(palabra)

def hayPalabraPalindroma(s: list[str]) -> bool:
    for i in range(len(s)):
        if(s[i] == palindromo(s[i])):
            return True
    return False

#1.7
def hayMayuscula(palabra: str) -> bool:
    for char in palabra:
        if char.isupper():
            return True
    return False

def hayNumero(palabra: str) -> bool:
    for char in palabra:
        if char.isdigit():
            return True
    return False

def hayMinuscula(palabra: str) -> bool:
    for char in palabra:
        if char.islower():
            return True
    return False

def contraseñaFuerte(password: str) -> str:
    res: str
    if(len(password) > 8 
       and hayMayuscula(password) 
       and hayMinuscula(password) 
       and hayNumero(password)):
        res = "VERDE"
    elif(len(password) < 5):
        res = "ROJO"
    else: 
        res = "AMARILLO"
    return res

#print(contraseñaFuerte("Ñwvywdvywdññww6")) #retorna VERDE

#1.8
def historialDeMovimientos(l: list[(str, int)]) -> int:
    saldo: int = 0
    for mov in l:
        if(mov[0] == "I"):
            saldo += mov[1]
        elif(mov[0] == "R"):
            saldo -= mov[1]
    return saldo

#1.9
def eliminar_vocales_repetidas(vocales: list[str]) -> list[str]:
    vocales_no_repetidas: str = ""
    for elem in vocales:
        if elem not in vocales_no_repetidas:
            vocales_no_repetidas += elem
    return vocales_no_repetidas 
            
def vocales_sin_repetir(palabra: int) -> list[str]:
    palabra: int = palabra.lower()
    vocales_sin_repetir: str = ""
    for char in palabra:
        if char in ["a", "e", "i", "o", "u"]:
            vocales_sin_repetir += char
    return eliminar_vocales_repetidas(vocales_sin_repetir)

def tieneAlMenos3vocalesDistintas(palabra: int) -> bool:
    if len(vocales_sin_repetir(palabra)) >= 3: 
        return True
    return False

#2.2
def cambia_par_por_cero(lista: list[int]) -> list[int]:
    for i in range(0, len(lista)):
        if(lista[i] % 2 == 0):
            lista[i] = 0
    return lista

#2.2
def cambia_par_por_cero_lista_nueva(lista: list[int]) -> list[int]:
    lista_nueva: list[int] = lista.copy()
    for i in range(0, len(lista_nueva)):
        if(lista_nueva[i] % 2 == 0):
            lista_nueva[i] = 0
    return lista_nueva

#2.3
def es_vocal(palabra: int) -> bool:
    palabra: int = palabra.lower()
    for char in palabra:
        if char in ["a", "e", "i", "o", "u"]:
            return True
    return False

#Acordarse: 'str' object does not support item assignment.
def string_sin_vocales(texto: str) -> str:
    textoSinVocales: str = ""
    for i in range(0, len(texto)):
        if(not(es_vocal(texto[i]))):
            textoSinVocales += texto[i]
    return textoSinVocales

#2.4
def reemplazaVocales(palabra: str) -> str:
    palabraConVocalesReemplazadas: str = ""
    for i in range(0, len(palabra)):
        if(es_vocal(palabra[i]) == True):
            palabraConVocalesReemplazadas += "_"
        else:
            palabraConVocalesReemplazadas += palabra[i]
    return palabraConVocalesReemplazadas 

#2.5
def darVueltaStr(palabra: int) -> int:
    palabraDadaVuelta: str = ""
    for i in range(len(palabra)-1, -1, -1):
        palabraDadaVuelta += palabra[i]
    return palabraDadaVuelta

#3.1
def lista_de_nombres() -> list[str]:
    listaDeNombres: list[str] = []
    nombre: str = ""
    while(nombre != "listo"):
        nombre = input("Ingresar nombre: ")
        if(nombre != "listo"):
            listaDeNombres += nombre
    return listaDeNombres
#el while s como un repetidor sin condiciones, que seguirá repitiendo el algoritmo hasta que pueda, uno debe de aclararle cuando parar (if), y que hacer luego con la información que recibio

def mesetaMasLarga(l: list[int]) -> int :
  contador: int = 1
  lista: list[int] = l

  for i in range(0, len(l)-1):
    if(lista[i] == lista[i+1]):
      contador +=  1
  return contador
#3.2
# def credito_de_sube() -> list[(str, int)]: