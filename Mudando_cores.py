number1 = int(input('Digite o primeiro valor: '))
number2 = int(input('Digite o segundo valor valor: '))
if number1 > number2:
    print(f'O primeiro valor de {number1} é \033[32mmaior\033[m que o segundo valor de \033[31m{number2}\033[m')
else:
    print(f'O segundo valor de {number2} é \033[33mmaior\033[m que o primeiro valor de \033[35m{number1}\033[m')