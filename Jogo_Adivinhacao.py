# import random
from random import randint # Importanto a classe randoint
from time import sleep # Importanto a classe sleep
print('-=-' * 20)
print('Vou pensar em número de 0 a 5, tente adivinhar...')
print('-=-' * 20)
number = int(input('Que número eu pensei? '))
number_r = randint(0,5) # Gerando número aleatorio entre 0 e 5
print('PROCESSANDO...')
sleep(2)
if number == number_r: # (condição if/else) se number for = a number_r
    print(f'Parabéns, você ganhou, o número que eu pensei foi {number_r}')
else: # (condicão if/else) se number for =! de number_r
    print(f'Você perdeu, o número que eu pensei foi {number_r}')