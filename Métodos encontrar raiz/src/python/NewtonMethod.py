import numpy as np
from Methods import Methods

class NewtonMethod (Methods):
    
    def __init__(self,  precisao: float, funcao, derivadaf, chute_inicial : float) -> None:
        super().__init__(precisao, funcao)
        self.derivadaf = derivadaf
        self.xi = chute_inicial
    
    def get_raiz(self):
        raiz_encontrada = False
        
        while(not raiz_encontrada):
            xj = self.xi - (self.funcao(self.xi)/self.derivadaf(self.xi))
            erro_relativo = abs((xj - self.xi)/np.array([1, xj]).max())
            
            linha = (self.xi, self.funcao(self.xi), self.derivadaf(self.xi), xj, erro_relativo)
            self.relacao.append(linha)
            
            if(erro_relativo < self.precisao):
                raiz = xj
                raiz_encontrada = True
            else:
                self.xi = xj
                
        return raiz
    
    def get_tabela(self):
        cabecalho = ["x_k","f(x_k)", "f'(x_k)","x_k+1", "Erro relativo"]
        return super().get_tabela(cabecalho)
    
    