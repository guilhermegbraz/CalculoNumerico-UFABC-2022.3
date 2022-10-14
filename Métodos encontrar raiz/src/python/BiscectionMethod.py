import numpy as np
from Methods import Methods

class BiscectionMethod(Methods):
    
    def __init__(self, ponto_a : float, ponto_b : float, precisao : float, funcao ) -> None:
        super().__init__( precisao , funcao)
        self.ponto_a = ponto_a
        self.ponto_b = ponto_b
    
    def get_raiz(self) :
   
        raiz_encontrada = False

        while(not raiz_encontrada) :
            
            x = np.array([self.ponto_a, self.ponto_b]).mean()
            erro_relativo = (abs((x - self.ponto_a)/np.array([1, x]).max()))
            
            linha = (self.ponto_a, self.ponto_b, self.funcao(self.ponto_a), self.funcao(self.ponto_b), x, self.funcao(x), erro_relativo)
            self.relacao.append(linha)
            
            if( erro_relativo < self.precisao) :
                raiz = x
                raiz_encontrada = True
            else:
                if self.funcao(self.ponto_a) * self.funcao(x) < 0:
                    self.ponto_b = x
                else:
                    self.ponto_a = x
        return raiz
    
    def get_tabela(self):
        cabecalho = ["a", "b", "f(a)", "f(b)","X_k", "f(X_k)", "Erro relativo"]
        return super().get_tabela(cabecalho)
    
    
