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
    print("A raiz encontrada  eh: {}\n".format(problemaA.get_raiz()))
    print(problemaA.get_tabela())
    
    print("\n---------- 4.(b).I---------- \n")
    problemaB = BiscectionMethod(-1, 0, 0.01, funcao_b)
    print("A raiz encontrada  eh: {}\n".format(problemaB.get_raiz()))
    print(problemaB.get_tabela())
    
    print("\n---------- 4.(b).II---------- \n")
    problemaB2 = BiscectionMethod(0, 1, 0.01, funcao_b)
    print("A raiz encontrada  eh: {}\n".format(problemaB2.get_raiz()))
    print(problemaB.get_tabela())
    
    print("\n---------- 4.(c)---------- \n")
    problemaC = BiscectionMethod(0.5, 1, 0.01, funcao_c)
    print("A raiz encontrada  eh: {}\n".format(problemaC.get_raiz()))
    print(problemaC.get_tabela())
    
    print("\n---------- 4.(d)---------- \n")
    problemaD = BiscectionMethod(0.5, 1, 0.01, funcao_d)
    print("A raiz encontrada  eh: {}\n".format(problemaD.get_raiz()))
    print(problemaD.get_tabela())
    

main()
    