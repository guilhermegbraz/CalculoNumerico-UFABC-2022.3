from RegulaFalsi import RegulaFalsi
from NewtonMethod import NewtonMethod
import math

def func (x : float) :
    return pow(x, 2) - 7

def func2(x : float) :
    return x - math.sqrt(2)

def dfunc2(x : float) :
    return 1

def main():
    prob1 = RegulaFalsi(0.01, func, 2.4, 2.8)
    result = prob1.get_raiz()
    print("\nA raiz aproximada eh: {}\n\n".format(result),prob1.get_tabela())
    
    prob2 = NewtonMethod(0.01, func2, dfunc2, 0.6)
    result2 = prob2.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2), prob2.get_tabela())

main()