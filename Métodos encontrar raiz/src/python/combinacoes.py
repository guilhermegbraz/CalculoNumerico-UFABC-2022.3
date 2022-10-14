import pandas as pd

def combinacao3() :
    relacao = list()
    for d1 in range(1,3):
        for d2 in range (0,3):
            for d3 in range (0, 3):
                for pot in range (-2, 2, 1):
                    resultado = (d1* pow(3, -1) + d2 * pow(3, -2) + d3 * pow(3, -3)) * pow(3,pot)
                    linha = ("Combinação 0.{}{}{} x 3^{}".format(d1, d2, d3, pot) , resultado);
                    relacao.append(linha)
    return relacao

def main():
    
    tabela = pd.DataFrame(combinacao3(), columns=["Mantissa base 3" , "Decimal"])
    print(tabela)
    
    return 1

main()