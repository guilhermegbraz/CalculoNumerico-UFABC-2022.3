import numpy as np
from Methods import Methods

class SecantesMethod(Methods) :
    def __init__(self,precisao : float, funcao, x0 : float, x1 : float) -> None:
            super().__init__( precisao, funcao)
            self.x0 = x0
            self.x1 = x1
            
    def get_raiz(self):
        parar = False
        while(not parar):
            xk = (self.x0 * self.funcao(self.x1) - self.x1 * self.funcao(self.x0))/(self.funcao(self.x1) - self.funcao(self.x0))
            
            incerteza1 = abs((xk - self.x1)/np.array([1, xk]).max())
            incerteza0 = abs((xk - self.x0)/np.array([1, xk]).max())
            
            erro_relativo = np.array([incerteza0, incerteza1]).min()
            linha = (self.x0, self.x1, self.funcao(self.x0), self.funcao(self.x1), xk, self.funcao(xk), erro_relativo)
            self.relacao.append(linha)
            
            if(incerteza1 < self.precisao or incerteza0 < self.precisao):
                parar = True
                raiz = xk
            else:
                self.atualiza_chutes(xk)
                
        return raiz

    def atualiza_chutes(self, xk : float):
        self.x0 = self.x1
        self.x1 = xk
    
    def get_tabela(self):
        cabecalho = ["x_k-1", "x_k", "f(x_k-1)", "f(x_k)", "x_k+1", "f(x_k+1)", "Erro relativo"]
        return super().get_tabela(cabecalho)