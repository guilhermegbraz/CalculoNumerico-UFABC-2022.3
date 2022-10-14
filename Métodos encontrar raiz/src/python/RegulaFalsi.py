import numpy as np
from SecantesMethod import SecantesMethod

class RegulaFalsi(SecantesMethod):
    
    def __init__(self,precisao : float, funcao, x0 : float, x1 : float) -> None:
        super().__init__( precisao, funcao, x0,x1)
        
        if(self.funcao(x1) * self.funcao(x0) > 0):
            raise Exception("Escolha os chutes iniciais (x0 e x1) de tal modo que f(x0) * f(x1) < 0")
    

    def get_raiz(self):
        
        return super().get_raiz()
    
    def atualiza_chutes(self, xk : float):
        if(self.funcao(xk) * self.funcao(self.x0) < 0) :
            self.x1 = xk
        else:
            self.x0 = xk
    
    
        