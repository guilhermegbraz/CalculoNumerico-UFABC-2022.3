import numpy as np
import math as mt

def funcao_problema(x):
    return pow(x, 2) + mt.log(x)

def main():
    ponto_inicio = 0.5
    ponto_final = 1
    raiz_encontrada = False
    precisao = 0.01
    
    while (not raiz_encontrada) :
        x = np.array([ponto_inicio, ponto_final]).mean()
        if((abs(x - ponto_inicio)/np.array([1, x]).max()) < precisao) :
            raiz = x
            contraiz_encontrada = False
        elif funcao_problema(ponto_inicio) * funcao_problema(x) < 0:
            ponto_final = x
        else:
            ponto_inicio = x
    
    return raiz

print(main())