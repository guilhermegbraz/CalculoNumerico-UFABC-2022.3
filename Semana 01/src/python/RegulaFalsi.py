import numpy as np
import pandas as pd
from Methods import Methods

class RegulaFalsi(Methods):
    
    def __init__(self, ponto_a : float, ponto_b : float, precisao : float, funcao, x0 : float, x1 : float) -> None:
        super().__init__(ponto_a, ponto_b, precisao, funcao)
        self.x0 = x0
        self.x1 = x1
        
        if(self.funcao(x1) * self.funcao(x0) > 0):
            raise Exception("Escolha os chutes iniciais (x0 e x1) de tal modo que f(x0) * f(x1) < 0")
    

    def get_raiz(self):
        parar = False
        while(not parar):
            xk = (self.x0 * self.funcao(self.x1) - self.x1 * self.funcao(self.x0))/(self.funcao(self.x1) - self.funcao(self.x0))
            incerteza1 = abs((xk - self.x1)/np.array([1, xk]).max())
            incerteza0 = abs((xk - self.x0)/np.array([1, xk]).max())
            
            linha = (self.x0, self.x1, self.funcao(self.ponto_a), self.funcao(self.ponto_b), xk, self.funcao(xk), incerteza0)
            self.relacao.append(linha)
            
            if(incerteza1 < self.precisao or incerteza0 < self.precisao):
                parar = True
                raiz = xk
            else:
                if(self.funcao(xk) * self.funcao(self.x0) < 0) :
                    self.x1 = xk
                else:
                    self.x0 = xk
        return raiz
        