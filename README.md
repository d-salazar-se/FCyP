# Manual de usuario

Programa que dibuja en la pantalla un árbol binario ordenado basado en una cadena de caracteres ingresada por el usuario.

  El programa se ejecuta como cualquier código python, es decir en computador con Python 2.7 instalado ya sea Linux o Windows a tráves de la terminal con la instrucción:

> python 1-G-2_Grupo_2.py
  
  Se debe comprobar que se esta trabajando en el mismo directorio donde se encuentra el código.
  El programa no requiere la instalación de ningún módulo extra para funcionar.

  Además en Windows se puede hacer uso del IDLE (Integrated Development Environment) para Python, en cuyo caso basta con abrir el archivo con el editor y seleccionar la opción de correr el código (tecla F5).

  Una vez iniciado programa se pedirá que se ingrese una cadena de caracteres, ésta debe cumplir con las siguientes reglas:
 - No deben existir espacios (éstos se eliminarán)
 - No se permiten mayúsculas (éstas seran transformadas a minúsculas)
 - No se permiten letras repetidas (tras la primera aparición de izquierda a derecha se eliminará el resto)
 - No se permiten letras que no existan en el alfabeto inglés (tales como ñ o ç, éstas se eliminarán)
 - No se permiten letras con tilde (éstas se eliminarán)

  Una vez ingresada la cadena de caracteres y presionada la tecla Enter se aplicarán las reglas recién mencionadas, si la cadena resultante posee al menos una letra se procederá a crear un árbol binario ordenado, en caso contrario se mostrará un mensaje mostrando el error. Tras ambos casos se procede a terminar la ejecución del programa.
