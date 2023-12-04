from random import randint # Importanto a classe randint
from time import sleep # Importanto a classe sleep
print(f'{"JOKENPO":=^40}')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura') # Array dos itens
pc = randint(0,2) # Gerando números aleatorios
print('JO')
print('KEN'.format(sleep(1))) # Demora 1 sec para mostrar
print('PO'.format(sleep(1)))
print('-=' * 20)
print('O \033[1;34mCOMPUTADOR\033[m escolheu {}'.format(itens[pc])) # Acessando o array dos itens por meio da var pc
print('\033[1;34mVOCÊ\033[m escolheu {}'.format(itens[jogador]))
print('-=' * 20)
if pc == 0: # Computador jogou pedra
    if jogador == 0:
        print('\033[01;33mEmpatou\033[m')
    elif jogador == 1:
        print('\033[1;32mVocê ganhou\033[m')
    elif jogador == 2:
        print('\033[1;31mVocê perdeu\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1: # Computador jogou papel
    if jogador == 0:
        print('\033[1;31mVocê perdeu\033[m')
    elif jogador == 1:
        print('\033[1;33mEmpatou\033[m')
    elif jogador == 2:
        print('\033[1;320mVocê ganhou\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2: # Computador jogou tesoura
    if jogador == 0:
        print('\033[1;32mVocê ganhou\033[m')
    elif jogador == 1:
        print('\033[1;31mVocê perdeu\033[m')
    elif jogador == 2:
        print('\033[1;33mEmpatou\033[m')
    else:
        print('JOGADA INVÁLIDA')