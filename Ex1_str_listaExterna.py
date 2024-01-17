import ast

numeros = None

def a():
    print(numeros)

def b():
    print("O tamanho da lista é: " + str(len(numeros)))

def c():
    numeros_ordenados = sorted(numeros)
    print(numeros_ordenados)

def d():
    numeros_repetidos = {}
    for i, num in enumerate(numeros):
        if numeros.count(num) > 1:
            if num not in numeros_repetidos:
                numeros_repetidos[num] = [i]
            else:
                numeros_repetidos[num].append(i)

    if numeros_repetidos:
        print("A lista tem números repetidos:")
        for num, posicoes in numeros_repetidos.items():
            print(f"Número {num} nas posições: {posicoes}")
    else:
        print("A lista não tem números repetidos.")

with open("Ex1_ListaNumerosa.txt", "r") as arquivo:
    linha = arquivo.read().strip()
    try:
        numeros = ast.literal_eval(linha)
        if isinstance(numeros, list):
            print("Arquivo lido com sucesso.")
        else:
            raise ValueError("Conteúdo não é uma lista válida.")
    except (ValueError, SyntaxError):
        print("Conteúdo do arquivo não é uma lista válida.")

print("a) Imprima o conteúdo da lista")
print("b) Determine o tamanho conteúdo da lista")
print("c) Coloque em ordem ascendente")
print("d) A lista tem números repetidos? Em caso afirmativo, em qual posição?")
opcao = input("Digite uma opção: ")

if opcao == "a":
    a()
elif opcao == "b":
    b()
elif opcao == "c":
    c()
elif opcao == "d":
    d()
else:
    print("Opção errada")