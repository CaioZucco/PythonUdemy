# Jogo de adivinhação de palavra secreta com validação de entrada
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0



"""palavra_secreta = "engenharia"
letras_descobertas = ["*" for _ in palavra_secreta]
tentativas = 0

print("Bem-vindo ao jogo da palavra secreta!")
print("Tente adivinhar a palavra digitando uma letra por vez.")

while "*" in letras_descobertas:
    letra = input("Digite uma letra: ").lower()

    # Verificação de entrada
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida! Digite apenas UMA letra do alfabeto.")
        continue

    tentativas += 1

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        print("Letra incorreta!")

    print("Palavra:", "".join(letras_descobertas))
    print("Tentativas:", tentativas)

print("\nParabéns! Você descobriu a palavra secreta:", palavra_secreta)
print("Total de tentativas:", tentativas)
"""