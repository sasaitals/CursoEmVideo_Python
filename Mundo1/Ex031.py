#Escreva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
print('-----------CALCULAR VALOR DA VIAGEM-----------')
km = int(input('Insira os quilometros da viagem (KM): '))
if(km < 200):
    v1 = km * 0.50
    print(f'A viagem de {km}Km vale R${v1}')
else:
    v2 = km * 0.45
    print(f'A viagem de {km}Km vale R${v2}')
