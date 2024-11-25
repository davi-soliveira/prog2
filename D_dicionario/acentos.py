def remover_acentos(texto):
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 
        'é': 'e', 'è': 'e', 'ê': 'e', 
        'í': 'i', 'ì': 'i', 'î': 'i', 
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 
        'ú': 'u', 'ù': 'u', 'û': 'u', 
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 
        'É': 'E', 'È': 'E', 'Ê': 'E', 
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 
        'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O', 
        'Ú': 'U', 'Ù': 'U', 'Û': 'U'
    }
    
    texto_sem_acentos = ''
    
    for char in texto:
        # Se o caractere estiver no dicionário, substitui pelo correspondente sem acento
        if char in acentos:
            texto_sem_acentos += acentos[char]
        else:
            texto_sem_acentos += char
    
    return texto_sem_acentos

def main():
    texto = input("Digite um texto com acentos: ")
    texto_sem_acentos = remover_acentos(texto)
    print(f"Texto original: {texto}")
    print(f"Texto sem acentos: {texto_sem_acentos}")

if __name__ == "__main__":
    main()
