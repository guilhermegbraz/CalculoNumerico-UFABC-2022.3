import pandas as pd

class Methods:
    
    
    def __init__(self, ponto_a : float, ponto_b : float, precisao : float, funcao ) -> None:
        self.ponto_a = ponto_a
        self.ponto_b = ponto_b
        self.precisao = precisao
        self.funcao = funcao
        self.__tabela = None
        self.relacao = list()
    
    @property
    def tabela(self):
        self.__tabela = pd.DataFrame(self.relacao, columns=["a", "b", "f(a)", "f(b)","X_k", "f(X_k)", "Erro relativo"])
        return self.__tabela