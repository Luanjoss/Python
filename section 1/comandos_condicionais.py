"""
COMANDOS CONDICIONAIS

IF => "SE",Trabalha com condiçoes booleanas.

Sixtaxe

if condição:
    execute_esta_linha

"""

x = 1
y = 154

if x > y:
    print("x é maior que y")

if y > x:
    print("y é maior que x")

"""
COMANDOS CONDICIONAIS

else => Ele é executado quando o comando if não é verdadeiro.

Sixtaxe

if condição:
    execute_esta_linha
    caso contrário
else:
    execute_esta_linha
    
"""
print("----------------------------------------------------------------------------")
x = 1
y = 2

if x == y:
    print("numeros iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("numeros iguais")
else:
    print("x não é maior que y")