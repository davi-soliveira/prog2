# Dicionário de entrada
dicionario = {'Ciência': [88, 89, 62, 95], 'Linguagem': [77, 78, 84, 80]}

# Lista para armazenar os dicionários resultantes
lista_de_dicionarios = []

# Número de elementos nas listas (assumimos que todas as listas têm o mesmo tamanho)
tamanho = len(next(iter(dicionario.values())))  # Obtém o tamanho de uma lista

# Loop para criar os dicionários a partir dos valores das listas
for i in range(tamanho):
    novo_dicionario = {}
    for chave, lista in dicionario.items():
        novo_dicionario[chave] = lista[i]
    lista_de_dicionarios.append(novo_dicionario)

# Exibir a lista de dicionários resultante
print(lista_de_dicionarios)
