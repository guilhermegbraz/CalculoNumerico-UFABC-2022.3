import numpy as np


class BiscectionMethod:
    
    def __init__(self, ponto_a : float, ponto_b : float, precisao : float, funcao: function, maxima_iteracao = None ) :
        self.ponto_a = ponto_a
        self.ponto_b = ponto_b
        self.precisao = precisao
        self.funcao = funcao
        self.__tabela = None
    
    def get_raiz(self) :
        
        raiz_encontrada = False
        contador = 0
        
        
        while(not raiz_encontrada) :
             x = np.array([self.ponto_a, self.ponto_b]).mean()
             if((abs(x - self.ponto_a)/np.array([1, x]).max()) < self.precisao) :
                print("encontrei a raiz depois de {} iterações".format(contador))
                raiz = x
                raiz_encontrada = True
        else:
            if self.funcao(self.ponto_a) * self.funcao(x) < 0:
                print("atualizei o A" )
                self.ponto_b = x
            else:
                print("atualizei o B" )
                self.ponto_a = x
        contador += 1
        return raiz