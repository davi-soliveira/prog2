"""
    CONSTRUA O TAD EQUAÇÃO DO SEGUNDO GRAU. FAÇA UMA ESCOLHA PARA IMPLEMENTAR E CONSTRUA A SEGUINTE INTERFACE:

a) new_eq(ca, cb, cc)
b) getA (tad), get(B), getC(tad)
c) quant_raizes(tad)
d) getRaize1(tad)    
e) getRaize2(tad)

PESQUISE 3 USOS DE UMA EQUAÇÃO DO SEGUNDO GRAU E CONSTRUA UMA APLICAÇÃO EXEMPLO PARA CADA UMA DESSES CASOS DE USO.

PRINCIPAL IDEIA DO TAD E ABSTRAÇÃO E REUSO.
"""
import cal_raiz as ca

def main():
    lista_ch = []
    eq = open('equacao.txt', 'rt')
    linha = eq.readline()
    while linha != "":
        lista = linha.strip().split(', ')
        print(lista)
        raiz = ca.new_eq(float(lista[0]),float(lista[1]),float(lista[2]))
        print(raiz)

        linha = eq.readline()


if __name__ == "__main__":
    main()
