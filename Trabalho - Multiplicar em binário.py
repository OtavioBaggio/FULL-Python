    #Aluno: José Otávio Ribeiro Baggio
    #Trabalho - Multiplicar dois números bináios e o resultado ser(em decimal) entre 0 a 16

memoria = ['1000', '1111', '1111', '1010']
acumulador = ['0000']

# comandos aceitos
# 00 - LER
# 01 - ESCREVER
# 10 - MULTIPLICAR

instrucao = '10000010'  # Instrução tem 8 bits

def mostraMemoria():
    mem = ''
    for posicao in memoria:
        mem = mem + posicao
    print(mem)

def mostraAcumulador():
    print("Acumulador:", acumulador[0])

def ler(posicao):
    global acumulador
    acumulador[0] = memoria[posicao]
    mostraAcumulador()

def escrever(posicao, dado):
    global acumulador, memoria
    memoria[posicao] = dado
    mostraMemoria()

def multiplicar(endDec, dado):
    global memoria
    valor = memoria[endDec]
    print('Multiplicação de binário para decimal(caso valor seja superior a 16, o resultado será mostrado em binário):')
    valorDec = int(valor, 2)            # Convertendo o valor binário pra decimal
    dadoDec = int(dado, 2)              # Converte a instrução para decimal
    resultado = valorDec * dadoDec      # Multiplica o resultado em decimal
    
    # Se o resultado for maior que 16, limitar em 16:
    if resultado > 16:
        resultado = 16
    
    resultadoBin = bin(resultado)[2:].zfill(5)      # Adicionando zero para ajustar à 5 bits (0 a 16)
    memoria[endDec] = resultadoBin                  # Atualizar a memória com o resultado
    #Imprimindo o resultado:
    print(f'Multiplicando {valor} ({valorDec}) por {dado} ({dadoDec}) = {resultado} ({resultadoBin})')
    mostraMemoria()

def executaInstrucao(instr):
    com = instr[:2]
    comDec = int(com, 2)
    end = instr[2:4]
    endDec = int(end, 2)
    dado = instr[4:]
    print(com, comDec, end, endDec, dado)
    
    if comDec == 0:
        ler(endDec)
    elif comDec == 1:
        escrever(endDec, dado)
    elif comDec == 2:  # Comando para multiplicar
        multiplicar(endDec, dado)

mostraMemoria()
executaInstrucao(instrucao)
