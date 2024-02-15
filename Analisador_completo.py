mediaIdade = 0
somaIdade = 0
idadeMaisVelho = 0
mulheresMenos20 = 0
for analisador in range(1, 5): # 1 até 4
    print(f'----- {analisador}º PESSOA -----')
    name = str(input('Nome: ')).strip()  # strip, desconsidera os espaços
    ayer = int(input('Idade: '))
    sexo = (input('Sexo: [M/F]: '))
    somaIdade += ayer # somaIdade = somaIdade + ayer (somando)
    mediaIdade = somaIdade / 4 # descobrindo a media (somando as idades e / pelo total)
    if sexo in 'fF':  # se for F (in considera F ou f)
        if ayer < 20:  # se tiver menos de 20 anos soma + 1
            mulheresMenos20 += 1  # (contando)
    if sexo in 'Mm': # se for do sexo M (in considera M ou m)
        if ayer > idadeMaisVelho:
            idadeMaisVelho = ayer # jogando a idade na var idadeMaisVelho
            nomeMaisVelho = name # jogando o nome na var nomeMaisVelho
print(f'A média de idade do grupo citado é {mediaIdade}')
print(f'O homem mais velho tem {idadeMaisVelho} anos e se chame {nomeMaisVelho}')
print(f'Ao todo tivemos {mulheresMenos20} mulheres com menos de 20 anos')



