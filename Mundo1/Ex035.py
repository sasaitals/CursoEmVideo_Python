#Descreve um programa que leia o comprimento de três retas e diga ao usuáio de elas podem ou não formar um triângulo.
print('---------VERIFICAÇÃ DE TRIÂNGULO---------')
r1 = float(input('Insira a primeira reta: '))
r2 = float(input('Insira a segunda reta: '))
r3 = float(input('Insira a terceira reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Com estas medidas, PODE formar um triângulo!')
else:
    print('Com estas medidas, NÃO PODE formar um triângulo!')