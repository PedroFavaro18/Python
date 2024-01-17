numeros = [100, 20, 30, 90, 50, 60, 70, 80, 40, 100, 10]

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