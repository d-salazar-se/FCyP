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
import math

# Definicion de la clase "Nodo", que seran los elementos del arbol
class Nodo:
	# Atributos
	hijoIzq = None
	hijoDer = None
	caracter = ''

	# Constructor
	def __init__(self, caracter = ''):
		self.caracter = caracter

	# Metodo que inserta un nodo dentro del arbol binario
	# 	Si es mayor se ingresa a la derecha, en caso contrario a la izquierda
	# Entrada: Objecto clase nodo
	# Salida: None
	def insertarNodo(self, nodo):
		if nodo.caracter < self.caracter:
			if self.hijoIzq is None:
				self.hijoIzq = nodo
			else:
				self.hijoIzq.insertarNodo(nodo)
		else:
			if self.hijoDer is None:
				self.hijoDer = nodo
			else:
				self.hijoDer.insertarNodo(nodo)

		return None
	
	# Metodo que genera una matriz con los nodos por nivel.
	# Entrada:
	# 		niveles -> lista con los niveles del arbol
	# 		prof 	-> profundidad actual del arbol (raiz = 0)
	# Salida: None
	def generarFormatoImpresion(self, niveles, prof = 0):
		# agregar el caracter a la lista con el nivel correspondiente
		niveles[prof].append(self.caracter)

		if self.hijoIzq is not None:
			self.hijoIzq.generarFormatoImpresion(niveles, prof+1)
		elif prof < len(niveles) - 1:
			# agregar tantos "nodo" vacios como potenciales hijos tenga el nodo
			i = prof + 1
			while i < len(niveles):
				for x in range(0, 2**(i - prof-1)):
					niveles[i].append(None)
				i += 1
			
		if self.hijoDer is not None:
			self.hijoDer.generarFormatoImpresion(niveles, prof+1)
		elif prof < len(niveles) - 1:
			# agregar tantos "nodo" vacios como potenciales hijos tenga el nodo
			i = prof + 1
			while i < len(niveles):
				for x in range(0, 2**(i - prof-1)):
					niveles[i].append(None)
				i += 1
			
		return None

	def imprimir(self, niveles):
		ancho = 6*(2**(len(niveles)-1))

		vistaImpresion = []
		
		#print '|'.center(ancho)
		for nivel in niveles:
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
				ramaDer = '-'*(int(math.ceil(float(ancho)/4))-1)
				ramaIzq = '-'*(int(math.ceil(float(ancho)/4))-1)

				c = '+' + ramaIzq + c + ramaDer + '+'
				r = '|' + (' '*(2*len(ramaIzq)+1)) + '|'
				
				# Centrar estas ramas en la fraccion de espacio 
				# que le corresponde
				linea += c.center(ancho)
				ramas += r.center(ancho)

			# Agregar a la matriz que guarda el formato de impresion
			vistaImpresion.append(list(linea))
			vistaImpresion.append(list(ramas))

			#print linea
			#print ramas
			ancho /= 2

		columnasARemover = []
		for col in range(len(vistaImpresion)):
			columna = [row[col] for row in vistaImpresion]

			if columna[1:] == columna[:-1]:
				columnasARemover.append(col)

		columnasARemover.sort(reverse=True)

		for indice in columnasARemover:
			for fila in vistaImpresion:
				del fila[indice]

		print('\n'.join([''.join(['{}'.format(item)for item in row])for row in vistaImpresion]))

		return None

	# Funcion que establece la profundidad del arbol binario
	# Entrada: un objeto arbol
	# Salida: Profundidad del arbol (numero de niveles)
	def obtenerProfundidad(self):
		# Llegamos a una hoja
		if self is None:
			return 0
		# No es hoja, continuar hacia abajo
		profIzq = 0
		profDer = 0
		if self.hijoIzq is not None:
			profIzq = self.hijoIzq.obtenerProfundidad()

		if self.hijoDer is not None:
			profDer = self.hijoDer.obtenerProfundidad()
		
		if profIzq > profDer:
			return profIzq + 1
		return profDer + 1

# FUNCIONES
def validarCadena(cadena):
	listado = []
	CARACTERES_VALIDOS = 'abcdefghijklmnopqrstuvwxyz'

	for caracter in cadena:
		if caracter in CARACTERES_VALIDOS and not caracter in listado:
			listado.append(caracter)
	return listado


# Funcion en donde se produce el codigo principal
# Entrada: None
# Salida: Un entero (0 si termina correctamente)
def main():
	#-----------------------------------
	# ENTRADA
	#-----------------------------------

	#cadena = raw_input("Ingrese texto: ").lower())
	
	#cadena = 'kxqethn'

	#cadena = 'zmawpscgi'
	#cadena = 'abcd'
	cadena = 'dabkms'
	#cadena = 'cbadmohkpwsz'

	#-----------------------------------
	# PROCESAMIENTO
	#-----------------------------------

	# Crear una Cadena valida de texto
	# Eliminar caracteres invalidos y repetidos
	cadena = validarCadena(cadena)

	# Declarar el inicio del arbol
	arbol = Nodo(cadena.pop(0))

	# insertar en el arbol item a item
	# segun orden de ingreso
	while len(cadena) > 0:
		n = Nodo(cadena.pop(0))
		arbol.insertarNodo(n)

	#-----------------------------------
	# SALIDA
	#-----------------------------------
	
	# Mostrar el arbol con el formato requerido
	n = [[] for i in range(arbol.obtenerProfundidad())]
	arbol.generarFormatoImpresion(n)

	arbol.imprimir(n)

	return 0

# Ejecución del codigo principal
if __name__ == "__main__":
	main()
