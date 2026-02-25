Cliente =[]

Nome = input("Digite seu nome: ")
Idade = int(input("Digite sua idade: "))
Cidade = input("Digite sua cidade: ")
Telefone = input("Digite seu telefone: ")


Cliente.append((Nome,Idade,Cidade,Telefone))

print(f"Segue todos os dados do cliente: {Cliente}")