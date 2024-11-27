def load(lista):
    with open(lista, 'r') as contato:
        cont = []
        for i in contato:
            cont.append(i.split(','))
        
        return cont
def tratar_dados(dados):
    nome = []
    telefone=[]
    print(dados)
    for i in dados:
        print(i)
        for j,k in i:
            print(j)
            print(k)
    

def main():
    telefone =load('telefone.txt')
    tratar_dados(telefone)




if __name__ == "__main__":
    main()