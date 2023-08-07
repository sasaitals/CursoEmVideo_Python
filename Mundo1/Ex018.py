#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

print('---------CALCULADORA DE SENO, COSSENO E TANGENTE---------')
a = float(input('Insira o ângulo: '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print(f'Ângulo: {a} \nSeu Seno: {s: .2f} \nSeu Cosseno: {c: .2f} \nSua Tangente: {t: .2f}')