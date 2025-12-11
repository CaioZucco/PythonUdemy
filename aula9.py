# Precedência dos Operadores
# 1. (n+n)
# 3. **
# 4. * / // %
# 5. + -

"""conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)"""

# Exercicio IMC
nome = 'Caio'
altura = 1.85
peso = 94.5
imc = peso / altura**2
print(nome,'tem','altura de',altura,',pesa',peso,'kgs','e seu imc é',imc)

# Usando f-strings
linha = f'{nome} tem altura de {altura}, pesa {peso} kgs e seu imc é {imc:.2f}'
print(linha)


formato = '{n} tem altura de {a}, pesa {p} kgs e seu imc é {i:.2f}'
print(formato.format(n=nome,a=altura,p=peso,i=imc))