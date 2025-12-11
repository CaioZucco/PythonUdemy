"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro do número {numero_str} é {numero_float * 2:.2f}')
except:
    print('O que você digitou não é um número')