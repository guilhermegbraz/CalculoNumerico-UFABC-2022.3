from RegulaFalsi import RegulaFalsi
import math

def func (x : float) :
    return pow(x, 2) - 7

def main():
    prob1 = RegulaFalsi(2, 3, 0.01, func, 2.4, 2.8)
    result = prob1.get_raiz()
    print("A raiz aproximada eh: {}\n".format(result),prob1.tabela)

main()