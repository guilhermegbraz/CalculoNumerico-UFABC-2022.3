import pandas as pd

class Methods:
    
    
    def __init__(self, precisao : float, funcao ) -> None:
        self.precisao = precisao
        self.funcao = funcao
        self.__tabela = None
        self.relacao = list()
    
    
    def get_tabela(self, cabecalho : list):
        self.__tabela = pd.DataFrame(self.relacao, columns=cabecalho)
        return self.__tabela