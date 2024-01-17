import os

def renomear(dir):
    count = 1
    for arquivo in os.listdir(dir):
        caminho_antigo = os.path.join(dir, arquivo)
        novo_nome = f"Foto ({count}).jpg"
        caminho_novo = os.path.join(dir, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        count += 1

dir = r'C:\Users\user\Desktop\Fotos\outro_pendrive\copia2013\fotos\parque xuxa'

renomear(dir)