"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
"""variavel = 'Olá mundo'
print(len(variavel))
print(variavel[2])
print(variavel[-7])
print((len(variavel[1:7])))
print(variavel[-8:-2])
print(variavel[0:len(variavel):1]) #len(variavel) = 9 (tamanho da string)
print(variavel[-1:-10:-1])
print(variavel[::-1])"""

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome TEM espaços')
    else:
        print('Seu nome NÃO tem espaços')

    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
   
else:
    print('Desculpe, você deixou campos vazios.')

  