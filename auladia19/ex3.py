# Função para converter listas em dicionários aninhados
def listas_para_dicionarios(*listas):
    resultado = []
    # Verificar se todas as listas têm o mesmo tamanho
    tamanho = len(listas[0])
    
    # Loop para iterar sobre os índices das listas
    for i in range(tamanho):
        # Criação do dicionário aninhado para cada conjunto de elementos
        dicionario = {}
        for j in range(len(listas)):
            if j == 0:
                chave = listas[j][i]
            elif j == 1:
                chave_interna = listas[j][i]
            else:
                valor = listas[j][i]
        
        # Associando os valores das listas em um dicionário aninhado
        dicionario[chave] = {chave_interna: valor}
        resultado.append(dicionario)
    
    return resultado

# Listas de entrada
list1 = ['S001', 'S002', 'S003', 'S004']
list2 = ['Pedra da Cebola', 'Praça do Papa', 'Costa Pereira', 'Reserva Paulo Vinhas']
list3 = [85, 98, 89, 92]

# Passando as listas para a função
resultado = listas_para_dicionarios(list1, list2, list3)

# Exibir o dicionário resultante
print(resultado)
