import random

"""
Foi utilizado 3 funçoes para esse trabalho.
a 1 função e a extrair matriz:
    para que a função possa funcionar tem que se passar a matriz que deseja que ela faça a extração de colunas e linhas desejadas
    1 parametro e a matriz;
    2 parametro e a linha que deseja cortar
    3 parametro e a coluna que deseja cortar
    4 parametro e a quantidade de linhas que deseja na nova matriz
    5 parametro e a quantidade de coluna que deseja na nova matriz
    obs a quantidade de colunas e linhas não pode ser superior a quantidade de linhas e colunas da matriz pai

2 função ela gera uma matriz
    para que a função função funcione precisa passar alguns parametros que são:
    quantidade de linha
    quantidade de colunas
    valor minimo e maximo que deseja na matriz   

3 função ela exibi a matriz
    essa função ela faz a limpeda da matriz e exibe ela fora do formato de lista e deixa ela indentada
"""

def extraimat(matriz, linha_de_corte, coluna_de_corte, qtd_linhas, qtd_colunas):
    matriz_recort = []
    for k in range(linha_de_corte, qtd_linhas + linha_de_corte):
        linha=[]
        for m in range(coluna_de_corte, qtd_colunas + coluna_de_corte):
            linha.append(matriz[k][m])
        matriz_recort.append(linha)
    return matriz_recort

def geraMatriz(linha, coluna, min, max):
    li_matriz = []
    for i in range(linha):
        col_matriz = []
        for j in range(coluna):
            col_matriz.append(random.randint(min, max))
        li_matriz.append(col_matriz)
    return li_matriz

def exibir_matriz(matriz):
    for linha in matriz:
        print()
        for j in linha:
            print('%5d' % j,end='')






def main():
    resultado = geraMatriz(10, 10, 0, 20)
    corte = extraimat(resultado, 1, 3, 2, 4)
    exibir_matriz(corte)
    print()
    exibir_matriz(resultado)
    


if __name__ == "__main__":
    main()