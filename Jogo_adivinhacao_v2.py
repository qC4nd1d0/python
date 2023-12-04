from random import randint
tentativas = 1
print('Olá, sou seu computador...' + '\nAcabei de pensar em um número entre 0 e 10.' + '\nSerá que você consegue adivinhar qual foi? ')
number_user = int(input('Qual seu palpite? '))
number_pc = randint(0,10) # gerando número aleatorio entre 0 e 10
while number_user != number_pc:
    tentativas += 1 # contando quantas * passou no while
    if number_user < number_pc:
        number_user = int(input('Mais... Tente novamente: '))
    if number_user > number_pc:
        number_user = int(input('Menos... Tente novamente: '))
print(f'Você acertou com \033[1;31m{tentativas}\033[m tentativa(s). \033[1;32mParabéns!\033[m')
print(f'Eu pensei no número {number_pc}')