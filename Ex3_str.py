nome = ["Jose", "Pedro", "Suzana", "Gisele", "João", "Andre", "Carlos", "Natalia"]
p1 = [3.5, 7.5, 6.5, 8, 3.5, 6, 1.5, 6]
p2 = [5.5, 7.5, 5.5, 7.5, 5.5, 7, 4, 5.5]
p3 = [1.5, 8, 7.5, 5, 2, 9, 7, 8.5]

def med(p1, p2, p3):
    md = (p1 + p2 + p3) / 3
    if md >= 6:
        situacao = "Aprovado"
    else:
        situacao = "DP"
    return md, situacao

def max_min(notas):
    maxima = max(notas)
    minima = min(notas)
    return maxima, minima

print("a) Crie uma função que calcule a média das notas de cada estudante e imprime a média de cada estudante e se ele está 'aprovado' ou 'reprovado'")
print("b) Crie uma função que determine a nota mínima e máxima da turma")
opcao = input("Digite uma opção: ")

if opcao == "a":
    for i in range(len(nome)):
        media, situacao = med(p1[i], p2[i], p3[i])
        print(f"{nome[i]}: Média = {media:.2f}, Situação = {situacao}")
elif opcao == "b":
    maxima, minima = max_min(p1 + p2 + p3)
    print(f"A maior nota foi:  {maxima:.2f}")
    print(f"A menor nota foi:  {minima:.2f}")
else:
    print("Opção inválida")