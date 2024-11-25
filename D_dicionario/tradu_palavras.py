def traduzir_palavra(dicionario, palavra):
    return dicionario[palavra.lower()] if palavra.lower() in dicionario else "Tradução não disponível."

def main():
    dicionario = {"hello": "olá", "world": "mundo", "python": "pitão"}
    palavra = input("Digite uma palavra em inglês: ")
    print(traduzir_palavra(dicionario, palavra))

if __name__ == "__main__":
    main()
