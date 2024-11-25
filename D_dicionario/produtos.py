def adicionar_produto(catalogo, id, nome, preco):
    if id not in catalogo:
        catalogo[id] = {"nome": nome, "preco": preco}

def remover_produto(catalogo, id):
    if id in catalogo:
        del catalogo[id]

def atualizar_produto(catalogo, id, nome=None, preco=None):
    if id in catalogo:
        if nome is not None:
            catalogo[id]["nome"] = nome
        if preco is not None:
            catalogo[id]["preco"] = preco

def exibir_produtos(catalogo):
    for id, dados in catalogo.items():
        print(f"ID: {id}, Nome: {dados['nome']}, Preço: {dados['preco']}")

def main():
    produtos = {}
    adicionar_produto(produtos, 1, "Mouse", 50.0)
    adicionar_produto(produtos, 2, "Teclado", 100.0)
    exibir_produtos(produtos)
    remover_produto(produtos, 1)
    atualizar_produto(produtos, 2, preco=120.0)
    exibir_produtos(produtos)

if __name__ == "__main__":
    main()
