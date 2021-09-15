"""
OPERADORES LÓGIOCOS 
and => Duas condições sejam verdadeiras
or => Pelo menos uma condição seja verdadeira
not => inverter o valor

"""

x = 2
y = 2

soma = x + y

print(x == y and x != soma)

x = 3
y = 3
z = 4

print(x == y or x == z and z == y)