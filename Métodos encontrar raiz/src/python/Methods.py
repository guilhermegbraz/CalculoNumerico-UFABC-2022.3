import pandas as pd

class Methods:
    def __init__(self, precisao : float, funcao ) -> None:
        self.precisao = precisao
        self.funcao = funcao
        self._tabela = None
        self.relacao = list()
    
    def get_tabela(self, cabecalho : list):
        self._tabela = pd.DataFrame(self.relacao, columns=cabecalho)
        return self._tabela
    
    def limpar_resultados(self) :
        self.relacao = list()
        self._tabela = None