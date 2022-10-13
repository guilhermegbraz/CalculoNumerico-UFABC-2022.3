from RegulaFalsi import RegulaFalsi
from NewtonMethod import NewtonMethod
import math

def func (x : float) :
    return pow(x, 2) - 7

def func2a(x : float) :
    return x - math.sqrt(2)

def dfunc2a(x : float) :
    return 1

def func2b(x : float) :
    return x - math.pow(10, 1/3)

def func2c(x : float) :
    return x - math.pow(5, 1/5)

def func2d(x : float) :
    return math.pow(x, 4) + x - 3 

def dfunc2d(x : float) :
    return 4 * math.pow(x, 3) + 1 


    
def main():
    prob1 = RegulaFalsi(0.01, func, 2.4, 2.8)
    result = prob1.get_raiz()
    print("\nA raiz aproximada eh: {}\n\n".format(result),prob1.get_tabela())
    
    prob2a = NewtonMethod(0.01, func2a, dfunc2a, 0.6)
    result2a = prob2a.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2a), prob2a.get_tabela())
    
    prob2b = NewtonMethod(0.01, func2b, dfunc2a, 2.5)
    result2b = prob2b.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2b), prob2b.get_tabela())
    
    prob2c = NewtonMethod(0.01, func2c, dfunc2a, 1.0)
    result2c = prob2c.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2c), prob2c.get_tabela())
    
    prob2d = NewtonMethod(0.01, func2d, dfunc2d, 1.0)
    result2d = prob2d.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2d), prob2d.get_tabela())
    
    prob2d.xi = -1
    prob2d.limpar_resultados()
    result2d = prob2d.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2d), prob2d.get_tabela())
    
    
main()