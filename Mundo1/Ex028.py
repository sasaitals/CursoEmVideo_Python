#Escreva um progama que leia um computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuario venceu ou perdeu. 
from random import randint
c = randint(1, 5)
print('---------ADVINHE O NÚMERO QUE O COMPUTADOR PENSOU----------')
n = int(input('Insira o númoro que você acha que o computador pensou: '))

if(c == n):
    print('Parabéns você acertou!!!')

else:
    print(f'Você erou :( pensei no número {c}')