def contar_dezenas(arquivo):
    contagem = {}
    with open(arquivo, 'r') as f:
        for linha in f:
            dezenas = linha.strip().split()
            for dezena in dezenas:
                if dezena not in contagem:
                    contagem[dezena] = 0
                contagem[dezena] += 1
    return contagem

def main():
    arquivo = "megasena.txt"
    contagem = contar_dezenas(arquivo)
    for dezena, freq in sorted(contagem.items(), key=lambda x: int(x[0])):
        print(f"{dezena}: {freq}")

if __name__ == "__main__":
    main()
