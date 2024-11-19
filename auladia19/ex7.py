# Lista de dicionários de entrada
lista_de_dicionarios = [
    {'id': '#FF0000', 'cor': 'vermelho'},
    {'id': '#800000', 'cor': 'marrom'},
    {'id': '#FFFF00', 'cor': 'amarelo'},
    {'id': '#808000', 'cor': 'oliva'}
]

# ID do dicionário a ser removido
id_remover = '#FF0000'

# Loop para encontrar e remover o dicionário com o ID especificado
for dicionario in lista_de_dicionarios[:]:  # Itera sobre uma cópia da lista
    if dicionario['id'] == id_remover:
        lista_de_dicionarios.remove(dicionario)

# Exibir a lista resultante
print(lista_de_dicionarios)
