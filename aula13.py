"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(maior_ou_igual)

#Exercicio if, elif, else
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor=} é maior que o {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'O {segundo_valor=} é maior que o {primeiro_valor=}')
else:
    print('Os Valores são iguais!')