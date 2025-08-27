"""
format() em Python. O método str. format() é usado para inserir valores em strings de uma maneira mais organizada. 
É possível usar o método format() para inserir valores em uma string em qualquer posição que você desejar, usando 
parâmetros posicionais – valores numéricos iniciando em zero, dentro de chaves { }.
"""

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)