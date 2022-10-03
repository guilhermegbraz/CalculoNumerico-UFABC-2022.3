from pip import main
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

### 6.(d)
def funcao_d(x : float):
    return x * math.pow(math.e, x) - 1



def main():
    print("---------- 6.(a)---------- \n")
    problemaA = BiscectionMethod(0.5, 1, 0.01, funcao_a)
    print("Raiz a partir do objeto eh: {}".format(problemaA.get_raiz()))
    print(problemaA.tabela)
    
    print("\n---------- 6.(b).I---------- \n")
    problemaB = BiscectionMethod(-1, 0, 0.01, funcao_b)
    print("Raiz a partir do objeto eh: {}".format(problemaA.get_raiz()))
    print(problemaB.tabela)
    
    print("\n---------- 6.(b).II---------- \n")
    problemaB.ponto_a = 0
    problemaB.ponto_b = 1
    print("Raiz a partir do objeto eh: {}".format(problemaA.get_raiz()))
    print(problemaB.tabela)
    
    print("\n---------- 6.(c)---------- \n")
    problemaC = BiscectionMethod(0.5, 1, 0.01, funcao_c)
    print("Raiz a partir do objeto eh: {}".format(problemaC.get_raiz()))
    print(problemaC.tabela)
    
    print("\n---------- 6.(d)---------- \n")
    problemaD = BiscectionMethod(0.5, 1, 0.01, funcao_d)
    print("Raiz a partir do objeto eh: {}".format(problemaD.get_raiz()))
    print(problemaD.tabela)
    

main()
    