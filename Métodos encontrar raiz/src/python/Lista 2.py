
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
    ##prob1()
    ##prob2()
    
    prob3RF = RegulaFalsi(0.01, func3, -1.20, -0.85)
    result3RF = prob3RF.get_raiz()
    print("\nA 1º raiz aproximada calculada com o método de Regula Falsi eh {}\n\n".format(result3RF), prob3RF.get_tabela())
    
    prob3RF.x0 = -0.7
    prob3RF.x1 = -0.6
    prob3RF.limpar_resultados()
    result3RF = prob3RF.get_raiz()
    print("\nA 2º raiz aproximada calculada com o método de Regula Falsi eh {}\n\n".format(result3RF), prob3RF.get_tabela())
    
    prob3RF.x0 = 1.5
    prob3RF.x1 = 1.7
    prob3RF.limpar_resultados()
    result3RF = prob3RF.get_raiz()
    print("\nA 3º raiz aproximada calculada com o método de Regula Falsi eh {}\n\n".format(result3RF), prob3RF.get_tabela())
    
    ##prob3_secantes()
    
    return 0

def prob1():
    prob1 = RegulaFalsi(0.01, func, 2.4, 2.8)
    result = prob1.get_raiz()
    print("\nA raiz aproximada para o exercicio 1 eh: {}\n\n".format(result),prob1.get_tabela())

def prob2():
    prob2a = NewtonMethod(0.01, func2a, dfunc2a, 1.0)
    result2a = prob2a.get_raiz()
    print("\nA raiz aproximada para o exercicio 2.a eh {}\n\n".format(result2a), prob2a.get_tabela())
    
    prob2b = NewtonMethod(0.01, func2b, dfunc2b, 2.5)
    result2b = prob2b.get_raiz()
    print("\nA raiz aproximada para o exercicio 2.b eh {}\n\n".format(result2b), prob2b.get_tabela())
    
    prob2c = NewtonMethod(0.01, func2c, dfunc2c, 1.0)
    result2c = prob2c.get_raiz()
    print("\nA raiz aproximada para o exercicio 2.c eh {}\n\n".format(result2c), prob2c.get_tabela())
    
    prob2d = NewtonMethod(0.01, func2d, dfunc2d, 1.0)
    result2d = prob2d.get_raiz()
    print("\nA raiz aproximada para o exercicio 2.d (x0 = -1) eh {}\n\n".format(result2d), prob2d.get_tabela())
    
    prob2d.xi = -1
    prob2d.limpar_resultados()
    result2d = prob2d.get_raiz()
    print("\nA raiz aproximada para o exercicio 2.d (x0 = 1) eh {}\n\n".format(result2d), prob2d.get_tabela())

def prob3_secantes():
    prob3Sec = SecantesMethod(0.01, func3, -1.32, -1.21)
    result3Sec = prob3Sec.get_raiz()
    print("\nA 1° raiz aproximada calculada com o método das secantes eh {}\n\n".format(result3Sec), prob3Sec.get_tabela())

    prob3Sec.x0 = -0.8
    prob3Sec.x1 = -0.7
    prob3Sec.limpar_resultados()
    result3Sec = prob3Sec.get_raiz()
    print("\nA 2° raiz aproximada calculada com o método das secantes eh {}\n\n".format(result3Sec), prob3Sec.get_tabela())
    
    prob3Sec.x0 = 1.45
    prob3Sec.x1 = 1.51
    prob3Sec.limpar_resultados()
    result3Sec = prob3Sec.get_raiz()
    print("\nA 3° raiz aproximada calculada com o método das secantes eh {}\n\n".format(result3Sec), prob3Sec.get_tabela())

    return 1
    
    
main()