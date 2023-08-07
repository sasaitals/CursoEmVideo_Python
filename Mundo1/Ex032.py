#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
print('---------VERIFICAÇÃO DE ANO BISEXTO---------')
a = int(input('Insira um ano qualquer: '))
if a % 4 == 0:
    print(f'O ano {a} é BISSEXTO!')
else:
    print(f'O ano {a} não é BISSEXTO!')