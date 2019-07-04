'''
PEP 2, 2019-1, Ejercicio 2.
La gente de YouTube esta desarrollando un estudio de
comportamiento de los usuarios frente a los videos de la plataforma...
'''
# BLOQUE DE IMPORTACION
import matplotlib.pyplot as p
import numpy as np

# BLOQUE DE DEFINICION

# Descripcion: Lee las lineas de un archivo y retorna una lista de strings con ellas
# Entrada: Nombre del archivo como string
# Salida: Lista de strings con las lineas del archivo
def leerArchivo(nombre):
  archivo = open(nombre, "r")
  texto = archivo.readlines()
  archivo.close()
  return texto

# Descripcion: Cuenta la cantidad de likes/dislikes/visualizaciones por fecha
# Entrada: Lista de strings con los datos de las visualizaciones
# Salida: Lista de listas con los datos por fecha
def contarDatos(lineas):
  likes = 0
  dislikes = 0
  visualizaciones = 0

  fechaActual = ""
  fechas = []

  # fechas = [ 
  #   [fecha, visualizaciones, likes, dislikes],
  #   [fecha, visualizaciones, likes, dislikes],
  #   [fecha, visualizaciones, likes, dislikes]
  #   ...
  # ]
  for linea in lineas:
    linea = linea.split(",")

    if linea[0] != fechaActual:
      fechas.append([fechaActual, likes, dislikes, visualizaciones])
      fechaActual = linea[0]
      likes = 0
      dislikes = 0
      visualizaciones = 0

    if linea[3].strip() == "LIKE":
      likes += 1

    if linea[3].strip() == "DISLIKE":
      dislikes += 1

    visualizaciones += 1

  # Agregar ultima fecha
  fechas.append([fechaActual, likes, dislikes, visualizaciones])
  # Remover primer registro en blanco
  fechas.pop(0)

  # Retornar fechas
  return fechas

# Descripcion: Convierte las listas en el tipo de datos vector/array de numpy
# Entrada: Lista de listas
# Salida: Lista arrays de numpy
def convertirDatos(datos):
  listas = [[], [], [], []]

  for dato in datos:
    listas[0].append(dato[0])    # fecha
    listas[1].append(dato[1])    # likes
    listas[2].append(dato[2])    # dislikes
    listas[3].append(dato[3])    # visualizaciones

  comoNumpy = []
  comoNumpy.append(np.array(listas[0]))
  comoNumpy.append(np.array(listas[1]))
  comoNumpy.append(np.array(listas[2]))
  comoNumpy.append(np.array(listas[3]))

  return comoNumpy

# Descripcion: Genera la grafica con los datos del video
# Entrada: 
# Salida: Lista de strings con las lineas del archivo
def graficar(datos):
  f_likes = p.plot(datos[0], datos[1], label = "LIKES")
  f_dislikes = p.plot(datos[0], datos[2], label = "DISLIKES")
  f_visualizaciones = p.plot(datos[0], datos[3], label = "VISUALIZACIONES")

  p.title("Videos Mas Vistos")
  p.ylabel("Cantidad")
  p.xlabel("Fechas")

  p.legend()
  p.show()


# BLOQUE PRINCIPAL
## ENTRADA
texto = leerArchivo("pelicula.txt")
## PROCESAMIENTO
datos = contarDatos(texto)
convertidos = convertirDatos(datos)
## SALIDA
graficar(convertidos)
