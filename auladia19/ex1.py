# Dicionário de entrada
dicionario = {'c1': 'vermelho', 'c2': 'verde', 'c3': None}

# Lista para armazenar as chaves a serem removidas
chaves_para_remover = []

# Loop para identificar itens com valor None
for chave in dicionario.keys():  # Itera sobre as chaves do dicionário
    if dicionario[chave] is None:
        chaves_para_remover.append(chave)  # Armazena a chave a ser removida

# Loop para remover as chaves identificadas
for chave in chaves_para_remover:
    del dicionario[chave]  # Remove a chave do dicionário

# Exibir o dicionário resultante
print(dicionario)

