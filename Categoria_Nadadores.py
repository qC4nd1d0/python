from datetime import date # Importanto o modulo datetime
print('-----CATEGORIA NADADORES-----')
print('Mirim = 9 anos ou menos\n'
      'Infantil = De 9 anos até 14\n'
      'Júnior = De 15 anos até 19\n'
      'Sênior = De 20 anos até 25\n'
      'Master = Acima de 25 anos\n')
nascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year # Ano do sistema
idade = anoAtual - nascimento # Descobrindo a idade do nadador
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: \033[1;32mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('Classificação: \033[1;35mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('Classificação: \033[1;33mJÚNIOR\033[m')
elif idade > 19 and idade <= 25:
    print('Classificação: \033[1;34mSÊNIOR\033[m')
else:
    print('Classificação: \033[1;31mMASTER\033[m')