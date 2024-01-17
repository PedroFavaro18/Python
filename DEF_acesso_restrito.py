def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == "Professor" and senha == "Unip23":
        print("Login efetuado")
        return True
    else:
        return False

def hello():
    nome = input("Digite seu nome: ")
    ra = input("Digite seu RA: ")
    return nome, ra

def nota():
    np1 = float(input("Digite sua nota da NP1: "))
    np2 = float(input("Digite sua nota da NP2: "))
    return np1, np2

def calculo(np1, np2):
    media = (np1 * 4 + np2 * 6) / 10
    return media

def resultado(media):
    if media > 9 and media < 10:
        print("Conceito: A \nSituação: Aprovado")
    elif media > 7 and media < 9:
        print("Conceito: B \nSituação: Aprovado")
    elif media > 3 and media < 7:
        print("Conceito: C \nSituação: Exame")
    elif media > 0 and media < 3:
        print("Conceito: D \nSituação: DP")
    else:
        print("Nota inválida!!")

autenticado = login()

if autenticado:
    nome, ra = hello()
    np1, np2 = nota()
    media = calculo(np1, np2)
    print("Olá", nome, "\nSeu RA é:", ra)
    resultado(media)
else:
    print("Acesso não autorizado.")

       


       
       