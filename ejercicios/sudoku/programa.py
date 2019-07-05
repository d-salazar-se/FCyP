"""
Determina si la matriz ingresada es efectivamente una de sudoku valida
"""
# BLOQUE DE IMPORTACION
# ~ no aplica

# BLOQUE DE DEFINICION

# Descripcion: Lee las lineas de un archivo y retorna una lista de strings con ellas
# Entrada: Nombre del archivo como string
# Salida: Lista de strings con las lineas del archivo
def leerArchivo(nombre):
  archivo = open(nombre, "r")
  texto = archivo.readlines()
  archivo.close()
  return texto

# Descripcion: Generar una lista con los datos de 1 columna 
# Entrada: Me da flojera hacer el resto.
# Salida: Me da flojera hacer el resto.
def obtenerColumna(matriz, indiceColumna):
  columna = []
  for fila in matriz:
    columna.append(fila[indiceColumna])
  return columna

# Descripcion: Me da flojera hacer el resto.
# Entrada: Me da flojera hacer el resto.
# Salida: Me da flojera hacer el resto.
def generaMatriz(texto):
  matriz = []

  for linea in texto:
    numeros = []
    for numero in linea.strip("\n").split(" "):
      numeros.append(int(numero))
    matriz.append(numeros)

  return matriz

# Descripcion: Me da flojera hacer el resto.
# Entrada: Me da flojera hacer el resto.
# Salida: Me da flojera hacer el resto.
def generarMatriz3x3(matriz, x, y):
  cuadrado3x3 = [[0,0,0],[0,0,0],[0,0,0]]

  cuadrado3x3[0][0] = matriz[x][y]
  cuadrado3x3[0][1] = matriz[x][y+1]
  cuadrado3x3[0][2] = matriz[x][y+2]

  cuadrado3x3[1][0] = matriz[x+1][y]
  cuadrado3x3[1][1] = matriz[x+1][y+1]
  cuadrado3x3[1][2] = matriz[x+1][y+2]

  cuadrado3x3[2][0] = matriz[x+2][y]
  cuadrado3x3[2][1] = matriz[x+2][y+1]
  cuadrado3x3[2][2] = matriz[x+2][y+2]

  return cuadrado3x3

# Descripcion: Valida que los valores de una lista de 9 elementos sean todos distintos entre ellos
# Entrada: Me da flojera hacer el resto.
# Salida: Me da flojera hacer el resto.
def validarLista(lista):
  contados = 0
  for i in range(1, 10):
    if i in lista:
      contados += 1

  if contados == 9:
    return True
  else:
    return False

# Descripcion: Valida que los valores de una matriz de 3x3 (9 elementos) sean todos distintos entre ellos
# Entrada: Me da flojera hacer el resto.
# Salida: Me da flojera hacer el resto.
def validar3x3(matriz):
  ingresados = []
  for x in range(3):
    for y in range(3):
      if matriz[x][y] not in ingresados:
        ingresados.append(matriz[x][y])
  
  if len(ingresados) == 9:
    return True
  else:
    return False

# Descripcion: Valida las 3 reglas del sudoku (horizontal/vertical/cuadrados)
# Entrada: Me da flojera hacer el resto.
# Salida: Me da flojera hacer el resto.
def validarSudoku(matriz):
  # Validar filas
  fila = 0
  while fila < len(matriz):
    if not validarLista(matriz[fila]):
      print("Fila " + str(fila+1) +" no cumple la regla del sudoku.")
      return False
    fila += 1

  # Validar columnas
  columna = 0
  while columna < len(matriz[0]):
    listaColumna = obtenerColumna(matriz, columna)
    if not validarLista(listaColumna):
      print("Columna " + str(columna+1) + " no cumple la regla del sudoku.")
      return False
    columna += 1

  # Validar los 9 cuadrados 3x3
  x = 0
  while x < 9:
    y = 0
    while y < 9:
      matriz3x3 = generarMatriz3x3(matriz, x, y)
      if not validar3x3(matriz3x3):
        return False
      y += 3
    x += 3

  return True

# BLOQUE PRINCIPAL
## ENTRADA
texto = leerArchivo("sudoku.txt")
## PROCESAMIENTO
matriz = generaMatriz(texto)
## SALIDA
if validarSudoku(matriz):
  print("Tablero valido")
else:
  print("El tablero no es valido")
