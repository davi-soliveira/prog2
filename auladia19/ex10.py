# Função para calcular o comprimento dos valores de um dicionário
def calcular_comprimento_valores(dicionario):
    # Criar um novo dicionário com os valores do dicionário original e seus comprimentos
    dicionario_saida = {valor: len(valor) for valor in dicionario.values()}
    return dicionario_saida

# Exemplos de entrada

# Exemplo 1
dicionario1 = {1: 'vermelho', 2: 'verde', 3: 'preto', 4: 'branco', 5: 'preto'}
resultado1 = calcular_comprimento_valores(dicionario1)
print("Dicionário de saída para o Exemplo 1:", resultado1)

# Exemplo 2
dicionario2 = {'1': 'Augusto Leite', '2': 'Natália Horans', '3': 'Alfredo Mullins', '4': 'Jana Rodes'}
resultado2 = calcular_comprimento_valores(dicionario2)
print("Dicionário de saída para o Exemplo 2:", resultado2)
