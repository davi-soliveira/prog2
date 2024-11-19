# Função para extrair valores associados a uma chave de uma lista de dicionários
def extrair_valores(lista_dicionarios, chave):
    # Usando list comprehension para extrair os valores da chave
    return [dicionario[chave] for dicionario in lista_dicionarios if chave in dicionario]

# Exemplos de uso

# Exemplo 1: Dicionários de entrada
lista_entrada1 = [{'Matemática': 90, 'Ciência': 92}, {'Matemática': 89, 'Ciência': 94}, {'Matemática': 92, 'Ciência': 88}]
chave1 = 'Ciência'

# Exemplo 2: Dicionários de entrada
lista_entrada2 = [{'Matemática': 90, 'Ciência': 92}, {'Matemática': 89, 'Ciência': 94}, {'Matemática': 92, 'Ciência': 88}]
chave2 = 'Matemática'

# Extrair valores para a chave 'Ciência'
resultado1 = extrair_valores(lista_entrada1, chave1)
print(f"Valores associados à chave '{chave1}': {resultado1}")

# Extrair valores para a chave 'Matemática'
resultado2 = extrair_valores(lista_entrada2, chave2)
print(f"Valores associados à chave '{chave2}': {resultado2}")
