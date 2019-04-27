'''
Ejercicio clase 6: 26/04/2019
Dado un numero entero 189 devolver el numero invertido 981
'''

# Para efectos del ejemplo, consideremos la entrada como 
# el numero entero 123, luego:
# numeroOriginal = 123
numeroOriginal = int(input("Ingrese numero: "))
numeroInvertido = 0

# Vamos a iterar (hacer el ciclo while) 
#
while numeroOriginal > 0:
	# resto correspondera siempre al ultimo digito del numero
	resto = numeroOriginal % 10

	numeroInvertido = (numeroInvertido * 10) + resto
	numeroOriginal = numeroOriginal // 10

print(numeroInvertido)

