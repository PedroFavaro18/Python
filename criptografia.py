def is_alpha(s):
    return s.isalpha()

def cifrar_vigenere(texto, chave):
    texto_cifrado = ""
    chave = chave.upper()
    indice_chave = 0

    for char in texto:
        if is_alpha(char):
            char_chave = chave[indice_chave % len(chave)].upper()
            deslocamento_chave = ord(char_chave) - ord('A')

            case_offset = ord('a') if char.islower() else ord('A')
            char_cifrado = chr((ord(char) - case_offset + deslocamento_chave) % 26 + case_offset)

            texto_cifrado += char_cifrado
            indice_chave += 1
        else:
            texto_cifrado += char

    return texto_cifrado

def decifrar_vigenere(texto_cifrado, chave):
    texto_decifrado = ""
    chave = chave.upper()
    indice_chave = 0

    for char in texto_cifrado:
        if is_alpha(char):
            char_chave = chave[indice_chave % len(chave)].upper()
            deslocamento_chave = ord(char_chave) - ord('A')

            case_offset = ord('a') if char.islower() else ord('A')
            char_decifrado = chr((ord(char) - deslocamento_chave - case_offset + 26) % 26 + case_offset)

            texto_decifrado += char_decifrado
            indice_chave += 1
        else:
            texto_decifrado += char

    return texto_decifrado

def chat():
    chave = input("Defina a senha: ")

    while True:
        remetente = input("Quem está enviando a mensagem (1 ou 2)? ('q' para sair)? ").strip()
        if remetente in ['1', '2']:
            destinatario = '2' if remetente == '1' else '1'

            texto = input(f"Pessoa {remetente}, digite a mensagem: ")

            # Remova espaços e verifique se a mensagem contém apenas caracteres alfabéticos
            if not texto.replace(" ", "").isalpha():
                print("Mensagem inválida. A mensagem deve conter apenas caracteres alfabéticos.")
                continue

            texto_cifrado = cifrar_vigenere(texto, chave)
            print("Mensagem Criptografada:", texto_cifrado)

            while True:
                chute_chave = input(f"Pessoa {destinatario}, digite a senha para descriptografar: ")
                if chute_chave == chave:
                    texto_decifrado = decifrar_vigenere(texto_cifrado, chute_chave)
                    print("Mensagem Descriptografada:", texto_decifrado)
                    break
                else:
                    print("Senha incorreta. Tente novamente.")
        elif remetente == 'q':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Digite '1', '2' ou 'q'.")

chat()