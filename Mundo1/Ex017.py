#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa
print('---------CALCULADORA DE HIPOTENUSA---------')
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa destes valores é {hi: .2f}')