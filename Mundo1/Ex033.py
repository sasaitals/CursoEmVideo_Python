#Faça um programa que leia três números e mostre qual é o maior e o menor
print('---------VERIFICANDO NÚMEROS---------')
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print(f'O maior numero digitado é {maior} e o menor {menor}!')