#Escreva um programa que pergunte a quantidade de Km percorridas por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

print('--------ALUGUEL DE CARRO--------')
d = int(input('Insira a quantidade de dias que alugou o veiculo: '))
km = float(input('Insira os quilometros rodados(KM): '))

dp = d * 60
kmp = km * 0.15
total = dp + kmp

print(f'VALOR DIÁRIA: R$60.00 \nVALOR POR CADA KM RODADO: R$0.15 \n------------------\nDias alugados: {d} \nKm rodados: {km} \nTotal a pagar pelos dias alugados: R${dp: .2f} \nTotal a pagar pelos quilometros rodados: R${kmp: .2f} \nTotal a pagar: R${total: .2f}')