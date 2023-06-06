import math

#-------------------------- ejercicio 1 --------------------------#

#1.1
def raizDe2() -> float:
    resultado : float = round(math.sqrt(2), 4)
    print(resultado) #esto imprime el resultado
    return resultado #esto retorna el resultado

#1.2
def imprimir_hola() -> None:   #no devuelve nada
    print('hola')

#1.3

def imprimir_un_verso() -> None:
    print("I wanna go to the ocean where I'm free\nThe forest for the color changing leaves")

#1.4

def factorial_2() -> int:
    return 1 * 2

#1.5

def factorial_3() -> int:
    return 1 * 2 * 3

#1.6

def factorial_4() -> int:
    return 1 * 2 * 3 * 4

#1.7
def factorial_5() -> int:
    return 1 * 2 * 3 * 4 * 5

#-------------------------- ejercicio 2 --------------------------#

#2.1
def imprimir_saludo(nombre: str) -> None:
    #nombre: str  
    #nombre = 'Thomy'                 
        #si pongo esto se va a imprimir siempre Thomy y nunca el nombre que le pase por parametro
    print('Hola '+ nombre)


#2.2
def raiz_cuadrada_de(numero: int) -> int:
    return math.sqrt(numero)

#2.3
def imprimir_dos_veces(estribillo: str) -> None:
    estribillo = "I wanna go to the ocean where I'm free\nThe forest for the color changing leaves" 
    print(estribillo + estribillo) #el + concatena 2 string
    print(estribillo * 2) #el * necesita de un int para concatenarse con si mismo n veces

#2.4
def es_multiplo_de(n: int, m: int) -> bool:
    return n % m == 0

#2.5
def es_par(numero: int) -> int:
    return es_multiplo_de(numero, 2)

#2.6
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    cantidad_de_piezas = comensales * min_cant_de_porciones
    return math.ceil(cantidad_de_piezas/8)  
    #cada pizza se divide en 8 piezas

#-------------------------- ejercicio 3 --------------------------#

#3.1
def alguno_es_0(numero_1: int, numero_2: int) -> bool:
    return numero_1 == 0 or numero_2 == 0

#3.2
def ambos_son_0(numero_1: int, numero_2: int) -> bool:
    return numero_1 == 0 and numero_2 == 0

#3.3
def es_nombre_largo(nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

#3.4
def es_bisiesto(anio: int) -> bool:
    return (es_multiplo_de(anio, 400) or es_multiplo_de(anio, 4)) and not(es_multiplo_de(anio, 100))

#-------------------------- ejercicio 4 --------------------------#
#¿Cómo usaron min y max?
def peso_pino(altura_metros: int) -> int:
    peso: int
    if (altura_metros <= 3):
        peso = altura_metros * 300 #altura en metros * 100(m a cm) * 3 mts.
    else:
        peso_hasta_3 = altura_metros * 300
        peso_mas_de_3 = altura_metros * 200 #altura en metros * 100(m a cm) * 2 mts.
        peso = peso_hasta_3 + peso_mas_de_3
    return peso

def es_peso_util(peso: int) -> bool:
    return  peso >= 400 and peso <= 1000

def sirve_pino(altura_metros: int) -> bool:
    return es_peso_util(peso_pino(altura_metros))

#-------------------------- ejercicio 5 --------------------------#
# #5.1: ¿cuál es la diferencia entre ambas?
def devolver_el_doble_si_es_par(un_numero: int) -> int:
    res: int #hay que nombrar las variables de antemano para que sea valido
    if (es_par(un_numero)):
        res = un_numero * 2
    else:
        res = un_numero 
    return res

def devolver_el_doble_si_es_par2(un_numero: int) -> int:
    if (es_par(un_numero)):
        return un_numero * 2
    else:
        return un_numero

#5.2: Basta con usar un if_else dado que es par o no.
def devolver_el_valor_si_es_par_sino_el_que_sigue(un_numero: int) -> int:
    res: int
    if (es_par(un_numero)):
        res = un_numero
    else:
        res = un_numero + 1
    return res

#5.3: Basta con usat un if_elif_else pues son tres opciones: multiplo de 3, muiltiplo de 9 o ninguno.
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(un_numero: int) -> int:
    res: int
    if (es_multiplo_de(un_numero, 3)):
        res = un_numero * 2
    elif (es_multiplo_de(un_numero, 9)):
        res = un_numero * 3
    else:
        res = un_numero
    return res

#5.4
def nombre_con_muchas_letras_o_no(nombre: str) -> None:
    if (len(nombre) >= 5):
        print("¡Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres.")

#5.5
def es_hora_de_agarrar_la_pala(sexo: str, edad: int) -> None:
    if (edad < 18):
        print("Andá de vacaciones")
    elif ((sexo == "F" and edad >= 60) or (sexo == "M" and edad >= 65)):
        print("Andá de vacaciones")
    else:
        print("Es hora de levantar la pala")

#-------------------------- ejercicio 6 --------------------------#
#6.1
def imprimir_del_1_al_10() -> None:
    x = 1
    while (x <= 10):
        print(x)
        x += 1

#6.2
def imprimir_del_10_al_40_pares() -> None:
    x = 10
    while (x <=40):
        if (es_par(x)):
            print(x)
            x += 1
        else:
            x += 1

#6.3
def imrpimir_10_veces_eco() -> None:
    x = 1
    while (x <= 10):
        print("eco")
        x += 1

#6.4
def cuenta_regresiva() -> None:
    x = 10
    while(x >= 1):
        print(x)
        if (x == 1):
            print("Despegue!")
        x -= 1 #el lugar donde ubicamos el contador o descontador es importante pues el orden en el cual se realiza el algoritmo es de arriba hacia abajo

#6.5
def viaje_en_el_tiempo_atras(anio_partida: int, anio_llegada: int) -> None:
    x = anio_partida
    while (x >= anio_llegada):
        print("Viajó un año al pasado, estamos en el año: " + str(x))
        x -= 1

#6.6
def viaje_en_el_tiempo_hasta_aristoteles(anio_partida: int) -> None:
    x = anio_partida
    while (x >= (-384)):
        print("Viajo un año al pasado, estamos en el anio: " + str(x))
        x -= 20

#-------------------------- ejercicio 7 --------------------------#
#7.1
def for_imprimir_del_1_al_10() -> None:
    for num in range(1, 11):
        print(num)

#7.2
def for_imprimir_del_10_al_40_pares() -> None:
    for num in range(10, 41, 2):
        print(num)

#7.3
def for_imprimir_10_eco() -> None:
    for num in range(1, 11):
        print("eco")

#7.4
def for_cuenta_regresiva() -> None:
    for num in range(10, 0, -1):
        print(num)
        if num == 1:
            print("¡Despegue!")

#7.5
def for_viaje_en_el_tiempo(anio_partida: int, anio_llegada: int) -> None:
    for num in range(anio_partida, (anio_llegada - 1), -1):
        print("Viajó un año al pasado, estamos en el año: " + str(num))

#7.6
def for_viaje_en_el_tiempo_hasta_aristoteles(anio_partida: int) -> None:
    for num in range(anio_partida, (-385), -20):
        print("Viajó un año al pasado, estamos en el año: " + str(num))
