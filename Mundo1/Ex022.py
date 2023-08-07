#Crie um programa que leia o nome de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quatas letras ao todo sem comtar espaços.
#Quantas letras tem o primeirop nome.

print('---------NOME COMPLETO---------')
n = str(input('Insira seu nome completo: ')).strip()
e = len(n) - n.count(' ')
print(f'Nome em maiúsculas: {n.upper()}')
print(f'Nome em minúsculas: {n.lower()}')
print(f'Quantidade total de letras: {e}')
s = n.split()
print(f'Primeiro nome: {s[0]}')
print(f'Quantidade de letras no primeiro nome: {len(s[0])}')
