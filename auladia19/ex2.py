# Dicionário de entrada
dicionario = {'César Hilal': 175, 'Aldo Carvalho': 180, 'Maria Eleonora': 165, 'Pedro Cunha': 190}

# Dicionário para armazenar as entradas filtradas
dicionario_filtrado = {}

# Loop para identificar entradas com valores maiores que 170
for chave, valor in dicionario.items():  # Itera sobre chaves e valores do dicionário
    if valor > 170:
        dicionario_filtrado[chave] = valor  # Armazena as entradas que atendem à condição

# Exibir o dicionário resultante
print(dicionario_filtrado)
