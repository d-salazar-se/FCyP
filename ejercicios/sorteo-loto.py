'''
Dado...
'''
from random import choice

# D: Genera una lista con 6 numeros pseudo-aleatorios
# E: No aplica.
# S: lista (list) de 6 numeros enteros.
def generarSorteo():
	sorteo = []
	listadoNumeros = list(range(1, 46))
	i = 0

	while i < 6:
		numero = choice(listadoNumeros)
		listadoNumeros.remove(numero)
		sorteo.append(numero)
		i += 1

	return sorteo

# D: Pedir numeros de su loto al usuario.
# E: No aplica.
# S: lista (list) de 6 numeros enteros.
def pedirDatosAlUsuario():
	listadoNumeros = []
	i = 0
	while i < 6:
		numero = int(input("[>] Ingrese numero [" + str(i+1) + "]: "))

		if (numero not in listadoNumeros) and (0 < numero and numero < 46):
			listadoNumeros.append(numero)
			i += 1
		else:
			print("[X] Debes ingresar un numero entre 0 y 45 que no hayas ingresado previamente!")

	return listadoNumeros

# D: Determinar numero de aciertos del usuario
# E: numerosSorteo (list) Lista de numeros enteros del sorteo
# 	 numerosUsuario (list) Lista de numeros enteros del usuario
# S: Numero de aciertos o coincidencias (int)
def determinarAciertos(numerosSorteo, numerosUsuario):
	numeroAciertos = 0
	i = 0
	while i < len(numerosUsuario):
		if numerosUsuario[i] in numerosSorteo:
			numeroAciertos += 1
		i += 1

	return numeroAciertos

# 
# BLOQUE PRINCIPAL
# 

# ENTRADA
numerosDelUsuario = pedirDatosAlUsuario()

# PROCESAMIENTO
numerosDelSorteo = generarSorteo()
numeroAciertos = determinarAciertos(numerosDelSorteo, numerosDelUsuario)

# SALIDA
print("Los numeros del sorteo son: ")
print(numerosDelSorteo)

if numeroAciertos > 3:
	print("Ganaste")
else:
	print("Perdiste")

