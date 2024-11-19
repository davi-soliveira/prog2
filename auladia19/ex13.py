# Função para obter todas as combinações de pares chave-valor de um dicionário
def obter_combinacoes(dicionario):
    # Obter todas as chaves do dicionário
    chaves = list(dicionario.keys())
    
    # Obter todas as listas de valores
    valores = list(dicionario.values())
    
    # Variável para armazenar as combinações de pares chave-valor
    combinacoes = []
    
    # Função recursiva para gerar todas as combinações
    def gerar_combinacoes(indice, atual):
        # Quando todas as chaves forem processadas, adiciona a combinação na lista
        if indice == len(chaves):
            combinacoes.append(atual.copy())
            return
        
        # Para a chave atual, percorre todos os valores possíveis
        for valor in valores[indice]:
            atual[chaves[indice]] = valor
            gerar_combinacoes(indice + 1, atual)
            del atual[chaves[indice]]  # Remove o valor da chave atual após a chamada recursiva

    # Iniciar a recursão a partir da primeira chave
    gerar_combinacoes(0, {})
    
    return combinacoes

# Exemplos de entrada

# Exemplo 1
dicionario1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
resultado1 = obter_combinacoes(dicionario1)
print("Combinações de pares chave-valor obtidas para o Exemplo 1:")
for item in resultado1:
    print(item)

# Exemplo 2
dicionario2 = {'V': [1, 3, 5], 'VI': [1, 5]}
resultado2 = obter_combinacoes(dicionario2)
print("\nCombinações de pares chave-valor obtidas para o Exemplo 2:")
for item in resultado2:
    print(item)
