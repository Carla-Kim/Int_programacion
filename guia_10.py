'''
notas:
- read() -> ("perro /ngato /nsapo")
- readline() -> ("perro")
- readlines() -> ("perro", "gato", "sapo")
- #in -> chequea en cada instancia en la linea si existe la palabraEnviada dentro (str contiguos), es un booleano.
- #split() tiene la funcion de separar "a b c" y devolver "a", "b", "c". devuelve sin los espacios y sin los saltos

'''

#1.2
def contarLineas(archivoEnviado: str) -> int:
    archivo = open(archivoEnviado, "r")
    contador: int = 0
    for linea in archivo.readlines():
        contador += 1
        
    archivo.close()
    return contador
    
#print(contarLineas("archivotest.txt"))

#1.2: notar que la linea es "texto texto" y no "texto", "texto"
def existePalabra(palabraEnviada: str, archivoEnviado: str) -> bool:
    archivo = open(archivoEnviado, "r")
    listaDeLineas: list[str] = archivo.readlines()
    for linea in listaDeLineas:
        if palabraEnviada in linea: #in -> chequea en cada instancia en la linea si existe la palabraEnviada dentro (str contiguos)
            return True
    archivo.close()
    return False

#print(existePalabra("texto", "archivotest.txt"))

#1.3
def cantidadApariciones(archivoEnviado: str, palabraEnviada: str) -> int:
    cantidadApariciones: int = 0
    archivo = open(archivoEnviado, "r")
    contenido =  archivo.readlines()
    listaDePalabras: list[str] = []
    
    for lista in contenido:
        listaDePalabras += lista.split() #+= une las palabras/elementos por separado
        
    for palabra in listaDePalabras:
        if palabraEnviada in palabra:
            cantidadApariciones += 1
    archivo.close()
    
    return cantidadApariciones

#print(cantidadApariciones("archivotest.txt", "texto"))

#2
def clonarSinComentarios(nombre_archivo: str):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.readlines()
    listaDeListaDePalabras: list[str] = []

    for linea in contenido:
        listaDeListaDePalabras.append(linea.split()) # .append une listas

    destino = open("clonSinComentarios.txt", "w", encoding = "utf8")
    
    for l in range(0, len(listaDeListaDePalabras)):
        if listaDeListaDePalabras[l][0] != "#":
            destino.write(contenido[l])
    
    archivo.close()
    destino.close()

#print(clonarSinComentarios("archivotest.txt"))

#3
def textoReverso(nombre_archivo: str):
    archivo = open(nombre_archivo, "r")
    destino = open("reverso.txt", "w", encoding = "utf8")
    destino.truncate()

    for linea in reversed(archivo.readlines()):
        destino.write(linea)
    #.reverse() no se lo puede usar para elementos iterables pero si reversed(), notar que reverse() cambia la lista en su lugar y solo deberiamos llamar a la funcion que le aplicamos el reverse, pero el reversed() crea una copia

    archivo.close()
    destino.close()

#print(textoReverso("archivotest.txt"))