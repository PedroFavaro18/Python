def a ():
    nome = input("Digite o nome da pessoa: ")
    sexo = input("Digite o sexo(M OU F): ")
    idade = input("Digite a idade: ")
    pessoa = {"Nome": nome, "Sexo": sexo,  "Idade": idade}

    return pessoa

def armazena ():
    pessoas = []
    for _ in range(10):
        pessoa = a()
        pessoas.append(pessoa)

    return pessoas

def salvar_em_arquivo(pessoas, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for pessoa in pessoas:
            arquivo.write(f"Nome: {pessoa['Nome']}, Sexo: {pessoa['Sexo']}, Idade: {pessoa['Idade']}\n")

def mostrar_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome: {pessoa['Nome']}, Sexo: {pessoa['Sexo']}, Idade: {pessoa['Idade']}")

# Armazenar os dados de 10 pessoas
lista_de_pessoas = armazena()
# Salvar os dados em um arquivo externo
salvar_em_arquivo(lista_de_pessoas, "Ex3_ListaClientes.txt")
# Mostrar as informações das pessoas
mostrar_pessoas(lista_de_pessoas)