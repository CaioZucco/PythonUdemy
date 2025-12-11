# EXERCICIO 1 AULA 54
numero = input('Digite um número inteiro: ')
try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} é impar')
except ValueError:
    print(f'O número "{numero}" não é um número inteiro')

# EXERCICIO 2 AULA 54

horario = input('Digite um horario em números inteiros: ')
try:
    horario_int = int(horario)
    if horario_int >= 0 and horario_int <= 11:
        print('Bom dia')
    elif horario_int >= 12 and horario_int <= 17:
        print('Boa Tarde')
    elif horario_int >= 18 and horario_int <= 23:
        print('Boa noite')
    else:
        print('Não reconheço o horário')
except:
    print(f'O horario inserido "{horario}" não é um número inteiro')

#EXERCICIO 3 AULA 54
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é pequeno')
    elif  tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')