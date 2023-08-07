#Faça um algoritmo que leia o salátio de um funcionário e mostre seu novo salário, com 15% de aumento

print('------CALCULO DE AUMENTO DE SALÁRIO------')
s = float(input('Insira o salário do funcionário(R$): '))

a = s + ((15 / 100) * s)
print(f'O funcionário ganhou ganhou um aumento de 15% no seu salário \nO novo valor é de R${a: .2f}')