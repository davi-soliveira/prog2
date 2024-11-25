def contar_caracteres(texto):
    contagem = {}
    for char in texto:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
    return contagem

def main():
    texto = input("Digite uma string: ")
    contagem = contar_caracteres(texto)
    for char, freq in contagem.items():
        print(f"{char}: {freq}")

if __name__ == "__main__":
    main()
