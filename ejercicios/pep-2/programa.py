'''
No-se-que-pep
'''
# BLOQUE DE IMPORTACION
from numro import convertirARomano

# BLOQUE DE DEFINICION

# Descripcion: Lee las lineas de un archivo y retorna una lista de strings con ellas
# Entrada: Nombre del archivo como string
# Salida: Lista de strings con las lineas del archivo
def leerArchivo(nombre):
  archivo = open(nombre, "r")
  texto = archivo.readlines()
  archivo.close()
  return texto

# Descripcion: Escribe la lista de strings 'texto' en el archivo 'nombre'
# Entrada: Nombre del archivo como string
# Salida: True en caso de exito.
def escribirArchivo(nombre, texto):
  archivo = open(nombre, "w")
  for linea in texto:
    archivo.write(linea + "\n")
  archivo.close()
  
  return True

# Descripcion: Cuenta la cantidad de veces que se ha repedito un elemento hasta cierta posicion 
# Entrada:  Lista (list) de elementos
#           Posicion (int) hasta donde contar
# Salida: Cantidad de veces (int) que se repite el elemento
def contar(listaReyes, posicion):
  contador = 0
  nombreRey = listaReyes[posicion]
  while posicion >= 0:
    if listaReyes[posicion] == nombreRey:
      contador += 1
    posicion -= 1

  return contador

# Descripcion: Crea la lista de nombres nuerada 
# Entrada: Lista de nombres
# Salida: Lista de strings con los nombres y su numero romano
def crearListaNumerada(listaReyes):
  posicionActual = 0
  listaReyesNumerada = []

  while posicionActual < len(listaReyes):
    numero = contar(listaReyes, posicionActual)
    numeroEnRomano = convertirARomano(numero)
    listaReyesNumerada.append(listaReyes[posicionActual].strip("\n") + " " + numeroEnRomano)
    posicionActual += 1

  return listaReyesNumerada

# BLOQUE PRINCIPAL
# ENTRADA
listaReyes = leerArchivo("dinastias.txt")
# PROCESAMIENTO
listaReyesNumerada = crearListaNumerada(listaReyes)
# SALIDA
if escribirArchivo("dinastiasNumeradas.txt", listaReyesNumerada):
  print("Archivo 'dinastiasNumeradas.txt' generado correctamente.")
else:
  print("Error al generar el archivo.")
