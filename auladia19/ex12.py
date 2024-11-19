# Função para filtrar somente os números pares de um dicionário
def filtrar_pares(dicionario):
    # Criar um novo dicionário com os números pares
    dicionario_filtrado = {chave: [num for num in valores if num % 2 == 0] 
                           for chave, valores in dicionario.items()}
    return dicionario_filtrado

# Exemplos de entrada

# Exemplo 1
dicionario1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
resultado1 = filtrar_pares(dicionario1)
print("Dicionário de saída para o Exemplo 1:", resultado1)

# Exemplo 2
dicionario2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
resultado2 = filtrar_pares(dicionario2)
print("Dicionário de saída para o Exemplo 2:", resultado2)
