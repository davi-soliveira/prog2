import random
def extraimat(m,l,c,q_linha,q_coluna):
    matriz_sub=[]
    matriz_recorte=[]
    for i in range(l,q_linha+l):
        linha=[]
        for j in range(c,q_coluna+c):
            linha.append(m[i][j])
        matriz_recorte.append(linha)
    return matriz_recorte

def geramatriz(linha,coluna,minimo,maximo):
    li_matriz=[]
    valores=int()
    for i in range(linha):
        col_matriz=[]
        for j in range(coluna):
            col_matriz.append(random.randint(minimo,maximo))
        li_matriz.append(col_matriz)
    return li_matriz

def main():
    qnt_linhas=int(input("Quantidade de linhas: "))
    qnt_colunas=int(input("Quantidade de colunas: "))
    min=int(input("min de numeros: "))
    max=int(input("max de numeors: "))
    linha_recorte=int(input("Insira a linha de corte: "))
    coluna_recorte=int(input("Insira a coluna de corte: "))
    recorte_linhas=int(input("valor de qnt de linhas"))
    recorte_colunas=int(input("valor de qnt de colunas"))
    matriz=geramatriz(qnt_linhas,qnt_colunas,min,max)
    matriz_recortada=extraimat(matriz,linha_recorte,coluna_recorte,recorte_linhas,recorte_colunas)
    print(matriz)
    print("_____________________________________")
    print(matriz_recortada)
main()
