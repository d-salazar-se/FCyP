"""
Construya un programa en Python que lea una matriz desde un archivo
de texto y permita a un usuario escoger una de las siguientes operaciones,
a realizar sobre la matriz:
- Encontrar el determinante
- Trasponer la matriz
- Encontrar la matriz identidad
- Encontrar la matriz inversa
"""
import numpy as np

def leerMatriz(nombreArchivo):
	nombreArchivo = nombreArchivo.strip(".txt") + ".txt"
	archivo = open(nombreArchivo, "r")
	lineas = archivo.readlines()
	archivo.close()
	return lineas

def convertirAMatrix(lineas):
	matriz = []
	for linea in lineas:
		filaComoNumero = []
		for item in linea.split(" "):
			filaComoNumero.append(int(item))
		matriz.append(filaComoNumero)
	return np.array(matriz)

def determinante(matrix):
	print("\nEl determinante de la matriz es: ")
	print(np.linalg.det(matrix))
	print()

def trasponer(matrix):
	print("\nLa matriz transpuesta corresponde a: ")
	print(matrix.transpose())
	print()

def identidad(matrix):
	print("\nLa matriz identidad corresponde a: ")
	print(np.identity(len(matrix[0])))
	print()

def inversa(matrix):
	print("\nLa matriz inversa corresponde a: ")
	print(np.linalg.inv(matrix))
	print()

def menu():
	print("~~ Menu ~~")
	print("[1] Encontrar el determinante")
	print("[2] Trasponer matriz")
	print("[3] Encontrar la matriz identidad")
	print("[4] Encontrar la matriz inversa")
	print("[5] Salir")
	print()

	opcion = int(input("[ > ] Ingrese opcion: "))

	return opcion

#=================================+
# BLOQUE PRINCIPAL
#=================================+

# ENTRADA
lineas = leerMatriz("matriz.txt")

# PROCESAMIENTO
matrix = convertirAMatrix(lineas)

# SALIDAS
opcion = 1
while opcion != 5:
	opcion = menu()

	if opcion == 1:
		determinante(matrix)
	elif opcion == 2:
		trasponer(matrix)
	elif opcion == 3:
		identidad(matrix)
	elif opcion == 4:
		inversa(matrix)
	elif opcion == 5:
		print("[ ~ ] Cerrando aplicacion...")
	else:
		print("[ ! ] Opción incorrecta, ingrese de nuevo.")
		opcion = 1

print("[ ~ ] Bye~")
