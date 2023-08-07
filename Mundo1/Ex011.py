#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
print('------CÁLCULO ÁREA DE QUANTIDADE DE TINTA------')
b = float(input('Insira a largura da área em METROS: '))
h = float(input('Insira a altura da área em METROS: '))

#Duas formar de execução
#1º
a = b * h
t = a / 2
print(f'A área da parede é de {a: .2f}m²\nQuatidade de tinta, em litros, necessária para pintar a área: {t: .2f}')

#2º
print(f'A área da parede é de {b * h: .2f}m²\nQuatidade de tinta, em litros, necessária para pintar a área: {(b * h) / 2: .2f}')