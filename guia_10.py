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
    
print(contarLineas("archivotest"))

#1.2: notar que la linea es "texto texto" y no "texto", "texto"
def existePalabra(palabraEnviada: str, archivoEnviado: str) -> bool:
    archivo = open(archivoEnviado, "r")
    listaDeLineas: list[str] = archivo.readlines()
    for linea in listaDeLineas:
        if palabraEnviada in linea: #in -> chequea en cada instancia en la linea si existe la palabraEnviada dentro (str contiguos)
            return True
    archivo.close()
    return False

print(existePalabra("texto", "archivotest"))

#1.3
def cantidadApariciones(archivoEnviado: str, palabraEnviada: str) -> int:
    cantidadApariciones: int = 0
    archivo = open(archivoEnviado, "r")
    contenido =  archivo.readlines()
    listaDePalabras: list[str] = []
    
    for lista in contenido:
        listaDePalabras += lista.split()
        
    for palabra in listaDePalabras:
        if palabraEnviada in palabra:
            cantidadApariciones += 1
    archivo.close()
    
    return cantidadApariciones

print(cantidadApariciones("archivotest", "texto"))