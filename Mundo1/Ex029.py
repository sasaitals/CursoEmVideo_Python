#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. A multa irá custar R$7,00 por cada Km acima do limite.
print('---------RADAR---------')
km = float(input('Insira a quilometragem: '))
if(km > 80):
    km2 = km - 80
    p = km2 * 7
    print(f'Você foi multado por ultrabassar a velocidade. Você deverá pagar uma uma multa de R${p}')
else:
    print('Parabéns, você não ultrapassou o limite de velocidade :)')