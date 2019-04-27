# Autoria: [Grupo 2] 10110-G-2
# Fecha: Segundo Semestre 2016
#
# Objectivo: Dibujar un arbol binario con letras
# Categoria: Ingenieria Informatica
# Descripcion: Dibujar un arbol binario con las letras de una secuencia 
# 		de caracteres ingresadas desde teclado.
#

# IMPORTACION DE LIBRERIAS
from math import ceil

# FUNCIONES

# Funcion que genera una cadena valida para el arbol, sin caracteres repetidos y pertenecientes al alfabeto ingles.
# Entrada: Un string <cadena>, Cadena de caracteres en base a la cual se genera una cadena "valida"
# Salida: Una lista <listado>, Lista con los caracteres que cumplen las dos reglas mencionadas anteriormente.
def generarCadenaValida(cadena):
	listado = []
	CARACTERES_VALIDOS = 'abcdefghijklmnopqrstuvwxyz'

	for caracter in cadena:
		if caracter in CARACTERES_VALIDOS and not caracter in listado:
			listado.append(caracter)
	return listado


# Funcion que inserta un nodo en el arbol ya estructurado.
# Entrada:
#	- Una lista <padre>, Lista que representa al nodo raiz del arbol.
#	- Un string <caracter>, String de largo 1 que contiene el caracter nuevo a ingresar, este no puede existir en el arbol.
# Salida: - no aplica.
def insertar(padre, caracter):
	
	while padre is not None:
		if caracter < padre[1]:
			if padre[0] == None:
				padre[0] = [None, caracter, None]
				return
			else:
				padre = padre[0]
		else:
			if padre[2] == None:
				padre[2] = [None, caracter, None]
				return
			else:
				padre = padre[2]

# Funcion que retorna la profundidad del arbol.
# Entrada: Una lista <raiz>, Lista de listas que representan al arbol.
# Salida: Un entero <contador>, Entero con el numero de niveles del arbol.
def obtenerProfundidad(raiz):
	nivelActual = [raiz]
	contador = 0
	while nivelActual:
		siguienteNivel = []
		for nodo in nivelActual:			
			if nodo[0]: siguienteNivel.append(nodo[0])
			if nodo[2]: siguienteNivel.append(nodo[2])
		nivelActual = siguienteNivel
		contador += 1

	return contador

# Funcion que recorre y retorna el arbol por niveles desde la raiz hacia las hojas.
# Entrada:
# 	- Una lista <arbol>, Lista de listas con el arbol y correspondientes subarboles por nivel.
# 	- Un entero <numeroNiveles>, Entero que representa la profundidad del arbol.
# Salida: Una lista <niveles>, Lista de listas con los nodos guardados en listas segun su nivel.
def obtenerNiveles(arbol, numeroNiveles):
	nivelActual = [arbol]
	
	profundidad = 0
	niveles = []
	
	for x in range(numeroNiveles):
		niveles.append([])
		
	while nivelActual:
		siguienteNivel = []

		for nodo in nivelActual:
			if nodo == None:
				if profundidad < numeroNiveles:
					niveles[profundidad+1].append(None)
					niveles[profundidad+1].append(None)
				continue
			
			
			niveles[profundidad].append(nodo[1])

			if nodo[0]:
				siguienteNivel.append(nodo[0])
			else:
				siguienteNivel.append([None,None,None])
			
			if nodo[2]:
				siguienteNivel.append(nodo[2])
			else:
				siguienteNivel.append([None,None,None])
		
		profundidad += 1
		
		if profundidad == numeroNiveles:
			return niveles

		nivelActual = siguienteNivel
		
	return niveles

# Funcion que agrega las "ramas" y espacios necesarios para generar 
# 	la estructura del arbol, basicamente "dibuja" el arbol en una matriz.
# Entrada: Una lista <arbol>, Lista con los nodos guardados por nivel en otra lista.
# Salida: Una lista <vistaImpresion>, Lista de listas (matriz) con los caracteres necesarios para ver el arbol.
def generarMatrizImpresion(arbol):
	# Maximo ancho necesario para mostrar el arbol por pantalla.
	# la funcion corresponde a 
	# ancho = 6 * ( 2 ^ (profundidad-1) )
	# por ejemplo, para un arbol de profundidad 4, tiene potencialmente 
	# 2 ^ (4-1) = 8 hijos en el nivel mas bajo, y cada uno de estos 
	# requiere 6 espacios para mostrarse => 48 espacios necesarios.
	ancho 		= 6*(2**(len(arbol)-1))
	vistaImpresion 	= []

	# primera linea, la "rama hacia la raiz"
	ramaRaiz	= '|'.center(ancho)
	lineaRamaRaiz 	= list(ramaRaiz)
	
	vistaImpresion.append(lineaRamaRaiz)

	# Por cada nivel en el arbol se agregan los nodos de ese nivel a dos "lineas".
	# Una contiene los nodos con sus ramas hacia los lados usando los caracteres
	# '-' y '+', ademas del nodo.
	# La otra contiene las ramificaciones hacia abajo usando el caracter '|'.
	for nivel in arbol:
		linea = ''
		ramas = ''
		
		# Todos los caracteres se ingresan a su nivel correspondiente (string)
		# cada nivel se compone de un par de lineas donde una guarda los nodos (linea) y sus ramas
		# laterales y la otras las ramificaciones hacia abajo (ramas).
		# Estas se agregan a la lista <vistaImpresion> como una lista, asi cada elemento 
		# de esta lista (vistaImpresion) corresponde a una lista compuesta de caracteres.
		for caracter in nivel:
			# Si no hay caracter en el espacio correspondiente,
			# agregar caracteres pertinentes pero "vacios".
			if caracter is None:
				linea += ' ' * ancho
				ramas += ' ' * ancho
				
				# Ya que no hay items en el nodo continuar hacia el siguiente ciclo.
				continue
			
			# Ingresar "ramas" a la izquierda y derecha 
			# del nodo con caracteres "-" y "+",
			# se usa la funcion "ceil" o techo para obtener un valor minimo de 1 
			# en caso que la division resulte en un numero entre 0 y 1.
			# se requiere al menos un "-" para mostrar el arbol como corresponde.
			rama = '-' * (int(ceil(ancho/4.0))-1)

			# Se guardan los caracteres para un nodo.
			dibujoCaracter 	= '+' + rama + caracter + rama + '+'
			ramificacion 	= '|' + (' '*(2*len(rama)+1)) + '|'
			
			# Centrar estas ramas en la fraccion de espacio 
			# que le corresponde
			linea += dibujoCaracter.center(ancho)
			ramas += ramificacion.center(ancho)

		# Agregar a la matriz que guarda el formato de impresion
		vistaImpresion.append(list(linea))
		vistaImpresion.append(list(ramas))
		
		# Al avanzar en la profundidad cada nodo dispone de la mitad del espacio que su padre.
		# La raiz dispone del ancho completo, pero sus dos hijos de la mitad de este, y los nodos
		# en el tercer nivel de la mitad de los del nivel 2 y asi sucesivamente.
		ancho /= 2

	return vistaImpresion

