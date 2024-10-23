'''
se cada palavra do input for diferente das letras in vogais retornar quantas consoates tem a palavra
'''
def checa_vogais(cons):
    vogais = ['a','e','i','o','u']
    acentos = ["á", "à", "ã", "â", "é", "è", "ê", "í", "ì", "î", "ó", "ò", "õ", "ô", "ú", "ù",
     "û", "ç", "Á", "À", "Ã", "Â", "É", "È", "Ê", "Í", "Ì", "Î", "Ó", "Ò", "Õ", "Ô", "Ú", "Ù", "Û", "Ç"]
    consoante = 0
    for j in cons:
        if j in acentos:

    
    for letra in cons:
        if letra not in vogais:
            consoante += 1
    return consoante
            
def loadLista(nome_arquivo):
    lst = []
    arq = open(f'{nome_arquivo}', "rt")
    

    conteudo = arq.readline()
    while conteudo != "":
        lst.append(conteudo.strip())
        conteudo = arq.readline()

    arq.close()
    
    return lst

def main():
    palavra = loadLista('palavras.txt')
    for i in palavra:
        print(f'a palavra {i} tem {checa_vogais(i)} consoantes')


if __name__ == "__main__":
    main()