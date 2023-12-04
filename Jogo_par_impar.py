from random import randint
numberUser = numberPc = soma = par = contador = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
while True:
    numberPc = randint(0, 10)  # gerando números aleatorios de 0 a 10
    numberUser = int(input('Digite um valor: '))
    palpite = str(input('Par ou Ímpar [P/I] ')).upper().strip()[0] # maius, remover espaços e considerar 1º letra
    soma = numberUser + numberPc
    par = soma % 2 # resto da divisão
    if palpite in 'Pp' and par == 0:
        print('-' * 30)
        print(f'Você jogou {numberUser} e o computador jogou {numberPc}. Totalizando {soma} DEU PAR')
        print('Você venceu!' + '\nVamos jogar novamente...')
        print('-' * 30)
        contador += 1
    elif palpite in 'pP' and par != 0:
        print('-' * 30)
        print(f'Você jogou {numberUser} e o computador jogou {numberPc}. Totalizando {soma} DEU ÍMPAR')
        print('Você perdeu!')
        break
    if palpite in 'Ii' and par == 0:
        print('-' * 30)
        print(f'Você jogou {numberUser} e o computador jogou {numberPc}. Totalizando {soma} DEU PAR')
        print('Você perdeu!')
        break
    elif palpite in 'Ii' and par != 0:
        print('-' * 30)
        print(f'Você jogou {numberUser} e o computador jogou {numberPc}. Totalizando {soma} DEU ÍMPAR')
        print('Você venceu!' + '\nVamos jogar novamente...')
        print('-' * 30)
        contador += 1
print('-' * 30)
print(f'GAME OVER. Você venceu {contador} vezes')


