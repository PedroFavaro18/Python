itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate","Miojo"]
import random


def a():
    itens_escolhidos = random.sample(itens_compra, 5)
    print("Itens Escolhidos Aleatoriamente:")
    for item in itens_escolhidos:
        print(item)

def b():
    print(itens_compra)

def c():
    itens_compra.append("óleo de canola")
    print(itens_compra)

def d():
    itens_compra.remove("Tomate")
    print(itens_compra)

print("a) inicialize uma lista de compras com 5 itens diferentes e exiba")
print("b) Imprima o conteúdo da lista")
print("c) Acrescente mais um item na lista de compras “óleo de canola”")
print("d) Remova da lista de compras o item “Tomate”")

opção = input("Digite uma opção: ")

if opção == "a":
    a()
elif opção == "b":
    b()
elif opção == "c":
    c()
elif opção == "d":
    d()
else: 
    print("Opção errada")