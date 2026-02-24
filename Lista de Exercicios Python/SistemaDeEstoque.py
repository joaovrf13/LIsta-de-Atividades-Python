Estoque = []
Quantidades = []



print("Digite quatro produtos para prosseguir")
for i in range(4):
    produto = input("Digite o seu produto: ")
    quantidade= int(input("Digite a quantidade do seu produto: "))
    Estoque.append(produto)
    Quantidades.append(quantidade)
    
print(f"Segue a lista completa de produtos em estoque: {Estoque}")
print(f"O estoque do primeiro produto: {Estoque[0]} é de {Quantidades[0]}")
print(f"O estoque do último produto: {Estoque[3]} é de {Quantidades[3]}")
Total_Produtos_Estoque = len(Estoque)
Quantidade_Estoque = sum(Quantidades)
print(f"O total de produtos cadastrados no estoque é de: {Total_Produtos_Estoque} ")
print(f"A quantidade total de produtos em estoque é de: {Quantidade_Estoque}")
    