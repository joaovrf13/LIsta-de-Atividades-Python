Produtos = []


produto = input(f"Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade: "))

dados_fixos = (produto, preco)

controle_estoque = {"qtd": quantidade}

produto_Final = [dados_fixos, controle_estoque] 
Produtos.append(produto_Final)

print(Produtos)