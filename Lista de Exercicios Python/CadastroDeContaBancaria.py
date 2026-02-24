Conta = []

NumeroConta = int(input("Digite o número da sua conta: "))
NomeCliente = input(("Digite o seu nome: "))
Saldo = float(input("Digite o seu saldo bancario: "))

Conta.append((NumeroConta, NomeCliente,Saldo))

print("==========================================")
print("          Dados Bancarios                ")
print("==========================================")
print(Conta)
print(f"O nome do cliente é: {Conta[0][1]}")
print(f"O saldo total da conta é de: R$ {Conta[0][2]}")