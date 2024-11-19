# Função para processar o arquivo e armazenar os dados no dicionário
def processar_arquivo(arquivo):
    # Dicionário para armazenar os dados (cep -> lista de números)
    dicionario_ceps = {}
    
    # Abrir o arquivo para leitura
    with open(arquivo, 'r') as file:
        # Ler cada linha do arquivo
        for linha in file:
            # Remover qualquer espaço em branco ou caractere extra
            linha = linha.strip()
            
            # Separar o par CEP e número pelo caractere vírgula
            cep, numero = linha.split(',')
            
            # Converter o CEP para um inteiro (para garantir a consistência no dicionário)
            cep = int(cep.strip())
            numero = int(numero.strip())
            
            # Adicionar o número da casa à lista correspondente ao CEP
            if cep in dicionario_ceps:
                dicionario_ceps[cep].append(numero)
            else:
                dicionario_ceps[cep] = [numero]
    
    return dicionario_ceps

# Exemplo de uso da função
arquivo = 'enderecos.txt'  # Nome do arquivo de entrada (ajuste conforme necessário)
dicionario_resultado = processar_arquivo(arquivo)

# Exibir o dicionário resultante
print(dicionario_resultado)
