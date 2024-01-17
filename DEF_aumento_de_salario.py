def ajuste(salario):
    if salario <= 1500 :
        return salario * 1.20
    elif (salario > 1500) and (salario <2500) :
        return salario * 1.10
    else:
        return salario * 1.05

salario = float(input("Digite seu salário: R$ "))
print("Ajuste de salário: R$ ", ajuste(salario))
    