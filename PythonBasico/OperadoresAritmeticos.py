adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)


# Concatenacao com operadores:

concatenacao = 'Harry' + ' ' + 'Potter'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Harry'
print(a_dez_vezes)
print(tres_vezes_luiz)

# Precedencia entre os operadores (o que vai ser executado primeiro):
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)


# Exercício: Seu João Estephano tem 1.80 de altura, pesa 95 Kg e seu IMC é de:
# 29.320987654320987

nome = 'João Estephano'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

print('IMC do ', nome, ':', imc)