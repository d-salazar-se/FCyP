"""
Segmento de codigo robado desde
http://code.activestate.com/recipes/81611-roman-numerals/
Todos los creditos a ese men.
"""
def convertirARomano(x):
  arabico = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
  romano  = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']

  xEnRomano = ""
  for i in range(len(arabico)):
    contador = int(x/arabico[i])
    xEnRomano += romano[i] * contador
    x -= arabico[i] * contador

  return xEnRomano
