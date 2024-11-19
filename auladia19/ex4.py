# Dicionário de entrada
dicionario = {'César': (1.77, 72), 'Aldo': (1.67, 65), 'Maria': (1.65, 68), 'Pedro': (1.72, 66)}

# Dicionário para armazenar os resultados filtrados
dicionario_filtrado = {}

# Loop para filtrar os estudantes com altura > 1.75 e peso > 70
for nome, (altura, peso) in dicionario.items():
    if altura > 1.75 and peso > 70:
        dicionario_filtrado[nome] = (altura, peso)  # Adiciona o estudante ao dicionário filtrado

# Exibir o dicionário filtrado
print(dicionario_filtrado)
