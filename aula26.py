""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###
    if operador == '+':
        soma = num_1_float  + num_2_float
        print(f'A soma de {num_1_float} e {num_2_float} é: {soma:.2f}')
    elif operador == '-':
        subt = num_1_float  - num_2_float
        print(f'A subtração de {num_1_float} e {num_2_float} é: {subt:.2f}')
    elif operador == '*':
        mult = num_1_float  * num_2_float
        print(f'A multiplicação de {num_1_float} e {num_2_float} é: {mult:.2f}')
    elif operador == '/':
        div = num_1_float  / num_2_float
        print(f'A divisão de {num_1_float} por {num_2_float} é: {div:.2f}')
    

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

    """while True:
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')
    operador = input('Digire o operador +-/*: ')

    numeros_validos = None

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um dos números digitados não é válido')
        continue

    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite um operador válido: ')
        continue

    if operador == '+':
        print(f'{numero1_float} + {numero2_float} é igual a ',numero1_float+numero2_float)
    elif operador == '-':
        print(f'{numero1_float} - {numero2_float} é igual a ',numero1_float-numero2_float)

    elif operador == '*':
        print(f'{numero1_float} * {numero2_float} é igual a ',numero1_float*numero2_float)

    elif operador == '/':
        print(f'{numero1_float} / {numero2_float} é igual a ',numero1_float/numero2_float)

    
    sair = input('Quer sair? Digite [S]air: ').lower().startswith('s')

    if sair is True:
        break

"""