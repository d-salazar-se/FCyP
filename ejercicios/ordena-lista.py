'''

'''

lista = [50,4,7,23,321,48,6]

print("Lista sin ordenar: " + str(lista))

# OPCION 1
# Consiste en tomar el menor elemento de la lista,
# removerlo, y agregarlo al final de una lista nueva.
# Finalmente, la lista original quedara vacia y la segunda
# lista quedara con los elementos ordenados.

copiaListaOriginal = lista.copy()		# tambien es valido usar la notacion de puntos "lista[:]"
listaOrdenada1 = []

while len(copiaListaOriginal) > 0:

	# seleccionar al primero como el menor de la lista
	i = 0
	menor = copiaListaOriginal[0]
	while i < len(copiaListaOriginal):
		# reemplazar a medida que se encuentre uno menor
		if menor > copiaListaOriginal[i]:
			menor = copiaListaOriginal[i]

		i += 1

	listaOrdenada1.append(menor)
	copiaListaOriginal.remove(menor)

print("[1]Lista ordenada: " + str(listaOrdenada1))

# OPCION 2
# Consiste en invertir si se encuentran dos numeros adyacentes
# en donde uno sea mayor al otro (o menor dependiendo del orden).
# Este algoritmo se conoce como "bubblesort"
copiaListaOriginal = lista.copy()		# tambien es valido usar la notacion de puntos "lista[:]"

i = 0
while i < len(copiaListaOriginal):
	j = 0
	while j < len(copiaListaOriginal) - 1:
		# Se invierte si los numeros adyacentes NO estan ordenados
		if copiaListaOriginal[j] > copiaListaOriginal[j+1]:
			temporal = copiaListaOriginal[j+1]
			copiaListaOriginal[j+1] = copiaListaOriginal[j]
			copiaListaOriginal[j] = temporal
		j += 1
	i += 1

print("[2]Lista ordenada: " + str(copiaListaOriginal))
