'''
Ejercicio clase 7: 27/04/2019
Dada una lista de numeros, retorne sus cuadrados separados por una coma y un espacio

"1 2 3 4" => "1, 4, 9, 16"
'''

# ENTRADA
entrada = input("Ingrese lista de numeros: ")	# entrada = "1 2 3 4"

# PROCESAMIENTO
listaNumeros = entrada.split(" ");				# listaNumeros = ["1", "2", "3", "4"]
listaCuadrados = []

i = 0

while i < len(listaNumeros):
	# se realiza la conversion a entero con int() para calcular
	# el cuadrado del numero
	# sea la tercera iteracion i = 2, listaNumeros[2] = "3",
	# cuadrado = int("3") ** 2 => 9
	cuadrado = int(listaNumeros[i]) ** 2

	# puesto que join trabaja con strings,
	# es necesario hacer la conversion con str() 
	# a string nuevamente y luego agregar a la lista.
	# siguiendo el mismo ejemplo con i = 2,
	# listaCuadrados = ["1", "4", "9"]
	listaCuadrados.append(str(cuadrado))

	i = i + 1

# finalmente se unen todos los cuadrados 
# con el par de caracteres ", " como se pide
# en el enunciado
# final = "1, 4, 9, 16"
final = ", ".join(listaCuadrados)

# SALIDA
print(final)