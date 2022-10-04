from pip import main
from BiscectionMethod import BiscectionMethod

import math 

### 4.(a)
def funcao_a(x : float):
    return pow(x,2) - math.sin(x)

### 4.(b)
def funcao_b(x : float):
    return math.cos(math.pi*(x+1)/8) + 0.148 * x -0.9062

### 4.(c)
def funcao_c(x : float):
    return pow(x, 2) + math.log(x)

### 4.(d)
def funcao_d(x : float):
    return x * math.pow(math.e, x) - 1



def main():
    print("---------- 4.(a)---------- \n")
    problemaA = BiscectionMethod(0.5, 1, 0.01, funcao_a)
    print("Raiz a partir do objeto eh: {}".format(problemaA.get_raiz()))
    print(problemaA.tabela)
    
    print("\n---------- 4.(b).I---------- \n")
    problemaB = BiscectionMethod(-1, 0, 0.01, funcao_b)
    print("Raiz a partir do objeto eh: {}".format(problemaB.get_raiz()))
    print(problemaB.tabela)
    
    print("\n---------- 4.(b).II---------- \n")
    problemaB2 = BiscectionMethod(0, 1, 0.01, funcao_b)
    print("Raiz a partir do objeto eh: {}".format(problemaB2.get_raiz()))
    print(problemaB.tabela)
    
    print("\n---------- 4.(c)---------- \n")
    problemaC = BiscectionMethod(0.5, 1, 0.01, funcao_c)
    print("Raiz a partir do objeto eh: {}".format(problemaC.get_raiz()))
    print(problemaC.tabela)
    
    print("\n---------- 4.(d)---------- \n")
    problemaD = BiscectionMethod(0.5, 1, 0.01, funcao_d)
    print("Raiz a partir do objeto eh: {}".format(problemaD.get_raiz()))
    print(problemaD.tabela)
    

main()
    