# Função para converter dicionário em lista de listas
def dicionario_para_lista(dicionario):
    # Usar list comprehension para criar a lista de listas a partir dos itens do dicionário
    return [[chave, valor] for chave, valor in dicionario.items()]

# Exemplos de entrada

# Exemplo 1
dicionario1 = {1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
resultado1 = dicionario_para_lista(dicionario1)
print("Lista de listas para o Exemplo 1:", resultado1)

# Exemplo 2
dicionario2 = {'1': 'Augusto Leite', '2': 'Natália Horans', '3': 'Alfredo Mullins', '4': 'Jana Rodes'}
resultado2 = dicionario_para_lista(dicionario2)
print("Lista de listas para o Exemplo 2:", resultado2)