# Funcion que remueve los espacios "innecesarios" en la estructura del arbol (matriz).
# Entrada: Una lista <matrizImpresion>, Lista de listas con los caracteres que muestran el arbol.
# Salida: - no aplica.
def comprimir(matrizImpresion):
	# Recorrer las columnas desde atras hacia adelante
	for indiceColumna in range(len(matrizImpresion[0])-1, -1, -1):
		# Obtener el elemento <indiceColumna> de cada fila en la matriz y formar asi la columna.
		columna = [fila[indiceColumna] for fila in matrizImpresion]
		
		# La columna solo se remueve si todos los caracteres en ella sean espacios en blanco (" ")
		# o sean "-" y esten seguidos por otro "-", en caso contrario se considera como necesario 
		# y no se elimina.
		remover = True

		# <fila> representa los caracteres en la columna.
		# Se revisan estos caracteres para saber si son extrictamente necesarios
		# para mostrar el arbol.
		for fila in range(len(columna)):
			# Si el elemento es un "-" y el elemento del lado es no es "-" entonces se debe conservar.
			if columna[fila] == '-' and matrizImpresion[fila][indiceColumna+1] != '-':
				remover = False
			
			# Si no es espacio en blanco y no es "-" entonces se conserva automaticamente
			if columna[fila] not in [' ', '-']:
				remover = False
		# Si no cumple con las reglas anterioes se eliminan los caracteres con la funcion "del" de python
		# se elimina caracter a caracter de la columna completa.
		if remover:
			for fila in matrizImpresion:
				del fila[indiceColumna]

# Funcion muestra una lista de listas (matriz) por pantalla.
# Entrada: Una lista <matriz>, Lista de listas (matriz) con los caracteres en cada casilla.
# Salida: Un string <arbolStr>, La matriz como string guardada con los saltos de linea correspondiente.
def imprimirMatriz(matriz):
	arbolStr = ""
	# Por cada fila en la matriz
	for fila in matriz:
		# Sumar la fila a <arbolStr>
		for caracter in fila:
			arbolStr += caracter
		# Agregar el salto de linea correspondiente
		arbolStr += "\n"
	return arbolStr

# Funcion en donde se produce el bloque de codigo principal, se ha definido asi para obtener un mejor orden.
# Entrada: - no aplica.
# Salida: - no aplica.
def main():
	#-----------------------------------
	# ENTRADA
	#-----------------------------------
	cadena = raw_input("Ingrese cadena: ")

	#-----------------------------------
	# PROCESAMIENTO
	#-----------------------------------
	cadena = cadena.lower()
	# Crear una lista con caracteres validos, 
	# eliminar caracteres invalidos y repetidos
	cadena = generarCadenaValida(cadena)

	if len(cadena) < 1:
		print "[ ! ] Debes ingresar al menos una letra valida."
		return
	
	# Declarar el inicio del arbol
	# Hijo Izquierdo = None, Hijo Derecho = None,
	# Se saca el primer elemento de la lista de caracteres validos.
	primerCaracter = cadena.pop(0)
	arbol = [None, primerCaracter, None]

	# insertar en el arbol item a item
	# segun orden de ingreso
	while len(cadena) > 0:
		caracter = cadena.pop(0)
		insertar(arbol, caracter)

	# Obtener la profundidad del arbol para poder generar los niveles del arbol.
	profundidad 	= obtenerProfundidad(arbol)
	# Obtener el arbol en una lista por niveles, ordenados de izquierda a derecha
	nivelesArbol	= obtenerNiveles(arbol, profundidad)
	# Agregar los caracteres necesarios para mostrar como un arbol.
	arbolConFormato = generarMatrizImpresion(nivelesArbol)
	
	# Se remueven los caracteres innecesarios para reducir el espacio que usa la impresion del arbol.
	comprimir(arbolConFormato)
	
	#-----------------------------------
	# SALIDA
	#-----------------------------------
	# Mostrar el arbol con el formato requerido
	arbolComoString = imprimirMatriz(arbolConFormato)
	print arbolComoString

	return

main()
