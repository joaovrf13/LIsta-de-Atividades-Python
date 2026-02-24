produtos = []

precos = []

print("Digite quatro produtos para prosseguir")
for i in range(4):
    produto = input("Digite o seu produto: ")
    preco = float(input("Digite um preço para o produto: "))
    precos.append(preco)
    produtos.append(produto)
    
print(f"Segue a lista de produtos e seus respectivos preços: {produtos} {precos}")

print(f"Primeiro produto: {produtos[0]} | Valor: R$ {precos[0]}")

print(f"Último produto: {produtos[3]} | Valor: R$ {precos[3]}")

total = sum(precos)
print(F"O valor total da compra é de: R$ {total}")

produtos[1] = "Manga"
precos[1] = 70

print(f"Segue a lista e os preços atualizados: {produtos} {precos}")

