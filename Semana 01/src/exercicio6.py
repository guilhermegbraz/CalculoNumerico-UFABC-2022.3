from BiscectionMethod import BiscectionMethod

import math 

### 6.(a)
def funcao_a(x : float):
    return pow(x,2) - math.sin(x)

### 6.(b)
def funcao_b(x : float):
    return math.cos(math.pi*(x+1)/8) + 0.148 * x -0.9062

### 6.(c)
def funcao_c(x : float):
    return pow(x, 2) + math.log(x)




teste = BiscectionMethod(0.5, 1, 0.01, funcao_problema)
print("Raiz a partir do objeto eh: {}".format(teste.get_raiz()))
print(teste.tabela)