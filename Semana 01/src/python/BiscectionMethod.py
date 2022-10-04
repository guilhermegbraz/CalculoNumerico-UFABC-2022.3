import numpy as np
import pandas as pd


class BiscectionMethod:
    
    def __init__(self, ponto_a : float, ponto_b : float, precisao : float, funcao ) :
        self.ponto_a = ponto_a
        self.ponto_b = ponto_b
        self.precisao = precisao
        self.funcao = funcao
        self.__tabela = None
        self.__relacao = list()
    
    def get_raiz(self) :
        
        raiz_encontrada = False

        while(not raiz_encontrada) :
            
            x = np.array([self.ponto_a, self.ponto_b]).mean()
            erro_relativo = (abs(x - self.ponto_a)/np.array([1, x]).max())
            
            linha = (self.ponto_a, self.ponto_b, self.funcao(self.ponto_a), self.funcao(self.ponto_b), x, self.funcao(x), erro_relativo)
            self.__relacao.append(linha)
            
            if( erro_relativo < self.precisao) :
                raiz = x
                raiz_encontrada = True
            else:
                if self.funcao(self.ponto_a) * self.funcao(x) < 0:
                    self.ponto_b = x
                else:
                    self.ponto_a = x
        return raiz
    
    @property
    def tabela(self):
        self.__tabela = pd.DataFrame(self.__relacao, columns=["a", "b", "f(a)", "f(b)","X_k", "f(X_k)", "Erro relativo"])
        return self.__tabela
