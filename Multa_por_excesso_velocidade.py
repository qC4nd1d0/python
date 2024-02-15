velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    velocidade = (velocidade - 80) * 7.0
    print(f'MULTADO! Você excedeu o limite de 80km/h\nVocê deve pagar uma multa de R${velocidade} reais')
else:
    print('Tenha um bom dia, dirija com segurança!')