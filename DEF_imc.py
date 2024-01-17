def hello():
    nome = input("Digite seu nome: ")
    ra = input("Digite seu RA: ")
    turma = input("Digite sua turma: ")
    return nome, ra, turma

def sexo():
    genero = input("Digite seu sexo (m ou f): ").lower()
    if genero == "m":
        return "Masculino"
    elif genero == "f":
        return "Feminino"
    else:
        return "Desconhecido o gênero"
    
def cal_f(imc_F):
    if imc_F < 19:
        print("Abaixo do pesdo")
    elif imc_F >= 19 and imc_F < 24:
        print("Peso ideal")
    else:
        print("Acima do peso")

def cal_m(imc_M):
    if imc_M < 20:
        print("Abaixo do peso")
    elif  imc_M >=20 and imc_M < 25:
        print ("Peso ideal")
    else: 
        print("Acima do peso")

def calculadora(peso, altura):
    imc = peso /(altura** 2)
    return imc 

nome, ra, turma = hello()

peso_ususario = float(input("Digite seu peso (Kg): "))
altura_usuario = float(input("Digite sua altura (m): "))

imc_ususario = calculadora(peso_ususario, altura_usuario)

genero_usuario = sexo()

print("Olá", nome, "\nSeu RA é:", ra, "\nSua turma é:", turma)

if genero_usuario == "Feminino":
    cal_f(imc_ususario)
elif genero_usuario == "Masculino":
    cal_m(imc_ususario)
else:
    print("Gênero desconhecido")
