def maior_nota():
    maior = 0
    num_alunos = 0

    while num_alunos < 5:
        nota = float(input("Digite as notas:"))
        maior = max(maior, nota)
        num_alunos += 1
    return maior

maior = maior_nota()
print(f"A maior nota é: {maior}") 
 