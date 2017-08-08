import random # importa a biblioteca random para gerar números aleatórios #

#palavras = ['abacate','chocolate','paralelepipedo','goiaba'] # gera uma variável que possui uma lista de palavras #
palavras = []
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def palavrasescolhidas():#cria uma função para poder escolher as palavras do jogo#
    global palavras
    while True:
        palavrasescolhidas = input("Digite aqui as palavras que você quer para o jogo:")
        if palavrasescolhidas == "":
            break
        palavras.append(palavrasescolhidas)
def principal(): # defini uma função #
    """
    Função Princial do programa
    """
    print('F O R C A')
    palavrasescolhidas()#chama a função#

    palavraSecreta = sortearPalavra() # essa variável chama uma função #
    palpite = '' # pede um palpite de uma letra sobre a palavra sorteada #
    desenhaJogo(palavraSecreta,palpite)

    while True: # estrutura de repetição, executada apanas quando for verdadeiro #
        palpite = receberPalpite() # chama a função receber palpite #
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo(): # essa função confere a quantidade de letras erradas, se esse número for igual ao número de letras da palavras a função retorna ao global#
    global FORCAIMG # esse por sua vez chama a imagem da forca referente ao número de letras erradas #
    if len(letrasErradas) == len(FORCAIMG): # se as letras erradas forem igual ao nuḿero de imagens da forca, você perdeu (o len conta a quantidade de elementos) #
        return True
    else:  # caso o contrário o jogo continua normalmente #
        return False
    
def ganhouJogo(palavraSecreta): # essa função confere se você acertou a letra, chamando a palavra que foi sorteada #
    global letrasCertas # chama a variável que pede uma letra #
    ganhou = True # uma variável com o valor verdade #
    for letra in palavraSecreta: # confere se a letra que você disse tem na palavra que foi sorteada #
        if letra not in letrasCertas: # se a palavra não tiver essa letra, a variável "ganhou" se torna falsa #
            ganhou = False 
    return ganhou  # "global" retorna ao seu valor inicial (verdadeiro), para as próximas letras #       
        


def receberPalpite(): # essa função pede um palpite sobre uma letra da palavra #
    
    palpite = input("Adivinhe uma letra: ") # pede para adivinhar uma letra #
    palpite = palpite.upper() # coloca as letras do palpite em letra maiúsculas #
    if len(palpite) != 1: # confere se você digitou apanas uma letra #
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas: # confere se você já disse essa letra #
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": # confere se você digitou algo fora do alfabeto #
        print('Por favor escolha apenas letras')
    else:
        return palpite # retorna ao palpite para você tentar a próxima letra #
    
    
    
def desenhaJogo(palavraSecreta,palpite): # chama as variáveis globais #
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) # imprime os desenhos da forca, de acordo com a quantidade de letras erradas #
    
     
    vazio = len(palavraSecreta)*'-' # para cada letra da palavra adiciona um tracinho #
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas ) # imprime o números de acertos e mostra as letras certas #
    print('Erros: ',letrasErradas) # imprime o número de erros e mostra as letra erradas #
    print(vazio) # imprime a quantidade de tracinhos para cada letra #
     

def sortearPalavra(): # sortea uma palavra da lista palavras #
    global palavras
    return random.choice(palavras).upper()

    
principal() #chama o programa principal
