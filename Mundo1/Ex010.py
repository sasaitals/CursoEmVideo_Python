#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considerando US$1,00 = 5,01
print('------CONVERSOR DE REAL PARA DÓLAR------')
rs = float(input('Insira o valor em reais(R$): '))

#Duas formar de execução
#1º
d = rs / 5.01
print(f'Convertendo o valor R${rs} \nUS${d: .2f}')

#2º
print(f'Convertendo o valor R${rs} \nUS${rs / 5.01: .2f}')