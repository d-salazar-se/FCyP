#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#
# Autoría: [Grupo 2] 10110-G-2
# Fecha: Segundo Semestre 2016
#
# Objectivo: Dibujar un arbol binario con letras
# Categoria: Ingenieria Informatica
# Descripcion: Dibujar un árbol binario con las letras de una secuencia 
# 		de caracteres ingresadas desde teclado.
#

# IMPORTACION DE LIBRERIAS
from math import ceil

# FUNCIONES

# Funcion que genera una cadena valida para el arbol:
# 	sin caracteres repetidos y pertenecientes al alfabeto ingles.
# Entrada: str cadena, Cadena de caracteres en base a la cual se genera una cadena "valida"
# Salida: list listado, Lista con los caracteres que cumplen las dos reglas mencionadas anteriormente.
def generarCadenaValida(cadena):
	listado = []
	CARACTERES_VALIDOS = 'abcdefghijklmnopqrstuvwxyz'

	for caracter in cadena:
		if caracter in CARACTERES_VALIDOS and not caracter in listado:
			listado.append(caracter)
	return listado


# Funcion que inserta un "nodo" en el arbol ya estructurado.
# Entrada:
#			- list padre, Lista que representa al nodo raiz del arbol.
#			- str caracter, Caracter nuevo a ingresar, este no puede existir en el arbol.
# Salida: None
def insertar(padre, caracter):
	
	while padre is not None:
		if caracter < padre[1]:
			if padre[0] is None:
				padre[0] = [None, caracter, None]
				return
			else:
				padre = padre[0]
		else:
			if padre[2] is None:
				padre[2] = [None, caracter, None]
				return
			else:
				padre = padre[2]

# Funcion que retorna la profundidad del arbol.
# Entrada: list raiz, Lista de listas que representan al arbol.
# Salida: integer, contador con el numero de niveles del arbol.
def obtenerProfundidad(raiz):
	nivelActual = [raiz]
	contador = 0
	while nivelActual:
		siguienteNivel = []
		for n in nivelActual:			
			if n[0]: siguienteNivel.append(n[0])
			if n[2]: siguienteNivel.append(n[2])
		nivelActual = siguienteNivel
		contador += 1

	return contador

# Funcion que recorre y retorna el arbol por niveles desde la raiz hacia las hojas.
# Entrada:
# 			- arbol list, Lista de listas con los arboles por nivel.
# 			- numeroNiveles integer, Entero que representa la profundidad del arbol.
# Salida: list, Lista de listas con los nodos guardados en listas segun su nivel.
def obtenerNiveles(arbol, numeroNiveles):
	nivelActual = [arbol]
	
	niveles = [[] for x in range(numeroNiveles)]
	profundidad = 0
	
	while nivelActual:
		siguienteNivel = []

		for n in nivelActual:
			if n is None:
				if profundidad < numeroNiveles:
					niveles[profundidad+1].append(None)
					niveles[profundidad+1].append(None)
				continue
			
			
			niveles[profundidad].append(n[1])

			if n[0]:
				siguienteNivel.append(n[0])
			else:
				siguienteNivel.append([None,None,None])
			
			if n[2]:
				siguienteNivel.append(n[2])
			else:
				siguienteNivel.append([None,None,None])
		
		profundidad += 1
		
		if profundidad == numeroNiveles:
			return niveles

		nivelActual = siguienteNivel
		
	return niveles

# Funcion que agrega las "ramas" y espacios necesarios para generar la estructura del arbol.
# Entrada: arbol list, Lista con los nodos guardados por nivel en otra lista.
# Salida: list, Lista de listas con los nodos guardados con sus respectivas ramas por nivel.
def generarMatrizImpresion(arbol):

	ancho 			= 6*(2**(len(arbol)-1))
	vistaImpresion 	= []

	vistaImpresion.append(list('|'.center(ancho)))

	for nivel in arbol:
		linea = ''
		ramas = ''
		for c in nivel:
			# Imprimir espacio pertinente pero "vacio"
			if c is None:
				linea += ' '*ancho
				ramas += ' '*ancho
				continue
			
			# Ingresar "ramas" a la izquierda y derecha 
			# del nodo con signos "-" y "+"
			rama = '-'*(int(ceil(ancho/4.0))-1)

			c = '+' + rama + c + rama + '+'
			r = '|' + (' '*(2*len(rama)+1)) + '|'
			
			# Centrar estas ramas en la fraccion de espacio 
			# que le corresponde
			linea += c.center(ancho)
			ramas += r.center(ancho)

		# Agregar a la matriz que guarda el formato de impresion
		vistaImpresion.append(list(linea))
		vistaImpresion.append(list(ramas))

		ancho /= 2

	return vistaImpresion

# Funcion que remueve los espacios "innecesarios" en la estructura del arbol (matriz).
# Entrada: matrizImpresion list, Lista de lista con los caracteres guardados por fila.
# Salida: None.
def comprimir(matrizImpresion):
	# Contar columnas desde atras hacia adelante
	for indiceColumna in range(len(matrizImpresion[0])-1, -1, -1):
		columna = [fila[indiceColumna] for fila in matrizImpresion]
		
		remover = True

		for fila in range(len(columna)):
			if columna[fila] == '-' and matrizImpresion[fila][indiceColumna+1] != '-':
				remover = False

			if columna[fila] not in [' ', '-']:
				remover = False

		if remover:
			for fila in matrizImpresion:
				del fila[indiceColumna]


# Funcion en donde se produce el codigo principal.
# Entrada: None.
# Salida: Un booleano que define sise termino correctamente la ejecucion del programa.
def main():
	#-----------------------------------
	# ENTRADA
	#-----------------------------------
	cadena = raw_input("Ingrese cadena: ").lower()

	# Crear una Cadena valida de texto, 
	# eliminar caracteres invalidos y repetidos
	cadena = generarCadenaValida(cadena)

	if len(cadena) < 1:
		print "[ ! ] Debes ingresar al menos una letra."
		return False

	#-----------------------------------
	# PROCESAMIENTO
	#-----------------------------------
	# Declarar el inicio del arbol
	# Hijo Izquierdo = None, Hijo Derecho = None
	arbol = [None, cadena.pop(0), None]

	# insertar en el arbol item a item
	# segun orden de ingreso
	while len(cadena) > 0:
		caracter = cadena.pop(0)
		insertar(arbol, caracter)

	profundidad = obtenerProfundidad(arbol)
	arbol 		= obtenerNiveles(arbol, profundidad)
	arbol 		= generarMatrizImpresion(arbol)
	
	comprimir(arbol)
	#-----------------------------------
	# SALIDA
	#-----------------------------------
	# Mostrar el arbol con el formato requerido
	print
	print "\n".join(["".join(["{}".format(item)for item in fila])for fila in arbol])

	return True

main()