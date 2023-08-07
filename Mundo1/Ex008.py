#Escreva um programa que leia um valor em metros e exiba convertido em centímetos e milímetros

print('--------CONVERSOR DE METROS PARA CENTÍMETROS E MILÍMETROS--------')
n = float(input('Digite um número em metros: '))

#1º
cm = n * 100
m = n * 1000

print(f'Metros: {n}\nCentímetros: {cm}\nMilímetros: {m}')

#2º
print(f'Metros: {n}\nCentímetros: {n *100}\nMilímetros: {n * 1000}')