DadosEmpresa = []

NomeDaEmpresa = input("Digite o nome da Empresa: ")
Documento = input("Digite o CNPJ da empresa: ")
Cidade = input("Digite a cidade da empresa: ")

DadosEmpresa.append((NomeDaEmpresa, Documento, Cidade))

print(f"Segue os dados cadastrais da empresa: {DadosEmpresa}")
print(f"O nome da empresa é: {DadosEmpresa[0][0]}")
print(f"A cidade da empresa é {DadosEmpresa[0][2]}")