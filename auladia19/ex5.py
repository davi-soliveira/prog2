# Listas de entrada
pares = [('amarelo', 1), ('azul', 2), ('amarelo', 3), ('azul', 4), ('vermelho', 1)]

# Dicionário para armazenar os agrupamentos
dicionario = {}

# Loop para agrupar os valores por chave
for cor, valor in pares:
    if cor in dicionario:
        dicionario[cor].append(valor)  # Adiciona o valor à lista existente
    else:
        dicionario[cor] = [valor]  # Cria uma nova chave com uma lista contendo o valor

# Exibir o dicionário resultante
print(dicionario)