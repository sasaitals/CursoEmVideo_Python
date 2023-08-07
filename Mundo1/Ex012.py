#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print('------CALCULADORA DE DESCONTO------')
n = float(input('Insira o valor do produto(R$): '))

d = n - ((5 / 100) * n)

print(f'O produto ganhou tem 5% de desconto \nO novo valor é de R${d: .2f}')
