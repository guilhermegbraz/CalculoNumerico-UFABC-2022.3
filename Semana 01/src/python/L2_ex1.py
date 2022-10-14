from SecantesMethod import SecantesMethod
from RegulaFalsi import RegulaFalsi
from NewtonMethod import NewtonMethod
import math

def func (x : float) :
    return pow(x, 2) - 7

def func2a(x : float) :
    return pow(x,2) - 2

def dfunc2a(x : float) :
    return 2 * x

def func2b(x : float) :
    return pow(x, 3) - 10

def dfunc2b(x : float) :
    return 3 * pow(x, 2)

def func2c(x : float) :
    return math.pow(x,5) - 5

def dfunc2c(x : float) :
    return 5 * pow(x, 4)

def func2d(x : float) :
    return math.pow(x, 4) + x - 3 

def dfunc2d(x : float) :
    return 4 * math.pow(x, 3) + 1 

def func3(x : float) :
    return pow(x, 3) - 2 * x - 1

    
def main():
    prob1 = RegulaFalsi(0.01, func, 2.4, 2.8)
    result = prob1.get_raiz()
    print("\nA raiz aproximada eh: {}\n\n".format(result),prob1.get_tabela())
    
    prob2a = NewtonMethod(0.01, func2a, dfunc2a, 1.0)
    result2a = prob2a.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2a), prob2a.get_tabela())
    
    prob2b = NewtonMethod(0.01, func2b, dfunc2b, 2.5)
    result2b = prob2b.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2b), prob2b.get_tabela())
    
    prob2c = NewtonMethod(0.01, func2c, dfunc2c, 1.0)
    result2c = prob2c.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2c), prob2c.get_tabela())
    
    prob2d = NewtonMethod(0.01, func2d, dfunc2d, 1.0)
    result2d = prob2d.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2d), prob2d.get_tabela())
    
    prob2d.xi = -1
    prob2d.limpar_resultados()
    result2d = prob2d.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result2d), prob2d.get_tabela())
    
    prob3RF = RegulaFalsi(0.01, func3, -1.5, -0.8)
    result3RF = prob3RF.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result3RF), prob3RF.get_tabela())
    
    prob3Sec = SecantesMethod(0.01, func3, -1.5, -1.32)
    result3Sec = prob3Sec.get_raiz()
    print("\nA raiz aproximada eh {}\n\n".format(result3Sec), prob3Sec.get_tabela())
    
    
    
main()