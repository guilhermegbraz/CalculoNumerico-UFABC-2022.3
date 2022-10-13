class RaizMethods:
    
    def __init__(self, ponto_a : float, ponto_b : float, precisao : float, funcao ) :
        self.ponto_a = ponto_a
        self.ponto_b = ponto_b
        self.precisao = precisao
        self.funcao = funcao
        self.__tabela = None
        self.__relacao = list()