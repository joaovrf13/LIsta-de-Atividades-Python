Cadastro = []

Nome = input("Digite um nome: ")
Senha = input("Digite uma senha: ")

Novo_Cadastro ={
 "Nome": Nome,
 "Senha": Senha  
}
Cadastro.append(Novo_Cadastro)

print(f"Dados cadastrais: {Cadastro}")
