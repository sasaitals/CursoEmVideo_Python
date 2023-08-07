#Crie um programa que leia um número inteiro e diga de ele é PAR ou ÍMPAR
print('---------PAR OU ÍMPAR---------')
n = int(input('Insira um número inteiro: '))
if(n % 2 == 0):
    print(f'O número {n} é PAR!')
else:
    print(f'O número {n} é ÍMPAR!')