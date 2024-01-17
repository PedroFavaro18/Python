def fatorial(num):
    if num < 0 :
        return "Digite um núnmero inteiro positivo inteiro!"
    
    resultado = 1
    for fato in range(1, num + 1):
        resultado *= fato
    return resultado
        

num = int(input("Digite um número: "))
print(f"Resultado da fatoração do número {num}! é: ",fatorial(num))